"""
White2FileDataGenerator.py

Function(s) to generate a resource json to be used to map White 2's world

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
from nds.gen5.FormatsGen5 import *
import ndspy.rom
import ndspy.narc


# this method is used to create a resource JSON for B2W2.

used_names = set()
repaired_names = set()

def write_json(headers_by_area_data, headers, matrices, events, rom):
    new_output = dict()
    for matrix_num in range(len(matrices)):  # iterates through each matrix
        for area_data_num in range(len(headers_by_area_data[matrix_num])):  # iterates through each
            area_data = headers_by_area_data[matrix_num][area_data_num]  # area_data is a list of int values representing header IDs
            for header_num in area_data:
                if headers[header_num].event_id != 0:  # checks that the header has an event file assigned to it
                    name = create_map_name(headers[header_num], headers)
                    if name in used_names:
                        other_header = new_output[name]['warps'][0]['header_id']
                        new_output[name + '_h' + str(other_header)] = new_output[name]
                        new_output.pop(name)
                        repaired_names.add(name)
                        name += '_h' + str(header_num)
                    used_names.add(name)
                    warps = events[headers[header_num].event_id].warps
                    connections = find_connecting_maps(matrices, headers[header_num], headers)
                    if warps != [] or connections != []:
                        new_output[name] = {"warps": warps, "connections": connections}
                        for idx in range(len(new_output[name]['warps'])):
                            new_output[name]['warps'][idx]['header_id'] = header_num

    for map_instance in new_output:
        print(map_instance)
        warps = new_output[map_instance]['warps']
        idx = 0
        for warp in warps:
            header_num = warp['dest_header']
            try:
                target_map_name = create_map_name(headers[header_num], headers, True)
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
    with open('test_output_w2.json', 'w') as outfile:
        json.dump(new_output, outfile, indent=2)


def create_map_name(header, headers, destination=False):
    text = []
    with open('w2 locations.txt') as f:
        for line in f.readlines():
            text.append(line.replace('\n', ''))

    name = 'Map_' + text[header.name_idx & 0x3FF].replace(' ', '_')
    if header.matrix_id == 0:
        pass
    elif header.matrix_id == 13:
        name += '_Center00'
    elif header.id == 29 or header.id == 63 or header.id == 98 or header.id == 108 or header.id == 121 or header.id == 473 or header.id == 489 or header.id == 502:
        name += '_Gym00'
    elif headers[header.parent_header_id].matrix_id == 0 and 'Gate' not in name:
        name += '_Interior_h' + str(header.id)
    else:
        name += '_h' + str(header.id)

    if destination and name in repaired_names:
        name += '_h' + str(header.id)

    return name



def find_connecting_maps(matrices, header, headers):
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
            ret.append(create_map_name(headers[entry], headers, True))

        return ret


def fix_json(headers_by_area_data, headers, matrices, events, rom):
    # with open('../../../Resources/gen5/White2MapResources.json') as infile:
    #     data = json.load(infile)
    with open('test_output_w2.json') as infile:
        data = json.load(infile)

    for map_instance in data:
        print(map_instance)
        warps = data[map_instance]['warps']
        idx = 0
        for warp in warps:
            event = events[headers[warp['header_id']].event_id]
            warp['height'] = event.warps[idx].height
            warp['width'] = event.warps[idx].width
            warp['x_pos'] = event.warps[idx].local_x_pos
            warp['y_pos'] = event.warps[idx].local_y_pos
            warp['map_x'] = event.warps[idx].map_x_pos
            warp['map_y'] = event.warps[idx].map_y_pos
            warp['is_rail'] = event.warps[idx].is_rail
            warps[idx] = warp
            idx += 1

        data[map_instance]['warps'] = warps

    # for row in whole_matrix_print:
    #     for map in row:
    #         print(map, end='')
    #     print()

    # with open('test_output.json', 'w') as outfile:
    #     json.dump(existing_json, outfile, indent=2)

    # DON'T UNCOMMENT THESE LINES UNLESS YOU WANT TO REVERT THE CLEAN NAMES
    with open('test_output_w2.json', 'w') as outfile:
        json.dump(data, outfile, indent=2)