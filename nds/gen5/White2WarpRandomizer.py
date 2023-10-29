"""
White2WarpRandomizer.py

Pokemon White 2 Warp Randomizer

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
import typing

from nds.buffer import Buffer
from nds.gen5 import White2WarpMapInfo as info, White2WarpMapInfo
from ips_util import Patch
from RandomizerUtils import Utils
from RandomizerUtils import SructureDefinitions
from RandomizerUtils import SructureDefinitions as structs
import ndspy.rom
import ndspy.narc
import ndspy.codeCompression

from nds.gen5.FormatsGen5 import Overworlds, Matrix, Map, White2Header
from nds.tableLocator import TableLocator
import os


class White2RandomizerFunctions(SructureDefinitions.GenRandomizerFunctions):
    def __init__(self):
        self.maps = []
        self.map_name_to_id = dict()
        self.start_map = "Map_Aspertia_City"
        self.map_to_group_ids_map_ids = dict()
        self.map_to_warp_event_pointer = dict()
        self.warp_entry_size = 0x8
        self.resource_json = dict()
        self.events = []
        self.headers = []
        self.unwriteable_headers = []
        self.events_narc = None
        self.maps_narc = None
        self.matrix_narc = None
        self.scripts_narc = None
        self.text_narc = None
        self.headers_narc = None

    def load_map_data(self) -> dict:
        map_warps = dict()

        cwd = os.getcwd()
        print(cwd)
        with open(Utils.resource_path(os.path.join('Resources', 'gen5', 'White2MapResources.json'))) as f:
            self.resource_json = json.load(f)

        for map_name in self.resource_json:
            try:
                map_id = map_name
                self.map_name_to_id[map_name] = map_id
                warps = self.resource_json[map_name]['warps']
                connections = self.resource_json[map_name]['connections']
                temp1 = []
                temp2 = []
                # print(map_id)
                # for warp in warps:
                #     print('\t' + str(warp))
                # print('\t' + str(connections))

                if warps is not None:
                    i = 0
                    for warp in warps:
                        map_based_dest_warp_id = 256
                        if warp['dest_map_id'] != 'Map_None':
                            for dest_map_warp_num in range(len(self.resource_json[warp['dest_map_id']]['warps'])):
                                if self.resource_json[warp['dest_map_id']]['warps'][dest_map_warp_num]['id'] == \
                                        warp['dest_warp_id']:
                                    map_based_dest_warp_id = dest_map_warp_num
                        global_x = warp['x_pos'] + warp['map_x']*32
                        global_y = warp['y_pos'] + warp['map_y']*32
                        temp1.append(
                            structs.Warp(global_x, global_y, warp['global_z'], warp['dest_map_id'],
                                         map_based_dest_warp_id, i, warp['header_id'], warp['dest_header'],
                                         warp['width'], warp['height'], warp['is_rail']))
                        i = i + 1
                if connections is not None:
                    for connection in connections:
                        temp2.append(structs.Connection('', 0, connection))

                map_warps[map_id] = [temp1, temp2]
            except (KeyError, IndexError, ValueError) as e:
                print("Error Reading Map File \'%s\' with error involving %s" % (map_name, str(e)))
                continue

        # for map_name in PlatinumWarpMapInfo.override_maps:
        #     if map_name in map_warps:
        #         map_warps.pop(map_name)

        return map_warps
    def define_starting_map_id(self):
        return self.start_map

    def info(self):
        return info

    # Determine unreachable maps returns a list of maps that normally we were unable to get to by normal
    # warps/connections, but we have decided we still want those maps in the randomizer. For example, iron island is
    # not part of the "main loop" in Plat, but is actually always accessible from Canalave via a script so it indeed is
    # meant to be part of the loop. Additional examples can include the battle resort since it's the same deal with
    # a boat script, fullmoon and newmoon islands, birth and faraway islands in gen 3, liberty island in gen 5, etc...
    def determine_unreachable_maps(self, map_nodes: dict, map_warps: dict):
        in_map = map_nodes.keys()
        total_maps = map_warps.keys()
        not_reachable = []
        #print(in_map)
        for map_name in total_maps:
            if map_name not in in_map:
                if 'Abyssal_Ruins' not in map_name and 'Black' not in map_name and 'h295' not in map_name \
                    and 'h313' not in map_name and 'h316' not in map_name and 'h312' not in map_name and 'h311' not in map_name \
                        and 'h310' not in map_name and 'h309' not in map_name and 'h308' not in map_name and 'h293' not in map_name and 'h307' not in map_name \
                            and 'h292' not in map_name and 'h298' not in map_name and 'h291' not in map_name and 'h297' not in map_name and 'h290' not in map_name and 'h289' not in map_name \
                                and 'h314' not in map_name and 'h304' not in map_name and 'Unity_Tower' not in map_name and 'h302' not in map_name and 'h303' not in map_name and 'h301' not in map_name and \
                                    'h328' not in map_name and 'h525' not in map_name and 'h523' not in map_name and 'h521' not in map_name and 'h519' not in map_name and 'h524' not in map_name and 'h522' not in map_name \
                                        and 'h520' not in map_name and 'h327' not in map_name and 'Liberty_Garden' not in map_name and 'Strange' not in map_name:
                    not_reachable.append(map_name)
                #print(map_name)
        print(len(not_reachable))
        return not_reachable
        # return []

    def is_not_needed_map_ok(self, map_name: str) -> bool:
        if 'Interior' in map_name or 'Gate' in map_name:
            return True  # TODO add better not needed map filters
        else:
            return False

    def insert_data_into_binary(self, map_name, warp):
        can_write = True
        for map_group in info.grouped_warps:
            if map_name in White2WarpMapInfo.grouped_warps[map_group]['warps']:
                can_write = False
            elif warp.dest_map in White2WarpMapInfo.grouped_warps[map_group]['warps']:
                can_write = False

        if warp.dest_map != 'Map_None' and can_write:
            header_id = warp.header_id
            warp_id = self.resource_json[map_name]['warps'][warp.warp_id]['id']

            dest_header_id = self.resource_json[warp.dest_map]['warps'][0]['header_id']
            dest_warp_id = self.resource_json[warp.dest_map]['warps'][warp.dest_warp_id]['id']

            header = self.headers[header_id]
            if header_id not in self.unwriteable_headers:  # TODO make a better way to handle this, prob not right
                self.events[header.event_id].warps[warp_id].dest_header = dest_header_id
                self.events[header.event_id].warps[warp_id].dest_warp_id = dest_warp_id

    def write_map_updates_to_binary_file(self, map_warps):
        for map_name in map_warps:
            if map_name != 'Map_None':
                for warp in map_warps[map_name][0]:
                    self.insert_data_into_binary(map_name, warp)

    def write_header_permission_changes(self):  # makes teleport/ fly/ dig/ escape rope usable everywhere
        buffer = Buffer(self.headers_narc.files[0])
        for i in range(615):
            self.headers.append(White2Header(buffer, i))

        for header in range(len(self.headers)):
            self.headers[header].set_teleport_flag()

        size = len(buffer.data)
        buffer = Buffer(bytearray(size), write=True)
        for header in range(len(self.headers)):
            buffer.write_bytes(self.headers[header].write())

        self.headers_narc.files[0] = buffer.data

    # TODO idk if this code fully works yet
    def fix_warp_groupings(self, map_warps):
        dummy_event_num = len(self.events_narc.files) - 1
        dummy_map_num = len(self.maps_narc.files) - 1
        dummy_matrix_num = len(self.matrix_narc.files) - 1
        dummy_level_script_num = len(self.scripts_narc.files) - 1

        for group_name in White2WarpMapInfo.grouped_warps:
            entry = White2WarpMapInfo.grouped_warps[group_name]
            if 'header_dummy' in list(entry.keys()):
                map_name = list(entry['warps'].keys())[0]
                warp_on_map = entry['warps'][map_name][0]
                dummy_header = entry['header_dummy']
                resource_folder = entry['resource_folder']

                self.unwriteable_headers.append(dummy_header)

                opposite_map = map_warps[map_name][0][warp_on_map].dest_map
                opposite_warp_map_id = map_warps[map_name][0][warp_on_map].warp_id
                opposite_header = self.resource_json[opposite_map]['warps'][0]['header_id']
                true_opposite_warp = self.resource_json[opposite_map]['warps'][opposite_warp_map_id]['id']
                print(map_name + ' warps ' + str(entry['warps'][map_name]) + ' to ' + opposite_map + ' warp ' +
                      str(true_opposite_warp))

                self.events[self.headers[opposite_header].event_id].warps[true_opposite_warp].dest_header = dummy_header
                self.events[self.headers[opposite_header].event_id].warps[true_opposite_warp].dest_warp_id = 0

                with open(Utils.resource_path(
                        os.path.join('Resources', 'gen4', 'hgss_fixes', 'groupings', resource_folder, 'script.scr')),
                        'rb') as f:
                    data = bytearray(f.read())
                self.scripts_narc.files.append(data)

                self.headers[dummy_header].area_data_id = 6
                self.headers[dummy_header].matrix_id = dummy_matrix_num
                self.headers[dummy_header].level_script_id = dummy_level_script_num
                self.headers[dummy_header].event_id = dummy_event_num
                self.headers[dummy_header].script_id = len(self.scripts_narc.files) - 1
                self.headers[dummy_header].music_day_id = self.headers[opposite_header].music_day_id
                self.headers[dummy_header].music_night_id = self.headers[opposite_header].music_night_id

    def overwrite_other_data(self, map_warps):
        for group in White2WarpMapInfo.other_overwrites:
            entry = White2WarpMapInfo.other_overwrites[group]
            resource_folder = entry['resource_folder']

            print(entry)

            if 'script_overwrite' in entry:
                script_id = entry['script_overwrite']
                with open(Utils.resource_path(
                        os.path.join('Resources', 'gen5', 'white2_fixes', 'overwrites', resource_folder, 'scripts',
                                     str(script_id) + '.bin')), 'rb') as f:
                    data = bytearray(f.read())
                self.scripts_narc.files[script_id] = data
            if 'event_overwrite' in entry:
                event_id = entry['event_overwrite']
                with open(Utils.resource_path(
                        os.path.join('Resources', 'gen5', 'white2_fixes', 'overwrites', resource_folder, 'entities',
                                     str(event_id) + '.bin')), 'rb') as f:
                    data = bytearray(f.read())
                self.events[event_id] = Overworlds(Buffer(data))
            if 'map_overwrite' in entry:
                map_id = entry['map_overwrite']
                with open(Utils.resource_path(
                        os.path.join('Resources', 'gen5', 'white2_fixes', 'overwrites', resource_folder, 'maps',
                                     str(map_id) + '.bin')), 'rb') as f:
                    data = bytearray(f.read())
                self.maps_narc.files[map_id] = data
            if 'text_overwrite' in entry:
                text_id = entry['text_overwrite']
                with open(Utils.resource_path(
                        os.path.join('Resources', 'gen5', 'white2_fixes', 'overwrites', resource_folder, 'text',
                                     str(text_id) + '.bin')), 'rb') as f:
                    data = bytearray(f.read())
                self.text_narc.files[text_id] = data
            if 'matrix_overwrite' in entry:
                matrix_id = entry['matrix_overwrite']
                with open(Utils.resource_path(
                        os.path.join('Resources', 'gen5', 'white2_fixes', 'overwrites', resource_folder, 'matrix',
                                     str(matrix_id) + '.bin')), 'rb') as f:
                    data = bytearray(f.read())
                self.matrix_narc.files[matrix_id] = data

    def apply_season(self, arm9):
        buffer = Buffer(bytearray(arm9), write=True)
        base_size = bytearray([0x8B, 0x00, 0x00, 0xEB])
        base_season = bytearray(
            [0x08, 0xB5, 0x84, 0xB0, 0x00, 0xA8, 0x0F, 0xF0, 0x6B, 0xF9, 0x01, 0x98, 0x41, 0x1E, 0x03, 0x20,
             0x08, 0x40, 0x00, 0x06, 0x00, 0x0E, 0x04, 0xB0, 0x08, 0xBD])
        replacement_season = bytearray(
            [0x20, 0xf7, 0x46, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
             0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])
        for idx in range(len(buffer.data) - len(base_season)):
            buffer.pos = idx
            data = buffer.read_bytes(len(base_size))
            if data == base_size:
                print('writing size')
                buffer.pos = idx
                buffer.write_u32(0)
            buffer.pos = idx
            data = buffer.read_bytes(len(base_season))
            if data == base_season:
                print('writing season')
                buffer.pos = idx
                buffer.write_u8(0x00)  # makes it so the season is spring
                buffer.write_bytes(replacement_season)
                break
        return buffer.data

    def write_rom(self, input_file: str, output_file: str, map_warps: dict):
        print('writing')
        rom = ndspy.rom.NintendoDSRom.fromFile(input_file)

        self.events_narc = ndspy.narc.NARC(rom.getFileByName('/a/1/2/6'))
        self.maps_narc = ndspy.narc.NARC(rom.getFileByName('/a/0/0/8'))
        self.matrix_narc = ndspy.narc.NARC(rom.getFileByName('/a/0/0/9'))
        self.scripts_narc = ndspy.narc.NARC(rom.getFileByName('/a/0/5/6'))
        # self.text_narc = ndspy.narc.NARC(rom.getFileByName('/a/0/2/7'))  # todo change
        self.headers_narc = ndspy.narc.NARC(rom.getFileByName('/a/0/1/2'))

        self.write_header_permission_changes()

        maps = []

        # fills list of event files to be used for writing changes
        for x in range(len(self.events_narc.files)):
            self.events.append(Overworlds(Buffer(self.events_narc.files[x])))

        # fills list of game maps to be used to fix escalator and stair warps
        i = 0
        for x in range(len(self.maps_narc.files)):
            maps.append(Map(Buffer(self.maps_narc.files[x]), i))
            i += 1

        # fixes escalator and stair warps to not spit you out into walls or crash the game
        # for map_id in range(len(maps)):
        #     for row in range(32):
        #         for col in range(32):
        #             perm = maps[map_id].get_permissions(row, col)
        #             if perm == 0x6A or perm == 0x6B or perm == 0x5E or perm == 0x5F or perm == 0x3C or perm == 0x3D or \
        #                     perm == 0x3E:
        #                 maps[map_id].permissions[row][col] = 0x69
        #     self.maps_narc.files[map_id] = maps[map_id].write()

        # self.resolve_corner_warps(maps)

        self.overwrite_other_data(map_warps)

        # applies warp changes
        self.write_map_updates_to_binary_file(map_warps)

        # applies season locking
        rom.arm9 = self.apply_season(ndspy.codeCompression.decompress(rom.arm9))

        # writes warp changes to internal rom
        for event_id in range(len(self.events)):
            self.events_narc.files[event_id] = self.events[event_id].write()

        # writes all changes to file
        rom.setFileByName('/a/0/1/2', self.headers_narc.save())
        rom.setFileByName('/a/1/2/6', self.events_narc.save())
        rom.setFileByName('/a/0/0/8', self.maps_narc.save())
        rom.setFileByName('/a/0/0/9', self.matrix_narc.save())
        rom.setFileByName('/a/0/5/6', self.scripts_narc.save())
        # rom.setFileByName('/a/0/2/7', self.text_narc.save())
        rom.saveToFile(output_file)
        print('Rom write success')
