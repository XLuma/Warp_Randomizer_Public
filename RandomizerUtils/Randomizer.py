"""
Randomizer.py

Core file containing the randomizer

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
import sys
import os

from RandomizerUtils import Definitions
from gen3 import EmeraldWarpRandomizer, FireRedWarpRandomizer
from nds.gen4 import PlatinumWarpRandomizer, PlatinumWarpMapInfo
from nds.gen4 import JohtoWarpRandomizer
from nds.gen5 import White2WarpRandomizer
import RandomizerUtils.Definitions
import RandomizerUtils.SructureDefinitions as structs
import RandomizerUtils.RandomGenerator as random_generator


def build_node(parent_node, map_nodes, map_warps, valid_warps, gen_functions):
    warps, connections = map_warps[parent_node.map]
    for warp in warps:
        for chain_break in gen_functions.info().map_chain_breaks:
            if chain_break in warp.dest_map:
                continue

        if warp.dest_map in map_nodes:
            parent_node.add_warps(warp, map_nodes[warp.dest_map])
            valid_warps.append(warp)
        else:
            if warp.dest_map not in map_warps:
                continue
            warp_node = structs.MapNode(warp.dest_map)
            map_nodes[warp.dest_map] = warp_node
            result = build_node(warp_node, map_nodes, map_warps, valid_warps, gen_functions)
            if not result:
                map_nodes.pop(warp.dest_map, None)
                continue
            parent_node.add_warps(warp, warp_node)
            valid_warps.append(warp)
    for connection in connections:
        if connection.map in map_nodes:
            parent_node.add_connection(map_nodes[connection.map])
        else:
            if connection.map not in map_warps:
                continue
            connection_node = structs.MapNode(connection.map)
            map_nodes[connection.map] = connection_node
            result = build_node(connection_node, map_nodes, map_warps, valid_warps, gen_functions)
            if not result:
                map_nodes.pop(connection.map, None)
                continue
            parent_node.add_connection(connection_node)
    if len(parent_node.connections) == 0 and len(parent_node.warp_nodes) == 0:
        return False
    return True


def build_map(map_warps: dict, gen_functions):
    map_nodes = dict()
    valid_warps = []
    starting_node = structs.MapNode(gen_functions.define_starting_map_id())
    map_nodes[gen_functions.define_starting_map_id()] = starting_node
    build_node(starting_node, map_nodes, map_warps, valid_warps, gen_functions)
    return starting_node, map_nodes, valid_warps


# Need to compile a list of every warp available
# Also build a list of warps to be ignored that we shouldn't randomize
def build_available_warps(randomized_map_warps, map_warps, all_maps, gen_functions):
    available_warps = []
    ignore_warps = []
    for map_name in map_warps:
        if map_name not in all_maps:
            # If the map is not in all_maps, we have determined this map is unreachable and we don't want to include
            # it in our randomzier, so we add do dont_randomize and skip the map
            #gen_functions.info().dont_randomize.append(map_name)
            continue
        skip = False
        for dont_randomize_map in gen_functions.info().dont_randomize:
            # Next we need to check if map is in don't randomize, since we allow things like "Map_Littleroot" and all
            # maps that begin with that would be auto added to dont randomize we need to go through entire don't
            # randomize instead of checking if map_name is in dont_randomize_map
            if dont_randomize_map in map_name:
                skip = True
                break
        if skip:
            continue

        randomized_warps, randomized_connections = randomized_map_warps[map_name]
        warps, connections = map_warps[map_name]
        to_ignore = map_name in gen_functions.info().not_needed
        index = -1
        for warp in warps:
            index = index + 1
            if 'gym' in map_name.lower() and warp.dest_map == map_name:
                # Warps inside gym dont get randomized, we consider these warps to be ignored
                continue

            if map_name in gen_functions.info().dont_randomize_warp \
                    and warp.warp_id in gen_functions.info().dont_randomize_warp[map_name]:
                # we also want to skip any warps that are in the don't randomize_warp
                # eventually we will actually give dont randomize warps filler warps from don't randomize but that
                # happens at the very end of randomizer
                continue

            skip = False
            for dont_randomize_map in gen_functions.info().dont_randomize:
                if dont_randomize_map in warp.dest_map:
                    # We need to check to make sure that destination map is also allowed to be randomized
                    skip = True
                    break
            if skip:
                continue

            if not to_ignore:
                # This warp is a valid warp that we must randomize
                available_warps.append([map_name, randomized_warps[index]])
            else:
                # If map is in not needed its allowed to be ignored
                ignore_warps.append([map_name, randomized_warps[index]])
    return available_warps, ignore_warps


# We will condense all pairs into a single warp in available and ignore warps
# This will keep things simpler and only deal with fixing pairs at the end
# That way during the actual randomization we never have to worry about dealing with pair logic
def remove_pair_warps(available_warps, ignore_warps, randomized_map_warps, map_warps, all_maps, gen_functions):
    paired_warps = dict()
    for game_map in all_maps:
        if 'Map_Castelia_City_h28' in game_map:
            debug = -2
        # We will iterate through all maps to find any pairs that exist
        warps, connections = map_warps[game_map]
        if len(warps) > 1:
            warp_coords = dict()
            for warp in warps:
                if 'gym' in game_map.lower() and (warp.dest_map == game_map or 'gym' in warp.dest_map.lower()):
                    continue
                if warp.no_pair:
                    continue
                for x in range(0, warp.width):
                    for y in range(0, warp.height):
                        warp_x = warp.x + x
                        warp_y = warp.y + y
                        offsets = [-1, 0, 1]
                        for offset in offsets:
                            # need to check x + 1 and y + 1 to see if warps are next ot each other
                            for coord_to_try in [(warp_x + offset, warp_y), (warp_x, warp_y + offset)]:
                                if coord_to_try in warp_coords and warp_coords[coord_to_try] != warp.warp_id:
                                    # if this offset coord exists as a warp and is not our current warp, we know we
                                    # have found a pair
                                    if game_map in paired_warps:
                                        # Check to see if a pair already exists in game map
                                        found_pair = False
                                        pairs = paired_warps[game_map]
                                        for pair in pairs:
                                            if warp_coords[coord_to_try] in pair and warp.warp_id not in pair:
                                                # Add warp to existing pair, if warp_id is currently not in pair
                                                pair.append(warp.warp_id)
                                                found_pair = True
                                                break
                                        if not found_pair:
                                            # Create new pair in game map entry
                                            paired_warps[game_map].append([warp_coords[coord_to_try], warp.warp_id])
                                    else:
                                        # create a game map pair entry
                                        paired_warps[game_map] = [[warp_coords[coord_to_try], warp.warp_id]]

                        warp_coords[(warp_x, warp_y)] = warp.warp_id  # finally add warp to warp coords for look up

            # It is possible that duplicate pairs exist so we must consolidate pairs into a single warp pair
            while True:
                completed = True
                if game_map not in paired_warps:
                    break  # No need to do anything if map has no pairs
                for i in range(0, len(paired_warps[game_map])):
                    paired_ids = paired_warps[game_map][i]
                    merge = None
                    for warp_id in paired_ids:
                        j = 0
                        for pair_to_check in paired_warps[game_map]:
                            # check if any warp_id in current pairing exists in any other pair
                            if i != j and warp_id in pair_to_check:
                                merge = pair_to_check  # warp exists in another pair therefore we must merge pairs
                                break
                            j = j + 1
                        if merge is not None:
                            break
                    if merge is not None:
                        for warp_id in merge:  # add all warps from merge into paired warps then remove merge from pairs
                            if warp_id not in paired_warps[game_map][i]:
                                paired_warps[game_map][i].append(warp_id)
                        paired_warps[game_map].remove(merge)
                        completed = False  # to adjust for size change in len(paired_warps[game_map]), we break out
                        break  # of for loop and loop on the while loop
                if completed:
                    break  # if we get through the entire for loop without handling any merges, we are good to move on

            # Ok finally we need to remove all except for first warp id of all pairs from available and ignore warps
            # this helps to ensure that we dont have to deal with any paired warps while randomizing
            if game_map not in paired_warps:
                continue  # No need to do anything if map has no pairs
            warps, connections = randomized_map_warps[game_map]
            for paired_ids in paired_warps[game_map]:
                # This is an important check, if a paired_warp is in map_to_map_warp_accessibility
                # we need to make sure the warp used in map_to_map_warp_accessibility isnt being erased
                # as such we update that entry to make sure it is using the warp in the pair that will still exist
                if game_map in gen_functions.info().map_to_map_warp_accessibility:
                    for key_map in gen_functions.info().map_to_map_warp_accessibility[game_map]:
                        warp_tuple = gen_functions.info().map_to_map_warp_accessibility[game_map][key_map]
                        if warp_tuple.warp_id in paired_ids:
                            gen_functions.info().map_to_map_warp_accessibility[game_map][key_map] = \
                                gen_functions.info().WT(paired_ids[0], warp_tuple.flag)

                # Now we can remove all pairs except the first warp in paired_ids from available pool
                for warp_id in paired_ids[1:]:
                    if [game_map, warps[warp_id]] in available_warps:
                        available_warps.remove([game_map, warps[warp_id]])
                    elif [game_map, warps[warp_id]] in ignore_warps:
                        ignore_warps.remove([game_map, warps[warp_id]])
    return paired_warps


# After all randomization has occurred we need to go through and make sure all pairs are now matching and repaired
def restore_paired_warps(final_map_warps, paired_warps):
    for game_map in paired_warps:
        warps, connections = final_map_warps[game_map]
        for paired_ids in paired_warps[game_map]:
            # We know that the first warp in paired_ids should be the warp that was randomized
            # we need to make sure all other warps for the pair then match
            randomized_warp = paired_ids[0]
            for warp_id in paired_ids[1:]:
                warps[warp_id].dest_map = warps[randomized_warp].dest_map
                warps[warp_id].dest_warp_id = warps[randomized_warp].dest_warp_id


# Split map/warp pairs into an end node or a connecting node
def map_warp_divide(all_maps, map_warps, gen_functions, available_warps):
    end = []
    connects = []
    for game_map in all_maps:
        if game_map in gen_functions.info().not_needed:
            continue  # It is already assumed all not needed are end maps that can only be used at end of randomization

        # In order to get an accurate number of warps per map we can use available_warps since it is already adjusted
        # by removing all paired warps
        warp_count = 0
        for warp in available_warps:
            if warp[0] == game_map:
                warp_count = warp_count + 1
        warps, connections = map_warps[game_map]
        if warp_count > 1 and 'gym' not in game_map.lower():
            # We now this map has multiple real warps that potentially connect so we must check
            for warp in warps:
                if game_map not in gen_functions.info().map_warp_accessibility:
                    # if the map isnt specified in map warp accessibility we know that every warp connects
                    connects.append([game_map, warp.warp_id])
                elif warp.warp_id not in gen_functions.info().map_warp_accessibility[game_map] or \
                        (game_map in gen_functions.info().dont_randomize_warp and
                         warp.warp_id in gen_functions.info().dont_randomize_warp[game_map]):
                    # The warp was intended to not be randomized thus we should not add it to any list that we should
                    # consider
                    continue
                else:
                    if len(gen_functions.info().map_warp_accessibility[game_map][warp.warp_id]) != 0:
                        # Warp connects to additional warps
                        connects.append([game_map, warp.warp_id])
                    else:
                        # This warp connects with no other warps thus is considered an end point
                        end.append([game_map, warp.warp_id])
        else:
            if len(connections) > 0:
                # If there is only one warp or less, as long as there is a connection we can assume the map can continue
                connects.append([game_map, -1])
            elif warp_count == 1:
                # if there is only 1 warp and no connections, we know for certainty the map is a dead end
                end.append([game_map, -1])
            else:
                # len(connections) == 0 and warp_count == 0, therefore there are no valid warps on this map and it is
                # not considered reachable
                continue
    return end, connects


def get_all_accessible_warps_from_warp(game_map, warp_id, accessible_maps, gen_functions, randomized_map_warps,
                                       available_warps, orig_map_warps, include_starting_warp):
    accessible_warps = []
    dont_randomize_warps = []
    warps, connections = randomized_map_warps[game_map]
    for warp in warps:
        check_warps, check_connections = randomized_map_warps[game_map]
        if warp.warp_id == warp_id:
            if include_starting_warp:
                # This for scenario when coming from connection and we want to include it in our don't randomize
                # and accessible warp list, so we must check its a don't randomize warp
                if [game_map, warps[warp.warp_id]] not in available_warps:
                    if check_warps[warp.warp_id].dest_map == '':
                        # We know warp was not intended to be randomized so lets move on from rom this warp
                        dont_randomize_warps.append(warp.warp_id)
                        continue
                accessible_warps.append(warp.warp_id)
            continue  # skip incoming warp
        if [game_map, warps[warp.warp_id]] not in available_warps:
            # There are two scenarios where this could occur, firstly the warp was intentionally removed to not be
            # available or the warp as already been randomized, the only way to check is to see if the warp has been
            # randomized

            if check_warps[warp.warp_id].dest_map == '':
                # We know warp was not intended to be randomized so lets move on from rom this warp
                dont_randomize_warps.append(warp.warp_id)
                continue

        if game_map in gen_functions.info().map_warp_accessibility:
            # we must now check if incoming warp can reach this current warp following the rules specified
            if warp.warp_id not in gen_functions.info().map_warp_accessibility[game_map] or \
                    (game_map in gen_functions.info().dont_randomize_warp and
                     warp.warp_id in gen_functions.info().dont_randomize_warp[game_map]):
                # this is a don't randomize warp, so lets just ignore this warp
                continue
            if not gen_functions.info().is_warp_to_warp_valid(game_map, accessible_maps, warp_id, warp.warp_id):
                continue  # We know that we cannot currently go from incoming warp to this warp

        # If we have made it passed all these checks we know that the warp is accessible from our current warp
        accessible_warps.append(warp.warp_id)
    return accessible_warps, dont_randomize_warps


def add_to_accessible_maps(accessible_maps, current_map, previous_map, incoming_warp_id):
    if current_map in accessible_maps:
        if (incoming_warp_id != -1 and incoming_warp_id not in accessible_maps[current_map]) or \
                (incoming_warp_id == -1 and previous_map not in accessible_maps[current_map]):
            if incoming_warp_id != -1:
                accessible_maps[current_map].append(incoming_warp_id)
            else:
                accessible_maps[current_map].append(previous_map)
    else:
        if incoming_warp_id != -1:
            accessible_maps[current_map] = [incoming_warp_id]  # came from warp
        else:
            accessible_maps[current_map] = [previous_map]  # came from connection


# Accessible_maps allows us to keep track of everything across multiple loops
# Visited Maps is intended to reset after each run through
def build_warps_to_randomize(accessible_maps, visited_maps, warps_to_randomize, randomized_map_warps, available_warps,
                             current_map, previous_map, incoming_warp_id, gen_functions, orig_map_warps):
    if current_map == 'Map_Galactic_HQ_Floor02_00':
        help = 0
    if current_map not in randomized_map_warps:
        return

    warps, connections = randomized_map_warps[current_map]
    starting_warp = 0
    include_starting_warp = incoming_warp_id == -1

    # Ok lets determine if we have already checked this exact map/warp id combination or this exact connection path
    if current_map in visited_maps:
        if (incoming_warp_id != -1 and incoming_warp_id in visited_maps[current_map]) or \
                (incoming_warp_id == -1 and previous_map in visited_maps[current_map]):
            # In this pass we have already checked this path, breaks any potential loops
            return
        else:
            if incoming_warp_id != -1:
                visited_maps[current_map].append(incoming_warp_id)  # came from warp
            else:
                visited_maps[current_map].append(previous_map)  # came from connection
    else:
        if incoming_warp_id != -1:
            visited_maps[current_map] = [incoming_warp_id]  # came from warp
        else:
            visited_maps[current_map] = [previous_map]  # came from connection

    # Similarly lets update accessible_maps
    add_to_accessible_maps(accessible_maps, current_map, previous_map, incoming_warp_id)

    if incoming_warp_id != -1:
        starting_warp = incoming_warp_id  # since we entered map from warp, our starting warp will be incoming warp

        # Next we need to check if we are entering from a cont go back warp
        # Basically if we hit a 1-way warp we want to consider this warp as a dead end, this ensures that any other
        # warps that potentially connect to this one way are not dead ends but rather maps that connect to the main
        # loop
        if current_map in gen_functions.info().cant_go_back_warps and \
                incoming_warp_id in gen_functions.info().cant_go_back_warps[current_map]:
            starting_warp = -3  # Lets us know that we should not add any warps to randomize for this map
    else:
        # Since we are coming from a connection we need to handle setting our starting warp a bit differently
        # We need to check if we can add any warps from current_map
        if len(warps) == 0:
            starting_warp = -2  # there are no warps to check
        if current_map in gen_functions.info().map_to_map_warp_accessibility and \
                previous_map in gen_functions.info().map_to_map_warp_accessibility[current_map]:
            # map_to_map_warp_accessibility defines special scenarios for what warps to use when going from previous
            # map to current map, if it is specified then we use that warp to start
            wt_to_check = gen_functions.info().map_to_map_warp_accessibility[current_map][previous_map]
            if gen_functions.info().is_warp_ready(wt_to_check, accessible_maps):
                starting_warp = wt_to_check.warp_id
            else:
                starting_warp = -2  # Not currently able to traverse to any warp from this connection

    if starting_warp != -2:  # we need to check warps
        # Lets get a list of every warp that connects to our current warp that we can reach and isn't intended to not
        # be randomized
        accessible_warps, dont_randomize_warps = get_all_accessible_warps_from_warp(current_map, starting_warp,
                                                                                    accessible_maps, gen_functions,
                                                                                    randomized_map_warps,
                                                                                    available_warps, orig_map_warps,
                                                                                    include_starting_warp)

        for dont_randomize_warp in dont_randomize_warps:
            # Even though we dont want to randomize these warps we need to check if this warp belongs to dont_randomize
            # list, and if it does we should fill in the correct dont randomize info just in case and follow path
            # as these maps may lead to new areas or even be required as an event flag
            orig_warps, orig_connections = orig_map_warps[current_map]
            for dont_randomize_map in gen_functions.info().dont_randomize:
                if dont_randomize_map in orig_warps[dont_randomize_warp].dest_map or dont_randomize_map in current_map:
                    # we know this warp belongs to don't randomize
                    warps[dont_randomize_warp].dest_map = orig_warps[dont_randomize_warp].dest_map
                    warps[dont_randomize_warp].dest_warp_id = orig_warps[dont_randomize_warp].dest_warp_id
                    add_to_accessible_maps(accessible_maps, current_map, previous_map, dont_randomize_warp)
                    build_warps_to_randomize(accessible_maps, visited_maps, warps_to_randomize, randomized_map_warps,
                                             available_warps, warps[dont_randomize_warp].dest_map, current_map,
                                             warps[dont_randomize_warp].dest_warp_id, gen_functions, orig_map_warps)
                    break

        if starting_warp != -3:  # starting_warp = -3 in can't go back scenario, we dont want to add any warps
            for accessible_warp in accessible_warps:
                # If the warp has not been randomized yet we need to make sure the warp is included in the
                # warps_to_randomize list, otherwise if it already has been randomized we need to follow that warp to
                # the next map and repeat the process on that map
                if warps[accessible_warp].dest_map == '':
                    # warp has yet to be set, lets check if we need to add to warps_to_randomize
                    to_add = [current_map, warps[accessible_warp]]
                    if to_add not in warps_to_randomize:
                        warps_to_randomize.append(to_add)
                else:
                    # warp has already been randomized, progress
                    add_to_accessible_maps(accessible_maps, current_map, previous_map, accessible_warp)
                    build_warps_to_randomize(accessible_maps, visited_maps, warps_to_randomize, randomized_map_warps,
                                             available_warps, warps[accessible_warp].dest_map, current_map,
                                             warps[accessible_warp].dest_warp_id, gen_functions, orig_map_warps)

    # Ok finally we need to progress through all progess-able connections attached to map
    if not gen_functions.info().is_map_progressable(current_map, accessible_maps,  -1, True):
        # First we check if the map is considered progress-able i.e. if a map requires a flag/hm to get through
        return  # Map is not progress-able so don't assume we can go through connections
    for connection in connections:
        # connections are much easier :D
        # First check if connection is navigable, if not navigable, cannot make connection
        is_valid_connection = True
        for non_navigable_connection in gen_functions.info().non_navigable_connections:
            if current_map == non_navigable_connection[0]:
                if connection.map in non_navigable_connection:
                    is_valid_connection = False
                    break

        if not is_valid_connection:
            continue  # the connection is considered non-navigable therefore skip connection

        # Check specific connection to connection rules to see if we can progress through to next connection
        if current_map in gen_functions.info().connection_to_connection_rules:
            if connection.map in gen_functions.info().connection_to_connection_rules[current_map]:
                flag = gen_functions.info().connection_to_connection_rules[current_map][connection.map]
                bits = bin(flag)  # Convert flag into bits representation
                connetion_pass = True
                index = 0
                for bit in reversed(bits):
                    if bit == '1':
                        if not gen_functions.info().check_progession_blockers(index, accessible_maps):
                            connetion_pass = False  # One of the requirements is missing for flag
                            break
                    index = index + 1
                if not connetion_pass:
                    continue

        # Connection is safe to progress though so lets move on to next map
        build_warps_to_randomize(accessible_maps, visited_maps, warps_to_randomize, randomized_map_warps,
                                 available_warps, connection.map, current_map, -1, gen_functions, orig_map_warps)
    return


def randomizer_flag_event_rules(end, connecting_warps, accessible_maps, warps_to_randomize, gen_functions, rng):
    chance = rng.randrange(0, 101)
    # Find the current forced order flag we are on
    current_forced = 0
    for flag in gen_functions.info().FORCED_FLAG_ORDER:
        if not gen_functions.info().search_for_needed_maps(gen_functions.info().FLAG_EVENT_LIST[flag], accessible_maps):
            current_forced = flag
            break

    # We can now select a map with the following rules
    # If map/warp goes towards current forced flag
    # if map/warp goes towards a non-forced flag
    # if map/warp goes towards a currently non accessible connecting warp
    requirement_list = []
    for req in gen_functions.info().FLAG_EVENT_LIST[current_forced]:
        if req not in requirement_list:
            requirement_list.append(req)  # get all required maps for current flag in forced order
    for i in range(0, gen_functions.info().END_FLAG + 1):
        if i not in gen_functions.info().FORCED_FLAG_ORDER:
            for req in gen_functions.info().FLAG_EVENT_LIST[i]:
                if req not in requirement_list:
                    requirement_list.append(req)  # add non order forced flags into requirement list

    # Satisfies first two checks
    for req in requirement_list:
        map_name = req
        warp_parts = []
        if ':' in req:
            map_name = req.split(':')[0]
            warp_parts = req.split(':')
        if end[0] == map_name:
            if len(warp_parts) == 0 and map_name not in accessible_maps:
                return True
            else:
                if str(end[1].warp_id) in warp_parts:
                    return True

    # Satisfies third check
    if chance > 30 or end in warps_to_randomize:
        return False  # if the warp is in the to randomize list then we know we can already reach warp

    if end[0] not in accessible_maps or end[1].warp_id not in accessible_maps[end[0]]:
        if gen_functions.info().is_map_progressable(end[0], accessible_maps, end[1].warp_id):
            if [end[0], end[1].warp_id] in connecting_warps:
                return True  # Verify this warp is a connecting warp and that it is progress-able

    return False


def select_random_warp(warps_to_randomize, available_warps, ignore_warps, randomized_map_warps, accessible_maps,
                       connecting_warps, ending_warps, gen_functions, rng):
    # first select a warp that is in current map world
    start = rng.choice(warps_to_randomize)

    if len(ignore_warps) == 0:
        return False

    # then we must choose a warp from available, if no warps left in available select from ignore list
    if len(available_warps) <= 1:
        while True:
            end = rng.choice(ignore_warps)
            if gen_functions.is_not_needed_map_ok(end[0]):
                break
    else:
        # need to find a suitable random selection

        connect_maps = []
        for connect in connecting_warps:
            if connect[0] not in connect_maps:
                connect_maps.append(connect[0])

        end_maps = []
        for end in ending_warps:
            if end[0] not in end_maps:
                end_maps.append(end[0])

        # First Thing We Want To Get At Least 1 Warp/Connection to every map that has leads to another connection/warp
        # This will give the map a wide spread
        has_all_connects = True
        for connect_map in connecting_warps:
            if connect_map[1] == -1:
                # there are no warps to this map so we can't assume that we will be able to reach it immediately
                continue
            if connect_map[0] not in accessible_maps:
                # if map is not in accessible_maps it means we do not yet currently have a path to this map
                # However if every warp in this map is not progress-able then there is no reason to be visiting this
                # map yet and are ok with not having a warp to this map yet
                map_has_warp = False
                for warp in available_warps:
                    if warp[0] == connect_map[0]:
                        map_has_warp = True  # First we need to verify that this warp is actually available
                        break
                if map_has_warp:
                    if gen_functions.info().is_map_progressable(connect_map[0], accessible_maps, connect_map[1]):
                        has_all_connects = False  # Map is considered progress-able so we should have a warp to this map
                        break

        # A check if there are any flags yet to be satisfied
        has_all_flags_met = True
        for i in range(0, gen_functions.info().END_FLAG + 1):
            if not gen_functions.info().search_for_needed_maps(gen_functions.info().FLAG_EVENT_LIST[i],
                                                               accessible_maps):
                has_all_flags_met = False
                break

        # A way to check if we have used all dead end points we want to include
        used_all_ends = True
        for end_map in ending_warps:
            if end_map[0] not in gen_functions.info().not_needed:
                if end_map[0] in accessible_maps:
                    # Maps can potentially have multiple warps, but if a warp doesn't connect to any other warp
                    # we still need to consider that as an end point, in this scenario we need to check if we actually
                    # have the end point warp included or not
                    has_warp = False
                    for accessible_warp in accessible_maps[end_map[0]]:
                        if end_map[1] == accessible_warp or end_map[1] == -1:
                            # if the warp exists in accessible_maps for the given map or the given map has only 1 warp
                            # we can consider the map already visited
                            has_warp = True
                            break
                    if not has_warp:
                        # Finally we need to check if this warp is even in the available_warps to choose from
                        map_has_warp = False
                        for warp in available_warps:
                            if warp[0] == end_map[0]:
                                map_has_warp = True
                                break
                        if map_has_warp:
                            # Warp is valid and has not been selected therefore we are missing an end point
                            used_all_ends = False
                            break
                if end_map[0] not in accessible_maps:
                    used_all_ends = False  # end map is not reachable currently
                    break

        # Basically just only allow us to select warps that aren't in the accessible warps yet
        used_all_no_dead_ends = True
        for warp in available_warps:
            if warp not in warps_to_randomize:
                used_all_no_dead_ends = False

        count = 0
        while True:
            # Ok select end point until we hit whatever condition we are on
            if count >= 100000:
                # safety if we ever loop that many times, chances are we are stuck stuck
                return False
            count = count + 1
            end = rng.choice(available_warps)
            if end == start:
                continue
            if end[0] == start[0]:
                continue  # no warp can lead back to same map

            if not has_all_connects:
                # Ensures we have never encountered this map before and that there is at least one progress-able
                # path
                pair = [end[0], end[1].warp_id]
                if end[0] in accessible_maps or not gen_functions.info().is_map_progressable(end[0], accessible_maps,
                                                                                             end[1].warp_id):
                    continue
                elif end[0] not in connect_maps:
                    continue
                elif end[0] in connect_maps and pair not in connecting_warps:
                    continue
                break  # selected warps are good
            elif not has_all_flags_met:
                # We now have a responsibility to make sure we include every flagged map
                if not randomizer_flag_event_rules(end, connecting_warps, accessible_maps, warps_to_randomize,
                                                   gen_functions, rng):
                    continue
                break
            elif not used_all_ends:
                if end[0] not in end_maps:
                    continue
                break
            elif not used_all_no_dead_ends:
                if end in warps_to_randomize:
                    continue
                break
            else:
                break

    # Now we need to update warp in randomized map warps
    start_warps, start_connections = randomized_map_warps[start[0]]
    end_warps, end_connections = randomized_map_warps[end[0]]

    start_warps[start[1].warp_id].dest_map = end[0]
    start_warps[start[1].warp_id].dest_warp_id = end[1].warp_id
    end_warps[end[1].warp_id].dest_map = start[0]
    end_warps[end[1].warp_id].dest_warp_id = start[1].warp_id

    # Finally we need to remove start/end
    if end in available_warps:
        available_warps.remove(end)
    if end in ignore_warps:
        ignore_warps.remove(end)
    if start in available_warps:
        available_warps.remove(start)
    if start in ignore_warps:
        ignore_warps.remove(start)
    if start in warps_to_randomize:
        warps_to_randomize.remove(start)
    if end in warps_to_randomize:
        warps_to_randomize.remove(end)
    return True


# Pretty much entirely used for debugging, just a copy of checks used in selecting random warps
def crisis_randomize_debug(accessible_maps, connecting_warps, available_warps, warps_to_randomize,
                           ending_warps, gen_functions):
    for connect_map in connecting_warps:
        if connect_map[1] == -1:
            continue
        if connect_map[0] not in accessible_maps:
            map_has_warp = False
            for warp in available_warps:
                if warp[0] == connect_map[0]:
                    map_has_warp = True
                    break  # DO NOT PUT A BREAK POINT HERE FOR DEBUG
            if map_has_warp:
                if gen_functions.info().is_map_progressable(connect_map[0], accessible_maps, connect_map[1]):
                    break  # PLACE BREAKPOINT HERE FOR DEBUG

    for i in range(0, gen_functions.info().END_FLAG + 1):
        if not gen_functions.info().search_for_needed_maps(gen_functions.info().FLAG_EVENT_LIST[i], accessible_maps):
            break  # PLACE BREAKPOINT HERE FOR DEBUG

    for end_map in ending_warps:
        if end_map[0] not in gen_functions.info().not_needed:
            if end_map[0] in accessible_maps:
                has_warp = False
                for accessible_warp in accessible_maps[end_map[0]]:
                    if end_map[1] == accessible_warp or end_map[1] == -1:
                        has_warp = True
                        break  # DO NOT PUT A BREAK POINT HERE FOR DEBUG
                if not has_warp:
                    map_has_warp = False
                    for warp in available_warps:
                        if warp[0] == end_map[0]:
                            map_has_warp = True
                            break
                    if map_has_warp:
                        break  # PLACE BREAKPOINT HERE FOR DEBUG
            if end_map[0] not in accessible_maps:
                break  # PLACE BREAKPOINT HERE FOR DEBUG

    # used_all_no_dead_ends = True
    for warp in available_warps:
        if warp not in warps_to_randomize:
            # used_all_no_dead_ends = False
            break  # PLACE BREAKPOINT HERE FOR DEBUG


# Don't randomize warps are warps that are impossible or near impossible to reach, therefore we give these warps
# warps from the not needed to ensure if a player ever does reach one of these warps, the warp still appears randomized
def select_random_for_dont_randomize_warp(randomized_map_warps, rng, gen_functions, ignore_warps):
    for map_name in gen_functions.info().dont_randomize_warp:
        warp_ids = gen_functions.info().dont_randomize_warp[map_name]
        for warp_id in warp_ids:
            if map_name in randomized_map_warps:
                start_warps, start_connections = randomized_map_warps[map_name]
                if warp_id >= len(start_warps):
                    continue
                if start_warps[warp_id].dest_map != '':
                    print("Issue with don't randomize warp")  # PLACE BREAKPOINT HERE FOR DEBUG
                    continue
                # Find a random warp from not needed
                while True:
                    if map_name == 'Map_Nimbasa_City' and warp_id == 7:
                        end = []
                        end.append('Map_Gear_Station_Interior_h66')
                        end.append(structs.Warp(422, 458, 32, 'Map_Gear_Station_Interior_h66', 7, 8, 62, 66, 1, 1, False)) #idk I inverted 7 and 8 and it worked
                        break
                    else:
                        end = rng.choice(ignore_warps)
                    if gen_functions.is_not_needed_map_ok(end[0]):
                        break

                # Now we need to update warp in randomized map warps
                end_warps, end_connections = randomized_map_warps[end[0]]

                start_warps[warp_id].dest_map = end[0]
                start_warps[warp_id].dest_warp_id = end[1].warp_id
                end_warps[end[1].warp_id].dest_map = map_name
                end_warps[end[1].warp_id].dest_warp_id = warp_id

                # Finally we need to remove end
                if end in ignore_warps:
                    ignore_warps.remove(end)


def randomize(all_maps, map_warps, gen_functions, rng, randomized_map_warps):
    available_warps, ignore_warps = build_available_warps(randomized_map_warps, map_warps, all_maps, gen_functions)
    pairs = remove_pair_warps(available_warps, ignore_warps, randomized_map_warps, map_warps, all_maps, gen_functions)
    ends, connects = map_warp_divide(all_maps, map_warps, gen_functions, available_warps)

    # print('ENDS:')
    # for entry in ends:
    #     print(entry[0])
    # print('----------')

    # Build out data structures for us to keep track of maps we can currently reach and warps available for us to
    # randomize currently
    accessible_maps = dict()
    warps_to_randomize = []
    visited = dict()
    visited.clear()
    build_warps_to_randomize(accessible_maps, visited, warps_to_randomize, randomized_map_warps,
                             available_warps, gen_functions.define_starting_map_id(), '', -1, gen_functions, map_warps)

    while True:
        # Exit conditions for randomization
        if len(warps_to_randomize) == 0 and len(available_warps) != 0:
            # reached incomplete map lets do one more pass through build_warps_to_randomize and if still stuck
            # seed is invalid
            visited.clear()
            build_warps_to_randomize(accessible_maps, visited, warps_to_randomize, randomized_map_warps,
                                     available_warps, gen_functions.define_starting_map_id(), '', -1, gen_functions,
                                     map_warps)
            if len(warps_to_randomize) == 0:
                # seed is bad, give us a debug function call and then exit randomizer process
                crisis_randomize_debug(accessible_maps, connects, available_warps, warps_to_randomize, ends,
                                       gen_functions)
                return False

        elif len(warps_to_randomize) == 0 and len(available_warps) == 0:
            break  # Seed completed

        # First we do a random pick/insertion
        if not select_random_warp(warps_to_randomize, available_warps, ignore_warps, randomized_map_warps,
                                  accessible_maps, connects, ends, gen_functions, rng):
            # unable to find a valid selection for randomization, we will do one more pass through, if still failing,
            # seed is invalid
            visited.clear()
            build_warps_to_randomize(accessible_maps, visited, warps_to_randomize, randomized_map_warps,
                                     available_warps, gen_functions.define_starting_map_id(), '', -1, gen_functions,
                                     map_warps)
            if not select_random_warp(warps_to_randomize, available_warps, ignore_warps, randomized_map_warps,
                                      accessible_maps, connects, ends, gen_functions, rng):
                crisis_randomize_debug(accessible_maps, connects, available_warps, warps_to_randomize, ends,
                                       gen_functions)
                return False
        # Then we build all nodes again
        visited.clear()
        build_warps_to_randomize(accessible_maps, visited, warps_to_randomize, randomized_map_warps,
                                 available_warps, gen_functions.define_starting_map_id(), '', -1, gen_functions,
                                 map_warps)

    select_random_for_dont_randomize_warp(randomized_map_warps, rng, gen_functions, ignore_warps)
    restore_paired_warps(randomized_map_warps, pairs)
    return True


def clean_up_map_warps(map_warps):
    clean_map_warps = dict()
    for map_name in map_warps:
        # For every map warp we must create clean copy where dest map and dest warp id are not set
        # This allows for us to easily check that every warp that was meant to be set was in fact set
        warps, connections = map_warps[map_name]
        temp1 = []
        temp2 = []
        for warp in warps:
            temp1.append(structs.Warp(warp.x, warp.y, 0, '', -1, warp.warp_id, warp.header_id))
        for connection in connections:
            temp2.append(structs.Connection('', 0, connection.map))
        clean_map_warps[map_name] = [temp1, temp2]
    return clean_map_warps


def check_randomized_map_warps(randomized_map_warps, map_warps, gen_functions, all_maps):
    # Lets Check that every warp intended to be randomized was randomized
    for map_name in randomized_map_warps:
        warps, connections = randomized_map_warps[map_name]
        orig_warps, orig_connections = map_warps[map_name]
        index = 0
        for warp in warps:
            if warp.dest_map == '' or warp.dest_warp_id == -1:
                # Map wasn't randomized... lets figure out if that is ok?
                is_in_dont_randomize = False  # need to check if map is in dont randomize
                for dont_randomize_map in gen_functions.info().dont_randomize:
                    if dont_randomize_map in map_name:
                        is_in_dont_randomize = True

                if map_name not in all_maps:
                    # We dont even consider this map as ever reachable and should not be randomized
                    warp.dest_map = orig_warps[index].dest_map
                    warp.dest_warp_id = orig_warps[index].dest_warp_id
                elif is_in_dont_randomize or map_name in gen_functions.info().not_needed:
                    # these maps are expected to not be randomized thus it is ok if it wasnt randomized
                    # however we should at least make sure that randomized_map_warps gets the correct warp info
                    warp.dest_map = orig_warps[index].dest_map
                    warp.dest_warp_id = orig_warps[index].dest_warp_id
                elif 'gym' in map_name.lower():
                    # Warps inside gym shouldn't be randomized, however the main entry of the gym should be randomized
                    if orig_warps[index].dest_map == map_name:
                        # A warp inside gym, so shouldn't be random
                        warp.dest_map = orig_warps[index].dest_map
                        warp.dest_warp_id = orig_warps[index].dest_warp_id
                    else:
                        # Gym entrance not randomized... this is a failure
                        return False
                elif (map_name in gen_functions.info().dont_randomize_warp and
                      warp.warp_id in gen_functions.info().dont_randomize_warp[map_name]):
                    # specific warp is listed as a dont randomize warp
                    # these warps should be assigned random warps from the not needed list
                    return False
                else:
                    # A warp should only not be defined it its specified in not needed, don't randomize, don't randomize
                    # warp, is not included in the all maps or is a warp inside a gym
                    # if we hit this scenario we have a bug
                    return False
            index = index + 1

    # If we get past the entire for loop then we know all warps are set
    return True


def check_flags(flag, current_flags_satisfied):
    bits = bin(flag)  # git binary representation of flag
    index = 0
    warp_pass = True
    for bit in reversed(bits):
        if bit == '1' and current_flags_satisfied[index] != 1:
            # if bit set, we check bits index location to determine if we currently consider that flag satisfied
            # if that flag is not satisfied, this is not a valid warp to go to
            warp_pass = False
            break
        index = index + 1
    return warp_pass


# Find map based off current flag restrictions
# If it can't find map return empty path, otherwise return path taken
def find_map(map_to_find, warp_to_find, randomized_map_warps, gen_functions, current_flags_satisfied):
    paths_tested = [[(gen_functions.define_starting_map_id(), -1)]]
    maps_visited = [gen_functions.define_starting_map_id()]

    if map_to_find == gen_functions.define_starting_map_id():
        return [(gen_functions.define_starting_map_id(), -1)]

    while True:
        new_paths_tested = []
        for path in paths_tested:
            last_map, last_warp_id = path[len(path) - 1]

            next_warp_to_check = -2
            # check any special conditions for determining warp to start from if coming from connection
            if last_warp_id == -1:
                if (last_map in gen_functions.info().map_to_map_warp_accessibility and
                        path[len(path) - 2][0] in gen_functions.info().map_to_map_warp_accessibility[last_map]):
                    # ok so we should use this to define warp to start
                    warp_tuple = gen_functions.info().map_to_map_warp_accessibility[last_map][path[len(path) - 2][0]]
                    if check_flags(warp_tuple.flag, current_flags_satisfied):
                        # warp is valid
                        next_warp_to_check = warp_tuple.warp_id
            else:
                next_warp_to_check = last_warp_id

            warps, connections = randomized_map_warps[last_map]
            if next_warp_to_check != -2:
                # First we take all accessible warps and add them to the paths tested
                for warp in warps:
                    # Check map to see if there are any warp to warp restrictions
                    if last_map in gen_functions.info().map_warp_accessibility:
                        # if there are warp restrictions we must abide by these warp restrictions and add only the
                        # the allowed warps
                        if warp.warp_id in gen_functions.info().map_warp_accessibility[last_map]:
                            # warp rules will define the warps that connect to
                            warp_rules = gen_functions.info().map_warp_accessibility[last_map][warp.warp_id]


# This sanity check will be two fold... First we will check flag order list and ensure no warp is locked behind
# A check that should be complete after the current check we are on, and will create a cheat log for us
# cheat log is not 100% guaranteed to be the shortest path
# Second we will check that every map is reachable to starting map
def sanity_randomize_check(randomized_map_warps, map_warps, gen_functions, all_maps):
    flags_satisfied = [0] * len(gen_functions.info().FLAG_EVENT_LIST)
    for main_flag_check in gen_functions.info().FORCED_FLAG_ORDER:
        maps_to_find = gen_functions.info().FLAG_EVENT_LIST[main_flag_check]
        for map_to_find in maps_to_find:
            warp_to_find = -1
            if ':' in map_to_find:
                parts = map_to_find.split(':')
                map_to_find = parts[0]
                warp_to_find = int(parts[1])
            find_map(map_to_find, warp_to_find, randomized_map_warps, gen_functions, flags_satisfied)


def start_randomizer(input_rom_path, output_rom_path, rom_type, fixed_seed=-1, revision=0):
    if fixed_seed != -1:
        if isinstance(fixed_seed, int):
            rng = random_generator.Random(seed=fixed_seed)
        else:
            rng = random_generator.Random(seed=hash(fixed_seed))
    else:
        fixed_seed = random_generator.randrange(sys.maxsize)
        rng = random_generator.Random(seed=fixed_seed)

    if rom_type == Definitions.GEN3_EMERALD:
        gen_functions = EmeraldWarpRandomizer.EmeraldRandomizerFunctions()
    elif rom_type == Definitions.GEN4_PLATINUM:
        gen_functions = PlatinumWarpRandomizer.PlatinumRandomizerFunctions()
    elif rom_type == Definitions.GEN4_HEARTGOLD or rom_type == Definitions.GEN4_SOULSILVER:  # todo add back later
        gen_functions = JohtoWarpRandomizer.HeartGoldSoulSilverRandomizerFunctions()
    elif rom_type == Definitions.GEN3_FIRERED or rom_type == Definitions.GEN3_LEAFGREEN:
        gen_functions = FireRedWarpRandomizer.FireRedRandomizerFunctions(rom_type, revision)
    elif rom_type == Definitions.GEN5_WHITE2:  # todo put b2 back when we support it
        gen_functions = White2WarpRandomizer.White2RandomizerFunctions()
    else:
        return True, fixed_seed, True

    map_warps = gen_functions.load_map_data()
    starting_node, map_nodes, valid_warps = build_map(map_warps, gen_functions)
    non_reachable_to_add = gen_functions.determine_unreachable_maps(map_nodes, map_warps)
    all_maps = list(map_nodes.keys())
    all_maps = all_maps + non_reachable_to_add
    randomized_map_warps = clean_up_map_warps(map_warps)

    if not randomize(all_maps, map_warps, gen_functions, rng, randomized_map_warps):
        print('Seed Failed')
        return False, fixed_seed, False

    if not check_randomized_map_warps(randomized_map_warps, map_warps, gen_functions, all_maps):
        print('Seed Incorrect')
        return False, fixed_seed, False

    additional_output_path = output_rom_path.replace('.nds', '.txt')
    additional_output_path = additional_output_path.replace('.gba', '.txt')

    if sys.platform != 'win32':
        additional_output_path = additional_output_path.split('/')[len(additional_output_path.split('/')) - 1]
    else:
        additional_output_path = additional_output_path.split('/')[len(additional_output_path.split('/')) - 1]
    seed_path = 'seed_' + additional_output_path
    print(seed_path)
    # map_warps_path = 'warps_' + additional_output_path
    # map_warps_path = map_warps_path.replace('.txt', '.bin')
    # print(additional_output_path)

    print(fixed_seed)
    print(os.path.join(os.path.dirname(output_rom_path), seed_path))
    with open(os.path.join(os.path.dirname(output_rom_path), seed_path), 'w') as f:
        f.write(str(fixed_seed))
    # with open(os.path.join(os.path.dirname(output_rom_path), map_warps_path), 'wb') as outfile:
    #     pickle.dump(map_warps, outfile)

    gen_functions.write_rom(input_rom_path, output_rom_path, randomized_map_warps)
    return True, fixed_seed, False


def logic_brute_forcer(rom_type, fixed_seed=-1):
    if fixed_seed != -1:
        if isinstance(fixed_seed, int):
            rng = random_generator.Random(seed=fixed_seed)
        else:
            rng = random_generator.Random(seed=hash(fixed_seed))
    else:
        fixed_seed = random_generator.randrange(sys.maxsize)
        rng = random_generator.Random(seed=fixed_seed)

    if rom_type == Definitions.GEN3_EMERALD:
        gen_functions = EmeraldWarpRandomizer.EmeraldRandomizerFunctions()
    elif rom_type == Definitions.GEN4_PLATINUM:
        gen_functions = PlatinumWarpRandomizer.PlatinumRandomizerFunctions()
    # elif rom_type == Definitions.GEN4_HEARTGOLD or rom_type == Definitions.GEN4_SOULSILVER:
    #     gen_functions = JohtoWarpRandomizer.HeartGoldSoulSilverRandomizerFunctions()
    else:
        return True, fixed_seed

    map_warps = gen_functions.load_map_data()
    starting_node, map_nodes, valid_warps = build_map(map_warps, gen_functions)
    non_reachable_to_add = gen_functions.determine_unreachable_maps(map_nodes, map_warps)
    all_maps = list(map_nodes.keys())
    all_maps = all_maps + non_reachable_to_add
    randomized_map_warps = clean_up_map_warps(map_warps)

    if not randomize(all_maps, map_warps, gen_functions, rng, randomized_map_warps):
        print('moo')
        return False, fixed_seed

    if rom_type == Definitions.GEN4_PLATINUM:
        """This is for testing for gyms locked behind one-way warps"""
        # for entry in PlatinumWarpMapInfo.cant_go_back_warps:
        #     for warp_id in PlatinumWarpMapInfo.cant_go_back_warps[entry]:
        #         dest = map_warps[entry][0][warp_id].dest_map
        #         dest_warp = map_warps[entry][0][warp_id].dest_warp_id
        #         if 'Gym' in dest or 'League' in dest:
        #             if len(map_warps[dest][0]) == 1 and len(map_warps[dest][1]) == 0:
        #                 print(fixed_seed)
        #                 print('%s warp %i points to %s warp %i' % (entry, map_warps[entry][0][warp_id].warp_id, dest, dest_warp))
        #                 return True, fixed_seed

        """This is for finding maps locked behind an incorrect HM requirement"""
        found = False
        cancelled = False
        out = ''
        for event_idx in range(len(PlatinumWarpMapInfo.FLAG_EVENT_LIST)):
            for entry in PlatinumWarpMapInfo.FLAG_EVENT_LIST[event_idx]:
                entry = entry.split(':')[0]
                for warp_id in range(len(map_warps[entry][0])):
                    dest = map_warps[entry][0][warp_id].dest_map
                    dest_warp = map_warps[entry][0][warp_id].dest_warp_id
                    if dest in PlatinumWarpMapInfo.map_warp_accessibility.keys():
                        for warp_accessibility_id in PlatinumWarpMapInfo.map_warp_accessibility[dest]:
                            if warp_accessibility_id != dest_warp:
                                for warp_tuple in PlatinumWarpMapInfo.map_warp_accessibility[dest][
                                    warp_accessibility_id]:
                                    if warp_tuple.warp_id == dest_warp and (warp_tuple.flag >> event_idx) & 0b1 == 1:
                                        found = True
                                        out = '%s warp %i points to %s warp %i' % (
                                        dest, dest_warp, entry, map_warps[entry][0][warp_id].warp_id)
                                        continue
                                    if found and warp_tuple.warp_id == dest_warp and (
                                            warp_tuple.flag >> event_idx) & 0b1 == 0:
                                        cancelled = True
                                        continue

        if found and not cancelled:
            print(fixed_seed)
            print(out)
            return True, fixed_seed


if __name__ == "__main__":
    # result = start_randomizer(sys.argv[1], sys.argv[2], int(sys.argv[3]), int(sys.argv[4]))
    """This is for running the brute forcer"""
    # while True:
    #     result = logic_brute_forcer(Definitions.GEN4_PLATINUM)
    #     if result is not None:
    #         if result[0]:
    #             break
    #         else:
    #             continue
    #     else:
    #         continue
    # print('end')
