"""
JohtoFileDataGenerator.py

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
import concurrent.futures
import json
import os
import pickle
import threading
from time import sleep
import time
import re

from more_itertools import grouper

from RandomizerUtils import Utils
from nds.buffer import Buffer
from nds.gen4 import PlatinumWarpMapInfo
from nds.gen4.formats import Map, Matrix, Events
import ndspy.rom
import ndspy.narc
# from Dijkstra import Dijkstra


# this method is used to create a resource JSON for HGSS.


def write_json(headers_by_area_data, headers, matrices, events, names, rom):
    # for row in range(1024):
    #     whole_matrix_print.append([])
    #     for col in range(32):
    #         whole_matrix_print[row].append('0' * 32)

    # with open('../../../Resources/gen4/PlatinumMapResources.json') as f:
    #     existing_json = json.load(f)
    #
    # with open('../test.json') as f:
    #     unmodified_json = json.load(f)

    # new_names = []
    # new_to_old_dict = dict()
    # for map_instance in existing_json:
    #     new_names.append(map_instance)
    # new_names_idx = 0
    # for map_instance in unmodified_json:
    #     new_to_old_dict[map_instance] = new_names[new_names_idx]
    #     new_names_idx += 1

    new_output = dict()
    for matrix_num in range(len(matrices)):  # iterates through each matrix
        for area_data_num in range(len(headers_by_area_data[matrix_num])):  # iterates through each
            area_data = headers_by_area_data[matrix_num][area_data_num]  # area_data is a list of int values representing header IDs
            for header_num in area_data:
                if headers[header_num].event_id != 0:  # checks that the header has an event file assigned to it
                    name = create_map_name(headers[header_num], names)
                    warps = events[headers[header_num].event_id].warps
                    connections = find_connecting_maps(matrices, headers[header_num], headers, names)
                    if warps != [] or connections != []:
                        new_output[name] = {"warps": warps, "connections": connections}
                        for idx in range(len(new_output[name]['warps'])):
                            new_output[name]['warps'][idx]['header_id'] = header_num

    for map_instance in new_output:
        warps = new_output[map_instance]['warps']
        idx = 0
        for warp in warps:
            header_num = warp['dest_header']
            try:
                target_map_name = create_map_name(headers[header_num], names)
                warp['dest_map_id'] = target_map_name
            except:
                warp['dest_map_id'] = 'Map_Elevator_Destination_Dummy'
            warps[idx] = warp
            idx += 1

        new_output[map_instance]['warps'] = warps

    # for row in whole_matrix_print:
    #     for map in row:
    #         print(map, end='')
    #     print()

    # with open('test_output.json', 'w') as outfile:
    #     json.dump(existing_json, outfile, indent=2)

    # DON'T UNCOMMENT THESE LINES UNLESS YOU WANT TO REVERT THE CLEAN NAMES
    # with open('test_output_hgss.json', 'w') as outfile:
    #     json.dump(new_output, outfile, indent=2)


def create_map_name(header, names):
    with open('hgss_locations.txt') as f:
        text = f.readlines()

    header_name = names[header.id]
    ret = 'Map_'
    base_name = text[header.location_name].split()
    for idx in range(len(base_name)):
        ret += base_name[idx]
        if idx != len(base_name) - 1:
            ret += '_'

    general_area = re.compile('[RWTCPD]\d\d').match(header_name) is not None
    if general_area:
        if len(header_name) == 3:
            return ret
        else:
            ret += '_'
            sub_name = header_name[3:]
            building = re.compile('R').match(sub_name) is not None
            center = re.compile('PC').match(sub_name) is not None
            mart = re.compile('FS').match(sub_name) is not None
            corner = re.compile('SP').match(sub_name) is not None
            gym = re.compile('GYM').match(sub_name) is not None

            if building:
                building_idx = int(sub_name[1:3]) - 1
                ret += 'Room'
                if building_idx <= 9:
                    ret += '0%i_' % building_idx
                else:
                    ret += str(building_idx) + '_'

                floor_idx = int(sub_name[3:]) - 1
                if floor_idx <= 9:
                    ret += '0%i' % floor_idx
                else:
                    ret += str(floor_idx)

            elif center:
                building_idx = int(sub_name[2:4]) - 1
                ret += 'PokemonCenter'
                if building_idx <= 9:
                    ret += '0%i_' % building_idx
                else:
                    ret += str(building_idx) + '_'

                floor_idx = int(sub_name[4:]) - 1
                if floor_idx <= 9:
                    ret += '0%i' % floor_idx
                else:
                    ret += str(floor_idx)

            elif mart:
                building_idx = int(sub_name[2:4]) - 1
                ret += 'Mart'
                if building_idx <= 9:
                    ret += '0%i_' % building_idx
                else:
                    ret += str(building_idx) + '_'

                floor_idx = int(sub_name[4:]) - 1
                if floor_idx <= 9:
                    ret += '0%i' % floor_idx
                else:
                    ret += str(floor_idx)

            elif corner:
                building_idx = int(sub_name[2:4]) - 1
                ret += 'Special'
                if building_idx <= 9:
                    ret += '0%i_' % building_idx
                else:
                    ret += str(building_idx) + '_'

                floor_idx = int(sub_name[4:]) - 1
                if floor_idx <= 9:
                    ret += '0%i' % floor_idx
                else:
                    ret += str(floor_idx)

            elif gym:
                ret += 'Gym_'

                floor_idx = int(sub_name[5:]) - 1
                if floor_idx <= 9:
                    ret += '0%i' % floor_idx
                else:
                    ret += str(floor_idx)

            return ret
    else:
        safari = re.compile('SAF').match(header_name) is not None
        if safari:
            ret += 'SafariZone_'
            idx = int(header_name[3:])
            if idx <= 9:
                ret += '0%i' % idx
            else:
                ret += str(idx)

            return ret
        else:
            return ret


def find_connecting_maps(matrices, header, headers, names):
    if header.matrix_id != 0:
        return []
    else:
        adjacent = set()
        matrix = matrices[header.matrix_id]
        origin_maps = matrix.get_maps_by_header(header.id)
        for coord_tuple in origin_maps:
            connected = matrix.get_connected_headers(coord_tuple[1], coord_tuple[0], headers, header.id)
            for entry in connected:
                adjacent.add(entry)

        if header.id in adjacent:
            adjacent.remove(header.id)

        ret = []
        for entry in adjacent:
            ret.append(create_map_name(headers[entry], names))

        return ret

