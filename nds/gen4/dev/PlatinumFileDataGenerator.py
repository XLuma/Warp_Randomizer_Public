"""
PlatinumFileDataGenerator.py

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
from nds.gen4 import PlatinumWarpMapInfo
from nds.gen4.formats import Map, Matrix, Events
import ndspy.rom
import ndspy.narc
from Dijkstra import Dijkstra
from nds.tableLocator import TableLocator


# this method is used to create a resource JSON for Platinum.


def write_json(headers_by_area_data, headers, matrices, events, rom):
    for row in range(1024):
        whole_matrix_print.append([])
        for col in range(32):
            whole_matrix_print[row].append('0' * 32)

    with open('../../../Resources/gen4/PlatinumMapResources.json') as f:
        existing_json = json.load(f)

    with open('../test.json') as f:
        unmodified_json = json.load(f)

    new_names = []
    new_to_old_dict = dict()
    for map_instance in existing_json:
        new_names.append(map_instance)
    new_names_idx = 0
    for map_instance in unmodified_json:
        new_to_old_dict[map_instance] = new_names[new_names_idx]
        new_names_idx += 1

    new_output = dict()
    for matrix_num in range(len(matrices)):
        for area_data_num in range(len(headers_by_area_data[matrix_num])):
            area_data = headers_by_area_data[matrix_num][area_data_num]
            for header_num in area_data:
                output = matrices[matrix_num].get_maps_by_header(header_num)
                warps_by_map = sort_warps_by_map(headers[header_num], events)
                if output:
                    for coord_tuple in output:
                        name = 'm' + str(matrix_num) + ':ad' + str(area_data_num) + ':h' + str(header_num) + ':x' + str(
                            coord_tuple[0]) + ':y' + str(coord_tuple[1])
                        if warps_by_map.keys().__contains__(coord_tuple):
                            # print(name + ' -> ' + str(warps_by_map[coord_tuple]))
                            new_output[name] = {"warps": warps_by_map[coord_tuple],
                                                "connections": matrices[matrix_num].get_connected_maps(coord_tuple[1],
                                                                                                       coord_tuple[0],
                                                                                                       headers,
                                                                                                       header_num)}
                            # print(str(existing_json[new_to_old_dict[name]]))
                            # calculate_warp_accessibility(header_num, headers, matrix_num, matrices, events, coord_tuple,
                            #                              name, rom)
                        elif matrices[matrix_num].headers:
                            if matrices[matrix_num].get_header(coord_tuple[1], coord_tuple[0]) != 65535 and matrices[
                                matrix_num].get_header(coord_tuple[1], coord_tuple[0]) != 0 and matrices[
                                matrix_num].get_map(coord_tuple[1], coord_tuple[0]) != 0:
                                # print(name)
                                new_output[name] = {"warps": [],
                                                    "connections": matrices[matrix_num].get_connected_maps(
                                                        coord_tuple[1],
                                                        coord_tuple[0],
                                                        headers,
                                                        header_num)}
                                # calculate_warp_accessibility(header_num, headers, matrix_num, matrices, events,
                                #                              coord_tuple,
                                #                              name, rom)

    # for map_instance in new_to_old_dict:
    #     print()
    #     warps = existing_json[new_to_old_dict[map_instance]]['warps']
    #     idx = 0
    #     for warp in warps:
    #         print(new_to_old_dict[map_instance] + ': ' + str(warp))
    #         header_num = warp['dest_header']
    #         dest_warp_id = warp['dest_warp_id']
    #         try:
    #             matrix_num = headers[header_num].matrix_id
    #             area_data_num = headers[header_num].area_data_id
    #             events_num = headers[header_num].event_id
    #             map_x = events[events_num].warps[dest_warp_id].map_x_pos
    #             map_y = events[events_num].warps[dest_warp_id].map_y_pos
    #             target_map_name = 'm' + str(matrix_num) + ':ad' + str(area_data_num) + ':h' + str(header_num) + ':x' \
    #                               + str(map_x) + ':y' + str(map_y)
    #             if target_map_name in new_to_old_dict:
    #                 warp['dest_map_id'] = new_to_old_dict[target_map_name]
    #             else:
    #                 warp['dest_map_id'] = target_map_name
    #         except:
    #             warp['dest_map_id'] = 'Map_Elevator_Destination_Dummy'
    #         warps[idx] = warp
    #         idx += 1
    #         print('\t' + str(warp))
    #
    #     existing_json[new_to_old_dict[map_instance]]['warps'] = warps

    underscore_fix_dict = dict()
    for map_instance in existing_json:
        print()
        warps = existing_json[map_instance]['warps']
        for warp_num in range(len(warps)):
            print(map_instance + ': ' + str(warps[warp_num]))
            warps[warp_num]['dest_map_id'] = warps[warp_num]['dest_map_id'].replace(":", "_")
        existing_json[map_instance]['warps'] = warps

    for map_instance in existing_json:
        underscore_fix_dict[map_instance.replace(":", "_")] = existing_json[map_instance]

    # for row in whole_matrix_print:
    #     for map in row:
    #         print(map, end='')
    #     print()

    # For the love of all that is good in Sinnoh DON'T UNCOMMENT THESE LINES UNLESS YOU WANT TO REVERT THE CLEAN NAMES
    # with open('../../Resources/gen4/PlatinumMapResources.json', 'w') as outfile:
    #     json.dump(new_output, outfile, indent=2)

    # with open('test_output.json', 'w') as outfile:
    #     json.dump(existing_json, outfile, indent=2)

    with open('../test_output_2.json', 'w') as outfile:
        json.dump(underscore_fix_dict, outfile, indent=2)


def sort_warps_by_map(header, events):
    warps = dict()
    for warp in events[header.event_id].warps:
        warp['header_id'] = header.id
        map_pos_tuple = (warp.map_x_pos, warp.map_y_pos)
        if warps.keys().__contains__(map_pos_tuple):
            warp_list = warps.get(map_pos_tuple)
            warp_list.append(warp)
            warps[map_pos_tuple] = warp_list
        else:
            warps[map_pos_tuple] = [warp]

    return warps


# this is a new section in the file

class DijkstraThread(threading.Thread):
    def __init__(self, thread_id, name, boolean_list):
        threading.Thread.__init__(self)
        self.thread_id = thread_id
        self.name = name
        self.boolean_list = boolean_list
        self.local_result = None

    def run(self):
        print('Starting %i for %s: ' % (self.thread_id, str(self.boolean_list)))
        self.local_result = calculate_warp_accessibility(self.boolean_list)
        print('Exiting %i' % self.thread_id)


permission_obstructions_dict = {
    'surf': [0x10, 0x15],
    'waterfall': [0x13],
    'cliffs': [0x38, 0x39, 0x3A, 0x3B, 0x3F],
    'rock_climb': [0x4B, 0x4C],
    # 'bike_passable': [0x76, 0x79, 0x7A, 0x7C, 0x7D, 0xD8],
    'bike_no_pass': [0xD9, 0xDA]
}
collision_obstructions = [0x80]
permission_warps = [0x5E, 0x5F, 0x62, 0x63, 0x64, 0x65, 0x67, 0x69, 0x6C, 0x6D, 0x6E, 0x6F]
overworld_script_obstructions = [10000, 10001, 10002]

whole_matrix_print = []


def dijkstra(map_entry, map_name, bool_list):
    access_list = dict()
    if len(map_entry) != 0:
        header = map_entry[0]['header_id']
        matrix = matrices[headers[header].matrix_id]
        map_x = map_entry[0]['map_x']
        map_y = map_entry[0]['map_y']
        event = events[headers[header].event_id]

        this_map = matrix.get_map(map_y, map_x)
        map_data = Map(Buffer(maps_narc.files[this_map]), this_map, '')
        nodes, edges, edge_types = djikstra_node_init(map_data, event, map_y, map_x, bool_list)

        path_finder = Dijkstra(nodes, edges)
        # print(map_name + ': ')
        for start_num in range(len(map_entry)):
            start_warp = str(map_entry[start_num]['y_pos']) + ':' + str(map_entry[start_num]['x_pos'])
            this_warp_access = []
            for end_num in range(len(map_entry)):
                end_warp = str(map_entry[end_num]['y_pos']) + ':' + str(map_entry[end_num]['x_pos'])
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
                            this_warp_access.append((end_num, set(requirements)))
                    else:
                        # print("\tNo path from w%s to w%s exists" % (start_num, end_num))
                        pass
            access_list[start_num] = this_warp_access
            # print()
    if access_list != {}:
        return access_list
    else:
        return None


def djikstra_node_init(map_data, event, map_row, map_col, bool_list):
    nodes = []
    edges = dict()
    edge_types = dict()
    for row in range(32):
        for col in range(32):
            name = str(row) + ':' + str(col)
            nodes.append(name)
            edges[name] = dict()
            edge_types[name] = dict()
            obstructions = check_obstructed(map_data, row + 1, col, row, col, event, map_row, map_col, bool_list)
            if obstructions[0]:
                edges[name][str(row + 1) + ':' + str(col)] = 1
                edge_types[name][str(row + 1) + ':' + str(col)] = obstructions[1]

            obstructions = check_obstructed(map_data, row, col + 1, row, col, event, map_row, map_col, bool_list)
            if obstructions[0]:
                edges[name][str(row) + ':' + str(col + 1)] = 1
                edge_types[name][str(row) + ':' + str(col + 1)] = obstructions[1]

            obstructions = check_obstructed(map_data, row - 1, col, row, col, event, map_row, map_col, bool_list)
            if obstructions[0]:
                edges[name][str(row - 1) + ':' + str(col)] = 1
                edge_types[name][str(row - 1) + ':' + str(col)] = obstructions[1]

            obstructions = check_obstructed(map_data, row, col - 1, row, col, event, map_row, map_col, bool_list)
            if obstructions[0]:
                edges[name][str(row) + ':' + str(col - 1)] = 1
                edge_types[name][str(row) + ':' + str(col - 1)] = obstructions[1]
    return nodes, edges, edge_types


def check_obstructed(map_data, row, col, origin_row, origin_col, event, map_row, map_col, bool_list):
    if 32 > row >= 0 and 32 > col >= 0:
        perm_type = map_data.get_permissions(row, col)
        coll_type = map_data.get_collisions(row, col)

        if perm_type in permission_warps:
            return True, 'warp'

        for permission_obstruction_type in permission_obstructions_dict.keys():
            if permission_obstructions_dict[permission_obstruction_type].__contains__(perm_type):
                if permission_obstruction_type == 'cliffs':
                    if perm_type == 0x38 and origin_col > col:
                        return True, 'ledge'
                    if perm_type == 0x39 and col > origin_col:
                        return True, 'ledge'
                    if perm_type == 0x3a and row < origin_row:
                        return True, 'ledge'
                    if perm_type == 0x3b and origin_row < row:
                        return True, 'ledge'
                    else:
                        return False, 'ledge'
                elif permission_obstruction_type == 'surf':
                    return bool_list[0], PlatinumWarpMapInfo.SURF_FLAG
                # elif permission_obstruction_type == 'waterfall':
                #     return bool_list[1], 'waterfall'
                elif permission_obstruction_type == 'rock_climb':
                    return bool_list[1], PlatinumWarpMapInfo.ROCKCLIMB_FLAG
                # elif permission_obstruction_type == 'bike_passable':
                #     return bool_list[4], 'bike_walk'
                elif permission_obstruction_type == 'bike_no_pass':
                    return bool_list[2], PlatinumWarpMapInfo.BIKE_FLAG

            for overworld in event.overworlds:
                if overworld.local_x_pos == col and overworld.local_y_pos == row and overworld.map_y_pos == map_row and overworld.map_x_pos == map_col:
                    if overworld.script == 10000:
                        return bool_list[3], PlatinumWarpMapInfo.CUT_FLAG
                    elif overworld.script == 10001:
                        return bool_list[4], PlatinumWarpMapInfo.ROCKSMASH_FLAG
                    elif overworld.script == 10002:
                        return bool_list[5], PlatinumWarpMapInfo.STRENGTH_FLAG

        if coll_type == 0x80:
            return False, 'wall'

        return True, 'walk'
    return False, 'bounds'


def calculate_warp_accessibility(bool_list):
    map_warp_accessibility = dict()
    for map_name in resource_json:
        accessibility = dijkstra(resource_json[map_name]['warps'], map_name, bool_list)
        if accessibility is not None and len(accessibility) > 1:
            map_warp_accessibility[map_name] = accessibility

    # for map_name in map_warp_accessibility:
    #     if len(map_warp_accessibility[map_name]) > 1:
    #         print('%s: {' % map_name)
    #         for warp in map_warp_accessibility[map_name]:
    #             if len(map_warp_accessibility[map_name][warp]) > 1:
    #                 print('\t%s: [' % warp, end='')
    #                 for connection in map_warp_accessibility[map_name][warp]:
    #                     if connection != map_warp_accessibility[map_name][warp][len(map_warp_accessibility[map_name][warp])-1]:
    #                         print('WT(%s, %s)' % (connection[0], connection[1]), end=', ')
    #                     else:
    #                         print('WT(%s, %s)' % (connection[0], connection[1]), end='],\n')
    #         print('},')
    # print('Created list with %i entries' % len(map_warp_accessibility))
    return map_warp_accessibility


def list_first_slots(warp_tuples):
    ret = []
    for warp in warp_tuples:
        ret.append(warp[0])
    return ret


def run_warp_calculation():
    options = [True, False]

    bool_lists = []
    results = []
    active_threads = []

    for b1 in options:
        for b2 in options:
            for b3 in options:
                for b4 in options:
                    for b5 in options:
                        for b6 in options:
                            for b7 in options:
                                bool_lists.append([b1, b2, b3, b4, b5, b6, b7])

    num_lists = len(bool_lists)
    current = -1
    counter = 0
    while current != num_lists:
        counter += 1
        if len(active_threads) < 4:
            current += 1
            thread = DijkstraThread(current, "Dijkstra-" + str(current), bool_lists[current])
            thread.start()
            active_threads.append(thread)
            sleep(.25)

        for thread_num in range(len(active_threads)):
            if not active_threads[thread_num].is_alive():
                # print('%s dead' % active_threads[thread_num].name)
                results.append(active_threads[thread_num].local_result)
                active_threads[thread_num].join()
                active_threads.pop(thread_num)
                sleep(.25)
                break

    while len(active_threads) != 0:
        for thread_num in range(len(active_threads)):
            if not active_threads[thread_num].is_alive():
                results.append(active_threads[thread_num].local_result)
                active_threads[thread_num].join(0)
                active_threads.pop(thread_num)
                sleep(.25)
                break

    # results.append(calculate_warp_accessibility([False, False, False, False, False, False, False]))
    # results.append(calculate_warp_accessibility([True, False, False, False, False, False, False]))

    final_result = dict()
    maximum_passage = results[0]
    for entry in maximum_passage:
        final_result[entry] = maximum_passage[entry]
        for sub_list in results[1:]:
            if entry in sub_list:
                for warp_num in sub_list[entry]:
                    for connections in sub_list[entry][warp_num]:
                        for connection_num in range(len(connections)):
                            first_slots = list_first_slots(final_result[entry][warp_num])
                            if connections[connection_num][0] in range(len(first_slots)):
                                # final_result[entry][warp_num][]
                                pass

    # for map_num in range(len(maps_narc.files)):
    #     dijkstra(maps_narc, map_num)

    # dijkstra(maps_narc, 113)

    # for warp in events[header.event_id].warps:
    #     calculate_accessibility(warp, events[header.event_id], map_data)


def num_flags(bool_list):
    ret = 0
    for b in bool_list:
        if b:
            ret += 1
    return ret


def run_calculations_2():
    options = [False, True]

    bool_lists = dict()
    active_threads = []

    current = 0

    for b1 in options:
        for b2 in options:
            for b3 in options:
                for b4 in options:
                    for b5 in options:
                        for b6 in options:
                            for b7 in options:
                                bool_lists[current] = [b1, b2, b3, b4, b5, b6, b7]
                                current += 1

    current = 0
    new_bool_lists = dict()
    for num in range(8):  # TODO switch this back to bool_lists length
        for idx in bool_lists:
            if num_flags(bool_lists[idx]) == num:
                new_bool_lists[current] = bool_lists[idx]
                current += 1

    executor = concurrent.futures.ProcessPoolExecutor(16)  # TODO switch this back to 10
    futures = [executor.submit(call_calculation_grouping, group, new_bool_lists)
               for group in grouper(8, new_bool_lists)]  # TODO switch this back to 5
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

    with open('../warp_accessibility_output', 'wb') as out_file:
        pickle.dump(final_result, out_file)


def call_calculation_grouping(items, bool_lists):
    ret = dict()
    print('Starting range from %i to %i' % (items[0], items[len(items)-1]))
    for item in items:
        try:
            start_time = round(time.time() * 1000)
            print('\tStarting process %i on set %s' % (item, bool_lists[item]))
            ret[item] = calculate_warp_accessibility(bool_lists[item])
            end_time = round(time.time() * 1000)
            time_len = end_time - start_time
            print('\t\tProcess %i ended after %i milliseconds (%i seconds)' % (item, time_len, time_len/1000))
        except:
            print('\t\terror with item %i: %s' % (item, bool_lists[item]))
    return ret


rom = ndspy.rom.NintendoDSRom.fromFile('../Platinum.nds')
maps_narc = ndspy.narc.NARC(rom.getFileByName('fielddata/land_data/land_data.narc'))
events_narc = ndspy.narc.NARC(rom.getFileByName('/fielddata/eventdata/zone_event.narc'))
matrix_narc = ndspy.narc.NARC(rom.getFileByName('/fielddata/mapmatrix/map_matrix.narc'))

locator = TableLocator(rom)
headers = locator.get_table('mapHeaders')

matrices = []

for matrix_num in range(len(matrix_narc.files)):
    matrices.append(Matrix(Buffer(matrix_narc.files[matrix_num])))

events = []
for x in range(len(events_narc.files)):
    events.append(Events(Buffer(events_narc.files[x])))

with open(Utils.resource_path(os.path.join('Resources', 'gen4', 'PlatinumMapResources.json'))) as f:
    resource_json = json.load(f)

    # calculate_warp_accessibility()
    # run_warp_calculation()
if __name__ == '__main__':
    run_calculations_2()

# def calculate_warp_accessibility(header_num, headers, matrix_num, matrices, events, coord_tuple, name, rom):
#     header = headers[header_num]
#     matrix = matrices[matrix_num]
#     maps_narc = ndspy.narc.NARC(rom.getFileByName('fielddata/land_data/land_data.narc'))
#     map_id = matrix.get_map(coord_tuple[1], coord_tuple[0])
#     map_data = Map(Buffer(maps_narc.files[map_id]), map_id, name)
#
#     if matrix_num == 0:
#         obstructions_map = []
#         for row in range(32):
#             obstructions_map.append([])
#             row_str = ''
#             for col in range(32):
#                 obstructions_map[row].append(check_obstructed(map_data, events[header.event_id], row, col))
#                 row_str += check_obstructed(map_data, events[header.event_id], row, col)
#             whole_matrix_print[coord_tuple[1] * 32 + row][coord_tuple[0]] = row_str
#             # print()
#         # print()
#
#         for warp in events[header.event_id].warps:
#             calculate_accessibility(warp, events[header.event_id], map_data)
#
#
# def calculate_accessibility(warp, event, map_data):
#     for other_warp in event.warps:
#         if warp != other_warp:
#             pass
#
#
# def check_obstructed(map_data, event, row, col):
#     perm_type = map_data.get_permissions(row, col)
#     coll_type = map_data.get_collisions(row, col)
#
#     for warp in event.warps:
#         if warp.local_x_pos == col and warp.local_y_pos == row:
#             return ('\u001b[38;5;5m{' + '}\u001b[0m').format('W')  # purple
#
#     for permission_obstruction_type in permission_obstructions_dict.keys():
#         if permission_obstructions_dict[permission_obstruction_type].__contains__(perm_type):
#             if permission_obstruction_type == 'cliffs':
#                 return ('\u001b[38;5;138m{' + '}\u001b[0m').format('J')  # brown
#             elif permission_obstruction_type == 'surf':
#                 return ('\u001b[38;5;6m{' + '}\u001b[0m').format('S')  # cyan
#             elif permission_obstruction_type == 'waterfall':
#                 return '4'
#             elif permission_obstruction_type == 'slides':
#                 return '5'
#             elif permission_obstruction_type == 'rock_climb':
#                 return '6'
#             elif permission_obstruction_type == 'bike_passable':
#                 return '7'
#             elif permission_obstruction_type == 'bike_no_pass':
#                 return '8'
#
#     for overworld in event.overworlds:
#         if overworld.local_x_pos == col and overworld.local_y_pos == row:
#             if overworld.script == 10000:
#                 return 'T'
#             elif overworld.script == 10001:
#                 return 'R'
#             elif overworld.script == 10002:
#                 return 'B'
#
#     if coll_type == 0x80:
#         return ('\u001b[38;5;1m{' + '}\u001b[0m').format(str(1))  # red
#
#     return ('\u001b[38;5;144m{' + '}\u001b[0m').format(str(0))  # greyish yellow
