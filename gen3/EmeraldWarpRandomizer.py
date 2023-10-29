"""
EmeraldWarpRandomizer.py

Copyright (c) 2023 AtSign, XLuma, Turtleisaac

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""
import json
import os
import random
import typing
from gen3 import EmeraldWarpMapInfo as info
from ips_util import Patch
from RandomizerUtils import Utils
from RandomizerUtils import SructureDefinitions
from RandomizerUtils import SructureDefinitions as structs


class EmeraldRandomizerFunctions(SructureDefinitions.GenRandomizerFunctions):
    def __init__(self):
        self.maps = []
        self.map_name_to_id = dict()
        self.start_map = "MAP_LITTLEROOT_TOWN"
        self.resource_path = os.path.join(os.path.join('Resources', 'gen3'), 'emerald')
        self.map_to_group_ids_map_ids = dict()
        self.map_to_warp_event_pointer = dict()
        self.warp_entry_size = 0x8

    def load_map_data(self) -> dict:
        map_warps = dict()
        for root, dirs, files in os.walk(Utils.resource_path(os.path.join(self.resource_path, 'maps'))):
            for file in files:
                if file.endswith("map.json"):
                    self.maps.append(os.path.join(root, file))

        for map_file in self.maps:
            map_data = dict()
            with open(map_file) as f:
                map_data = json.load(f)
            try:
                map_id = map_data['id']
                self.map_name_to_id[map_data['name']] = map_id
                warps = map_data['warp_events']
                connections = map_data['connections']
                temp1 = []
                temp2 = []

                # For some reason these maps aren't connected but really should be for randomizer logic
                if map_id == "MAP_UNDERWATER_SOOTOPOLIS_CITY":
                    temp2.append(structs.Connection("emerge", 0, "MAP_SOOTOPOLIS_CITY"))
                if map_id == "MAP_SOOTOPOLIS_CITY":
                    temp2.append(structs.Connection("dive", 0, "MAP_UNDERWATER_SOOTOPOLIS_CITY"))
                if map_id == "MAP_UNDERWATER_SEAFLOOR_CAVERN":
                    temp2.append(structs.Connection("emerge", 0, "MAP_SEAFLOOR_CAVERN_ENTRANCE"))
                if map_id == "MAP_SEAFLOOR_CAVERN_ENTRANCE":
                    temp2.append(structs.Connection("dive", 0, "MAP_UNDERWATER_SEAFLOOR_CAVERN"))

                if warps is not None:
                    i = 0
                    for warp in warps:
                        temp1.append(
                            structs.Warp(warp['x'], warp['y'], warp['elevation'], warp['dest_map'],
                                         warp["dest_warp_id"], i))
                        i = i + 1
                if connections is not None:
                    for connection in connections:
                        temp2.append(structs.Connection(connection['direction'], connection['offset'],
                                                        connection['map']))
                map_warps[map_id] = [temp1, temp2]
            except (KeyError, IndexError, ValueError) as e:
                # print("Error Reading Map File: " + map_file)
                continue

        return map_warps

    def define_starting_map_id(self):
        return self.start_map

    def info(self):
        return info

    def determine_unreachable_maps(self, map_nodes: dict, map_warps: dict):
        in_map = map_nodes.keys()
        total_maps = map_warps.keys()
        not_reachable = []
        for map_name in total_maps:
            if map_name not in in_map:
                if "BATTLE_FRONTIER" not in map_name and "BATTLE_TENT" not in map_name and "SECRET_BASE" not in map_name \
                        and "ARTISAN_CAVE" not in map_name and "BATTLE_PYRAMID" not in map_name \
                        and "MAP_NAVEL_ROCK_HARBOR" not in map_name and "MAP_UNION_ROOM" not in map_name \
                        and "MAP_INSIDE_OF_TRUCK" not in map_name and "UNUSED" not in map_name \
                        and "PROTOTYPE" not in map_name and "BATTLE_COLOSSEUM" not in map_name and "SOUTHERN_ISLAND" \
                        not in map_name and "TRICK_HOUSE" not in map_name and "BIRTH_ISLAND_HARBOR" not in map_name \
                        and "TRADE_CENTER" not in map_name and "CONTEST_HALL" not in map_name \
                        and "RECORD_CORNER" not in map_name and "CAVE_ENTRANCE" not in map_name \
                        and "SS_TIDAL" not in map_name and "STORE_ELEVATOR" not in map_name \
                        and "UNDERWATER_ROUTE134" not in map_name and "SEALED_CHAMBER" not in map_name \
                        and "ABANDONED_SHIP" not in map_name:
                    not_reachable.append(map_name)
                    if "NAVEL_ROCK" not in map_name and "FARAWAY" not in map_name and "BIRTH_ISLAND" not in map_name \
                            and "MARINE" not in map_name and "TERRA" not in map_name and "HIGH_TIDE" not in map_name:
                        print(map_name)
        print(len(not_reachable))
        return not_reachable

    def is_not_needed_map_ok(self, map_name: str) -> bool:
        if '_HOUSE' in map_name or 'MART' in map_name and 'MYSTERY_EVENTS' not in map_name and 'TRICK' not in map_name:
            return True
        else:
            return False

    def insert_data_into_binary(self, rom: typing.BinaryIO, map_warps, map_name_to_id, map_name, warp_id, dest_map,
                                dest_warp_id):
        # First time entering this function we need to do some setup so we can write correct info into rom
        if len(self.map_to_group_ids_map_ids) == 0:
            with open(Utils.resource_path(os.path.join(self.resource_path, 'map_groups.h'))) as f:
                lines = f.readlines()
            group_id = -1
            map_id = 0
            for line in lines:
                if line.startswith('// gMapGroup'):
                    group_id = group_id + 1
                    map_id = 0
                elif line.startswith('#define MAP'):
                    self.map_to_group_ids_map_ids[line.split(' ')[1]] = [group_id, map_id]
                    map_id = map_id + 1

        if len(self.map_to_warp_event_pointer) == 0:
            with open(Utils.resource_path(os.path.join(self.resource_path, 'message.txt'))) as f:
                map_order_lines = f.readlines()
            with open(Utils.resource_path(os.path.join(self.resource_path, 'parsed.txt'))) as f:
                pointer_lines = f.readlines()

            pointer_index = 0
            for i in range(0, len(map_order_lines)):
                tmp_map_name = map_order_lines[i].split(' ')[3].replace('\n', '')
                map_id = map_name_to_id[tmp_map_name]
                if map_id not in map_warps:
                    continue
                warps, connections = map_warps[map_id]
                if len(warps) != 0:
                    self.map_to_warp_event_pointer[tmp_map_name] = \
                        pointer_lines[pointer_index].replace('08', '0x', 1).replace('\n', '')
                    pointer_index = pointer_index + 1

        rom.seek(int(self.map_to_warp_event_pointer[map_name], base=16))
        for i in range(0, warp_id):
            # Find correct warp in warp event list
            rom.seek(8, 1)
        rom.seek(5, 1)  # we are now at dest warp
        rom.write(dest_warp_id.to_bytes(1, 'big'))
        rom.write(self.map_to_group_ids_map_ids[dest_map][1].to_bytes(1, 'big'))
        rom.write(self.map_to_group_ids_map_ids[dest_map][0].to_bytes(1, 'big'))
        rom.seek(0)

    def write_map_updates_to_binary_file(self, rom: typing.BinaryIO, maps, map_warps, map_name_to_id):
        for map_file in maps:
            if 'TerraCave_Entrance' in map_file or 'MarineCave_Entrance' in map_file:
                continue
            with open(map_file) as f:
                map_data = json.load(f)
            try:
                map_id = map_data['id']
                map_name = map_data['name']
                warp_json = map_data['warp_events']
                if warp_json is not None and map_id in map_warps:
                    warps, connections = map_warps[map_id]
                    i = 0
                    updated_json = False
                    for warp in warp_json:
                        if warps[i] is not None and warps[i].dest_map != 'MAP_NONE':
                            self.insert_data_into_binary(rom, map_warps, map_name_to_id, map_name, i, warps[i].dest_map,
                                                         warps[i].dest_warp_id)
                        i = i + 1
            except (KeyError, IndexError, ValueError) as e:
                # print("Error Reading Map File: " + map_file)
                continue

    def write_rom(self, input_file: str, output_file: str, map_warps: dict):
        patch = Patch.load(Utils.resource_path(os.path.join(self.resource_path, 'emerald_patches.ips')))
        with open(input_file, 'rb') as f_in:
            with open(output_file, 'w+b') as f_out:
                f_out.write(patch.apply(f_in.read()))

        rom = open(output_file, 'r+b')
        self.write_map_updates_to_binary_file(rom, self.maps, map_warps, self.map_name_to_id)
        rom.close()
