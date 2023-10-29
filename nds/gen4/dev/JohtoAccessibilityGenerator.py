"""
JohtoAccessibilityGenerator.py

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

from more_itertools import grouper

from RandomizerUtils import Utils
from nds.buffer import Buffer
from nds.gen4 import JohtoWarpMapInfo
from nds.gen4.formats import Map, Matrix, Events
import ndspy.rom
import ndspy.narc
from Dijkstra import Dijkstra
from nds.tableLocator import TableLocator


class CompositeMap:
    def __init__(self, map_entry):
        self.header_id = map_entry[0]['header_id']
        self.matrix_id = headers[self.header_id].matrix_id
        matrix = matrices[self.matrix_id]

        self.map_locations = matrix.get_maps_by_header(self.header_id)
        smallest_x = 255
        largest_x = 0
        smallest_y = 255
        largest_y = 0
        self.map_objects = dict()
        for coord_tuple in self.map_locations:
            if coord_tuple[0] < smallest_x:
                smallest_x = coord_tuple[0]
            if coord_tuple[0] > largest_x:
                largest_x = coord_tuple[0]

            if coord_tuple[1] < smallest_y:
                smallest_y = coord_tuple[1]
            if coord_tuple[1] > largest_y:
                largest_y = coord_tuple[1]
            map_id = matrix.get_map(coord_tuple[1], coord_tuple[0])
            self.map_objects[coord_tuple] = Map(Buffer(maps_narc.files[map_id]), map_id, '', hgss=True)

        self.height = largest_y - smallest_y + 1
        self.width = largest_x - smallest_x + 1

        self.map_layout = []
        self.true_positions = []
        self.inverted_positions = dict()
        for row in range(self.height):
            self.map_layout.append([])
            self.true_positions.append([])
            for col in range(self.width):
                self.map_layout[row].append(None)
                self.true_positions[row].append(None)

        for coord_tuple in self.map_locations:
            self.map_layout[coord_tuple[1] - smallest_y][coord_tuple[0] - smallest_x] = self.map_objects[coord_tuple]
            self.true_positions[coord_tuple[1] - smallest_y][coord_tuple[0] - smallest_x] = coord_tuple
            self.inverted_positions[coord_tuple] = (coord_tuple[1] - smallest_y, coord_tuple[0] - smallest_x)

        self.permissions = []
        self.collisions = []

        for row in range(32 * self.height):
            self.permissions.append([])
            self.collisions.append([])
            for col in range(32 * self.width):
                self.permissions[row].append(0)
                self.collisions[row].append(0x80)

        for matrix_row in range(len(self.map_layout)):
            for matrix_col in range(len(self.map_layout[matrix_row])):
                for row in range(32):
                    for col in range(32):
                        self.permissions[matrix_row * 32 + row][matrix_col * 32 + col] = self.map_layout[matrix_row][
                            matrix_col].get_permissions(row, col)
                        self.collisions[matrix_row * 32 + row][matrix_col * 32 + col] = self.map_layout[matrix_row][
                            matrix_col].get_collisions(row, col)

        # for row in self.permissions:
        #     print(row)

    def get_permissions(self, row, col):
        return self.permissions[row][col]

    def get_collisions(self, row, col):
        return self.collisions[row][col]

    def get_map_pos(self, row, col):
        return self.inverted_positions[(col, row)]


permission_obstructions_dict = {  # TODO adjust for HG
    'surf': [0x10, 0x15],
    'waterfall': [0x13],
    'cliffs': [0x38, 0x39, 0x3A, 0x3B, 0x3F],
    'whirlpool': [0x11]
}
collision_obstructions = [0x80]
permission_warps = [0x5E, 0x5F, 0x62, 0x63, 0x64, 0x65, 0x67, 0x69, 0x6C, 0x6D, 0x6E, 0x6F]
overworld_script_obstructions = [10000, 10001, 10002]  # TODO adjust for HG

whole_matrix_print = []


def dijkstra(map_entry, map_name, bool_list):  # runs dijkstra on grouped 32x32 map chunks
    access_list = dict()
    if map_name == 'Map_Safari_Zone_Room00_01':
        return None
    if len(map_entry) != 0:
        composite_map = CompositeMap(map_entry)
        header = composite_map.header_id
        event = events[headers[header].event_id]

        nodes, edges, edge_types = djikstra_node_init(composite_map, event, bool_list)

        path_finder = Dijkstra(nodes, edges)
        # print(map_name + ': ')
        for start_num in range(len(map_entry)):
            start_map = composite_map.get_map_pos(int(map_entry[start_num]['map_y']), map_entry[start_num]['map_x'])
            start_warp = str(32 * start_map[0] + int(map_entry[start_num]['y_pos'])) + ':' + str(
                32 * start_map[1] + int(map_entry[start_num]['x_pos']))
            this_warp_access = []
            for end_num in range(len(map_entry)):
                end_map = composite_map.get_map_pos(int(map_entry[end_num]['map_y']), map_entry[end_num]['map_x'])
                end_warp = str(32 * end_map[0] + int(map_entry[end_num]['y_pos'])) + ':' + str(
                    32 * end_map[1] + int(map_entry[end_num]['x_pos']))
                if start_warp != end_warp:
                    p, v = path_finder.find_route(start_warp, end_warp)
                    se = path_finder.generate_path(p, start_warp, end_warp)
                    if se is not None:
                        requirements = []
                        for warp in range(len(se) - 1):
                            if edge_types[se[warp]][se[warp + 1]] != 'walk' and edge_types[se[warp]][se[warp + 1]] != \
                                    'bound' and edge_types[se[warp]][se[warp + 1]] != 'warp' and \
                                    edge_types[se[warp]][se[warp + 1]] != 'ledge':
                                requirements.append(edge_types[se[warp]][se[warp + 1]])
                        if not requirements:
                            # print("\tPath from w%s to w%s exists" % (start_num, end_num))
                            this_warp_access.append((end_num, 0))
                        else:
                            # print("\tPath from w%s to w%s exists with requirements %s" % (start_num, end_num, str(set(requirements))))
                            this_warp_access.append((end_num, list(set(requirements))))
                    else:
                        # print("\tNo path from w%s to w%s exists" % (start_num, end_num))
                        pass
            access_list[start_num] = this_warp_access
            # print()
    if access_list != {}:
        return access_list
    else:
        return None


def djikstra_node_init(composite_map, event,
                       bool_list):  # creates a node at each tile on the 32x32 map grid, and creates edges between all traversable node boundaries
    nodes = []
    edges = dict()
    edge_types = dict()
    for row in range(32 * composite_map.height):
        for col in range(32 * composite_map.width):
            map_row = composite_map.true_positions[int(row / 32)][int(col / 32)][1]
            map_col = composite_map.true_positions[int(row / 32)][int(col / 32)][0]
            name = str(row) + ':' + str(col)
            nodes.append(name)
            edges[name] = dict()
            edge_types[name] = dict()
            obstructions = check_obstructed(composite_map, row + 1, col, row, col, event, map_row, map_col, bool_list)
            if obstructions[0]:
                edges[name][str(row + 1) + ':' + str(col)] = 1
                edge_types[name][str(row + 1) + ':' + str(col)] = obstructions[1]

            obstructions = check_obstructed(composite_map, row, col + 1, row, col, event, map_row, map_col, bool_list)
            if obstructions[0]:
                edges[name][str(row) + ':' + str(col + 1)] = 1
                edge_types[name][str(row) + ':' + str(col + 1)] = obstructions[1]

            obstructions = check_obstructed(composite_map, row - 1, col, row, col, event, map_row, map_col, bool_list)
            if obstructions[0]:
                edges[name][str(row - 1) + ':' + str(col)] = 1
                edge_types[name][str(row - 1) + ':' + str(col)] = obstructions[1]

            obstructions = check_obstructed(composite_map, row, col - 1, row, col, event, map_row, map_col, bool_list)
            if obstructions[0]:
                edges[name][str(row) + ':' + str(col - 1)] = 1
                edge_types[name][str(row) + ':' + str(col - 1)] = obstructions[1]
    return nodes, edges, edge_types


def check_obstructed(composite_map, row, col, origin_row, origin_col, event, map_row, map_col,
                     bool_list):  # checks to see if an edge between two nodes exists or not
    if 32 * composite_map.height > row >= 0 and 32 * composite_map.width > col >= 0:
        perm_type = composite_map.get_permissions(row, col)
        coll_type = composite_map.get_collisions(row, col)

        if perm_type in permission_warps:
            return True, 'warp'

        for overworld in event.overworlds:
            if overworld.local_x_pos == col % 32 and overworld.local_y_pos == row % 32 and overworld.map_y_pos == map_row and overworld.map_x_pos == map_col:
                if overworld.script == 10001:
                    return bool_list[0], JohtoWarpMapInfo.ROCKSMASH_FLAG
                elif overworld.script == 10000:
                    return bool_list[1], JohtoWarpMapInfo.CUT_FLAG
                elif overworld.script == 10002 or overworld.ow_id == 381:  # the extra check is for the spray pail
                    return bool_list[2], JohtoWarpMapInfo.STRENGTH_FLAG

        for permission_obstruction_type in permission_obstructions_dict.keys():
            if permission_obstructions_dict[permission_obstruction_type].__contains__(perm_type):
                if permission_obstruction_type == 'cliffs':
                    if perm_type == 0x38 and origin_col < col:  # origin col is further left than current col (jump left to right)
                        return True, 'ledge'
                    if perm_type == 0x39 and col < origin_col:  # origin col is further right than current col (jump right to left)
                        return True, 'ledge'
                    if perm_type == 0x3a and row < origin_row:  # origin row is further down than current row (jump down to up)
                        return True, 'ledge'
                    if perm_type == 0x3b and origin_row < row:  # origin row is further up than current row (jump up to down)
                        return True, 'ledge'
                    else:
                        return False, 'ledge'
                elif permission_obstruction_type == 'surf':
                    return bool_list[3], JohtoWarpMapInfo.SURF_FLAG
                elif permission_obstruction_type == 'whirlpool':
                    return bool_list[4], JohtoWarpMapInfo.WHIRLPOOL_FLAG

        if coll_type == 0x80:
            return False, 'wall'

        return True, 'walk'
    return False, 'bounds'


def calculate_warp_accessibility(bool_list):
    map_warp_accessibility = dict()
    for map_name in resource_json:
        accessibility = dijkstra(resource_json[map_name]['warps'], map_name, bool_list)
        print('\t\tCompleted subtask for %s' % map_name)
        if accessibility is not None and len(accessibility) > 1:
            map_warp_accessibility[map_name] = accessibility
    return map_warp_accessibility


def list_first_slots(warp_tuples):
    ret = []
    for warp in warp_tuples:
        ret.append(warp[0])
    return ret


def num_flags(bool_list):
    ret = 0
    for b in bool_list:
        if b:
            ret += 1
    return ret


def run_calculations_2():
    options = [False, True]

    bool_lists = dict()

    current = 0

    for b1 in options:
        for b2 in options:
            for b3 in options:
                for b4 in options:
                    for b5 in options:
                        bool_lists[current] = [b1, b2, b3, b4, b5]
                        current += 1

    current = 0
    new_bool_lists = dict()
    for num in range(5):  # TODO switch this back to bool_lists length
        for idx in bool_lists:
            if num_flags(bool_lists[idx]) == num:
                new_bool_lists[current] = bool_lists[idx]
                current += 1

    executor = concurrent.futures.ProcessPoolExecutor(10)  # TODO switch this back to 10
    futures = [executor.submit(call_calculation_grouping, group, new_bool_lists)
               for group in grouper(5, new_bool_lists)]  # TODO switch this back to 5
    concurrent.futures.wait(futures)

    results = dict()

    for future in futures:
        ret = future.result()
        for entry in ret:
            results[entry] = ret[entry]

    results_list = []
    for idx in range(len(results)):
        results_list.append(results[idx])

    final_result = dict()
    maximum_passage = results_list[0]
    for entry in maximum_passage:
        final_result[entry] = maximum_passage[entry]
        for sub_list in results_list[1:]:
            if entry in sub_list:
                for warp_num in sub_list[entry]:
                    for connections in sub_list[entry][warp_num]:
                        first_slots = list_first_slots(final_result[entry][warp_num])
                        if connections[0] not in first_slots:
                            final_result[entry][warp_num].append(connections)
                            print('break')

    with open('../warp_accessibility_output_hg', 'wb') as out_file:
        pickle.dump(final_result, out_file)

    return final_result


def call_calculation_grouping(items, bool_lists):
    ret = dict()
    print('Starting range from %s to %s' % (items[0], items[len(items) - 1]))
    # print(bool_lists)
    for item in items:
        if item is not None:
            if true_xor(bool_lists[item][1], bool_lists[item][4]):
                try:
                    start_time = round(time.time() * 1000)
                    print('\tStarting process %i on set %s' % (item, bool_lists[item]))
                    ret[item] = calculate_warp_accessibility(bool_lists[item])
                    end_time = round(time.time() * 1000)
                    time_len = end_time - start_time
                    print('\t\tProcess %i ended after %i milliseconds (%i seconds)' % (item, time_len, time_len / 1000))
                except:
                    print('\t\terror with item %i: %s' % (item, bool_lists[item]))
            else:
                ret[item] = dict()
    return ret


def flag_list_to_num(requirements):
    num = 0
    for flag in requirements:
        num |= (1 << flag)
    return num


def true_xor(*args):
    return sum(args) == 1 or sum(args) == 0


rom = ndspy.rom.NintendoDSRom.fromFile('../HeartGold.nds')
maps_narc = ndspy.narc.NARC(rom.getFileByName('/a/0/6/5'))
events_narc = ndspy.narc.NARC(rom.getFileByName('/a/0/3/2'))
matrix_narc = ndspy.narc.NARC(rom.getFileByName('/a/0/4/1'))

locator = TableLocator(rom)
headers = locator.get_table('mapHeaders')

matrices = []

for matrix_num in range(len(matrix_narc.files)):
    matrices.append(Matrix(Buffer(matrix_narc.files[matrix_num])))

events = []
for x in range(len(events_narc.files)):
    events.append(Events(Buffer(events_narc.files[x])))

with open(Utils.resource_path(os.path.join('Resources', 'gen4', 'JohtoMapResources.json'))) as f:
    resource_json = json.load(f)

if __name__ == '__main__':
    result = run_calculations_2()
    # accessibility = dijkstra(resource_json['Map_Safari_Zone_Room00_01']['warps'], 'Map_Safari_Zone_Room00_01', [True, True, True, True, True])
    converted_value = 0

    for map_name in result:
        if len(result[map_name]) > 1:
            print('\'%s\': {' % map_name)
            for warp in result[map_name]:
                if len(result[map_name][warp]) > 1:
                    print('\t%s: [' % warp, end='')
                    for connection in result[map_name][warp]:
                        if connection != result[map_name][warp][len(result[map_name][warp]) - 1]:
                            if isinstance(connection[1], list):
                                converted_value = flag_list_to_num(connection[1])
                            else:
                                converted_value = connection[1]
                            print('WT(%s, %s)' % (connection[0], converted_value), end=', ')
                        else:
                            if isinstance(connection[1], list):
                                converted_value = flag_list_to_num(connection[1])
                            else:
                                converted_value = connection[1]
                            print('WT(%s, %s)' % (connection[0], converted_value), end='],\n')
            print('},')
    print('Created list with %i entries' % len(result))
    # \'.+\': \{\n    \},