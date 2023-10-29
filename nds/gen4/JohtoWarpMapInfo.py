"""
JohtoWarpMapInfo.py

HGSS Warp Randomizer rule definitions

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
class WT:
    def __init__(self, warp_id, flag):
        if isinstance(warp_id, int):
            self.warp_id = warp_id
            if isinstance(flag, int):
                self.flag = flag
            elif isinstance(flag, list):
                self.flag = create_accessibility(flag)
            else:
                raise ValueError("Invalid Warp Tuple")
        else:
            raise ValueError("Invalid Warp Tuple")


def create_accessibility(arr):
    val = 0
    for flag in arr:
        val += (1 << flag)
    return val


# Event/HM Dependencies
# Any Warp/Connection that has an Event/HM Dependency will have a corresponding blocker flag
# Based off bits set in flag, we will know what dependencies are required to traverse
ROCKSMASH_FLAG = 0
KURT_FLAG = 1
CUT_FLAG = 2
BIKE_FLAG = 3
RADIOTOWER1_FLAG = 4
STRENGTH_FLAG = 5
SURF_FLAG = 6
LAKEOFRAGE_FLAG = 7
ROCKETHQ_FLAG = 8
WHIRLPOOL_FLAG = 9
RADIOTOWER2_FLAG = 10
WATERFALL_FLAG = 11
KANTO_FLAG = 12
UNLOCK_VIRIDIAN_GYM_FLAG = 13
ROCKCLIMB_FLAG = 14
KANTO_POWER_PLANT_FLAG = 15
ELITE_FOUR_FLAG = 16
END_FLAG = ELITE_FOUR_FLAG

rocksmash_event = ['Map_Violet_City_Gym_00', 'Map_Route_36',
                   'Map_Sprout_Tower_Room00_02']  # also applies to miracle seed guy on route 32
kurt_event = ['Map_Azalea_Town_Room04_00']  # this is kurt's house
cut_event = ['Map_Slowpoke_Well_Room00_01', 'Map_Ilex_Forest_Room00_00:0', 'Map_Azalea_Town_Gym_00',
             'Map_Violet_City_Gym_00']
bike_event = ['Map_Goldenrod_City_Room01_00']  # this is the bike shop
radiotower1_event = ['Map_Radio_Tower_Room00_00']
strength_event = ['Map_Radio_Tower_Room00_00', 'Map_Goldenrod_City_Room05_00', 'Map_Route_42:0',
                  'Map_Goldenrod_City_Gym_00', 'Map_Azalea_Town_Gym_00',
                  'Map_Violet_City_Gym_00']  # also applies to sudowoodo roadblocks
surf_event = ['Map_Ecruteak_City_Room04_00', 'Map_Burned_Tower_Room00_01', 'Map_Ecruteak_City_Gym_00',
              'Map_Goldenrod_City_Gym_00', 'Map_Azalea_Town_Gym_00', 'Map_Violet_City_Gym_00']
lakeofrage_event = ['Map_Cianwood_City_Room04_00', 'Map_Lighthouse_Room00_06', 'Map_Lake_of_Rage',
                    'Map_Olivine_City_Gym_00', 'Map_Cianwood_City_Gym_00', 'Map_Ecruteak_City_Gym_00',
                     'Map_Azalea_Town_Gym_00', 'Map_Violet_City_Gym_00']  # unsure if you are required to go to the mahogany gift shop before entering rocket hq
rockethq_event = ['Map_Team_Rocket_HQ_Room00_02:0', 'Map_Team_Rocket_HQ_Room00_02:4', 'Map_Team_Rocket_HQ_Room00_03:0',
                  'Map_Team_Rocket_HQ_Room00_03:2']  # also grants access to whirlpool
whirlpool_event = ['Map_Mahogany_Town_Gym_02', 'Map_Olivine_City_Gym_00', 'Map_Cianwood_City_Gym_00',
                   'Map_Ecruteak_City_Gym_00', 'Map_Goldenrod_City_Gym_00', 'Map_Azalea_Town_Gym_00',
                   'Map_Violet_City_Gym_00']
radiotower2_event = ['Map_Mahogany_Town_Gym_02:0', 'Map_Olivine_City_Gym_00', 'Map_Cianwood_City_Gym_00',
                     'Map_Radio_Tower_Room00_04:0', 'Map_Radio_Tower_Room00_00', 'Map_Goldenrod_City_Room00_04',
                     'Map_Radio_Tower_Room00_05']
waterfall_event = ['Map_Ice_Path_Room00_00:0', 'Map_Ice_Path_Room00_00:3', 'Map_Dragons_Den_Room00_02',
                   'Map_Blackthorn_City_Gym_00', 'Map_Mahogany_Town_Gym_02', 'Map_Olivine_City_Gym_00',
                   'Map_Cianwood_City_Gym_00', 'Map_Ecruteak_City_Gym_00', 'Map_Goldenrod_City_Gym_00',
                   'Map_Azalea_Town_Gym_00', 'Map_Violet_City_Gym_00']
kanto_event = ['Map_Bell_Tower_Room00_09', 'Map_Whirl_Islands_Room00_06', 'Map_Blackthorn_City_Gym_00',
               'Map_Mahogany_Town_Gym_02', 'Map_Olivine_City_Gym_00', 'Map_Cianwood_City_Gym_00',
               'Map_Ecruteak_City_Gym_00', 'Map_Goldenrod_City_Gym_00', 'Map_Azalea_Town_Gym_00',
               'Map_Violet_City_Gym_00']

unlock_viridian_gym_event = ['Map_Cinnabar_Island']

rockclimb_event = ['Map_Pallet_Town_Room02_00', 'Map_Violet_City_Gym_00', 'Map_Azalea_Town_Gym_00', 'Map_Goldenrod_City_Gym_00', 'Map_Ecruteak_City_Gym_00', 'Map_Cianwood_City_Gym_00', 'Map_Olivine_City_Gym_00', 'Map_Mahogany_Town_Gym_02', 'Map_Blackthorn_City_Gym_00',
                      'Map_Vermilion_City_Gym_00', 'Map_Saffron_City_Gym_00', 'Map_Celadon_City_Gym_00',
                      'Map_Cerulean_City_Gym_00', 'Map_Fuchsia_City_Gym_00', 'Map_Pewter_City_Gym_00',
                      'Map_Viridian_City_Gym_00', 'Map_Seafoam_Islands_Room00_05'] #added gyms manually just to see

kanto_power_plant_event = ['Map_Power_Plant_Room01_01', 'Map_Cerulean_City_Gym_00']

elite_four_event = [ 'Map_Pokemon_League_Room01_00', 'Map_Pokemon_League_Room02_00', 'Map_Pokemon_League_Room03_00',
                    'Map_Pokemon_League_Room04_00', 'Map_Pokemon_League_Room05_00']

#goldenrod_bf_event = [] #just in case

FORCED_FLAG_ORDER = [ROCKSMASH_FLAG, CUT_FLAG, STRENGTH_FLAG, SURF_FLAG, WHIRLPOOL_FLAG, WATERFALL_FLAG, ELITE_FOUR_FLAG, KANTO_FLAG, KANTO_POWER_PLANT_FLAG, ROCKCLIMB_FLAG] #cleanup kanto badges later
FLAG_EVENT_LIST = [rocksmash_event, kurt_event, cut_event, bike_event, radiotower1_event, strength_event, surf_event,
                   lakeofrage_event, rockethq_event, whirlpool_event, radiotower2_event, waterfall_event,
                   kanto_event, unlock_viridian_gym_event, rockclimb_event, kanto_power_plant_event, elite_four_event]  # incomplete

no_event_allowed = []  # incomplete
map_chain_breaks = []  # incomplete

# Event Based Warps and Warp Connections
# If map not specified, assume that all warps are accessible
map_warp_accessibility = {
    'Map_Route_26': {
        0: [WT(1, 0), WT(2, 0), WT(3, 0)],
        1: [WT(0, 0), WT(2, 0), WT(3, 0)],
        2: [WT(0, 0), WT(1, 0), WT(3, 0)],
        3: [WT(0, 0), WT(1, 0), WT(2, 0)],
    },
    'Map_Route_27': {
        1: [WT(0, 0), WT(2, 0)],
        2: [WT(0, 0), WT(1, 0)],
    },
    'Map_Route_31': {
        0: [WT(1, 0), WT(2, 0)],
        1: [WT(0, 0), WT(2, 0)],
        2: [WT(0, 0), WT(1, 0)],
    },
    'Map_New_Bark_Town': {
        0: [WT(1, 0), WT(2, 0), WT(3, 0), WT(4, 0)],
        1: [WT(0, 0), WT(2, 0), WT(3, 0), WT(4, 0)],
        2: [WT(0, 0), WT(1, 0), WT(3, 0), WT(4, 0)],
        3: [WT(0, 0), WT(1, 0), WT(2, 0), WT(4, 0)],
        4: [WT(0, 0), WT(1, 0), WT(2, 0), WT(3, 0)],
    },
    'Map_Cherrygrove_City': {
        0: [WT(1, 0), WT(2, 0), WT(3, 0), WT(4, 0)],
        1: [WT(0, 0), WT(2, 0), WT(3, 0), WT(4, 0)],
        2: [WT(0, 0), WT(1, 0), WT(3, 0), WT(4, 0)],
        3: [WT(0, 0), WT(1, 0), WT(2, 0), WT(4, 0)],
        4: [WT(0, 0), WT(1, 0), WT(2, 0), WT(3, 0)],
    },
    'Map_Route_32': {
        0: [WT(1, 0), WT(2, 0), WT(3, 0)],
        1: [WT(0, 0), WT(2, 0), WT(3, 0)],
        2: [WT(0, 0), WT(1, 0), WT(3, 0)],
        3: [WT(0, 0), WT(1, 0), WT(2, 0)],
    },
    'Map_Violet_City': {
        0: [WT(1, 0), WT(2, 0), WT(3, 0), WT(4, 0), WT(5, 0), WT(6, 0), WT(7, 0), WT(8, 0), WT(9, 0), WT(10, 0)],
        1: [WT(0, 0), WT(2, 0), WT(3, 0), WT(4, 0), WT(5, 0), WT(6, 0), WT(7, 0), WT(8, 0), WT(9, 0), WT(10, 0)],
        2: [WT(0, 0), WT(1, 0), WT(3, 0), WT(4, 0), WT(5, 0), WT(6, 0), WT(7, 0), WT(8, 0), WT(9, 0), WT(10, 0)],
        3: [WT(0, 0), WT(1, 0), WT(2, 0), WT(4, 0), WT(5, 0), WT(6, 0), WT(7, 0), WT(8, 0), WT(9, 0), WT(10, 0)],
        4: [WT(0, 0), WT(1, 0), WT(2, 0), WT(3, 0), WT(5, 0), WT(6, 0), WT(7, 0), WT(8, 0), WT(9, 0), WT(10, 0)],
        5: [WT(0, 0), WT(1, 0), WT(2, 0), WT(3, 0), WT(4, 0), WT(6, 0), WT(7, 0), WT(8, 0), WT(9, 0), WT(10, 0)],
        6: [WT(0, 0), WT(1, 0), WT(2, 0), WT(3, 0), WT(4, 0), WT(5, 0), WT(7, 0), WT(8, 0), WT(9, 0), WT(10, 0)],
        7: [WT(0, 0), WT(1, 0), WT(2, 0), WT(3, 0), WT(4, 0), WT(5, 0), WT(6, 0), WT(8, 0), WT(9, 0), WT(10, 0)],
        8: [WT(0, 0), WT(1, 0), WT(2, 0), WT(3, 0), WT(4, 0), WT(5, 0), WT(6, 0), WT(7, 0), WT(9, 0), WT(10, 0)],
        9: [WT(0, 0), WT(1, 0), WT(2, 0), WT(3, 0), WT(4, 0), WT(5, 0), WT(6, 0), WT(7, 0), WT(8, 0), WT(10, 0)],
        10: [WT(0, 0), WT(1, 0), WT(2, 0), WT(3, 0), WT(4, 0), WT(5, 0), WT(6, 0), WT(7, 0), WT(8, 0), WT(9, 0)],
    },
    'Map_Azalea_Town': {
        0: [WT(1, 0), WT(2, [CUT_FLAG]), WT(3, 0), WT(4, 0), WT(5, 0), WT(6, 0), WT(7, [KURT_FLAG])],
        1: [WT(0, 0), WT(2, [CUT_FLAG]), WT(3, 0), WT(4, 0), WT(5, 0), WT(6, 0), WT(7, [KURT_FLAG])],
        2: [WT(0, 0), WT(1, 0), WT(3, 0), WT(4, 0), WT(5, 0), WT(6, 0), WT(7, [KURT_FLAG])],
        3: [WT(0, 0), WT(1, 0), WT(2, [CUT_FLAG]), WT(4, 0), WT(5, 0), WT(6, 0), WT(7, [KURT_FLAG])],
        4: [WT(0, 0), WT(1, 0), WT(2, [CUT_FLAG]), WT(3, 0), WT(5, 0), WT(6, 0), WT(7, [KURT_FLAG])],
        5: [WT(0, 0), WT(1, 0), WT(2, [CUT_FLAG]), WT(3, 0), WT(4, 0), WT(6, 0), WT(7, [KURT_FLAG])],
        6: [WT(0, 0), WT(1, 0), WT(2, [CUT_FLAG]), WT(3, 0), WT(4, 0), WT(5, 0), WT(7, [KURT_FLAG])],
        7: [WT(0, [KURT_FLAG]), WT(1, [KURT_FLAG]), WT(2, [KURT_FLAG]), WT(3, [KURT_FLAG]), WT(4, [KURT_FLAG]), WT(5, [KURT_FLAG]), WT(6, [KURT_FLAG])],
    },
    'Map_Route_34': {
        0: [WT(1, 0), WT(2, 0)],
        1: [WT(0, 0), WT(2, 0)],
        2: [WT(0, 0), WT(1, 0)],
    },
    'Map_Goldenrod_City': { #might need event for warp 2 since its linked with radio tower 1 ?
        0: [WT(1, 0), WT(2, 0), WT(3, 0), WT(4, 0), WT(5, 0), WT(6, 0), WT(7, 0), WT(8, 0), WT(9, 0), WT(10, 0),
            WT(11, 0), WT(12, 0), WT(13, 0), WT(14, 0), WT(15, 0), WT(16, 0)],
        1: [WT(0, 0), WT(2, 0), WT(3, 0), WT(4, 0), WT(5, 0), WT(6, 0), WT(7, 0), WT(8, 0), WT(9, 0), WT(10, 0),
            WT(11, 0), WT(12, 0), WT(13, 0), WT(14, 0), WT(15, 0), WT(16, 0)],
        2: [WT(0, 0), WT(1, 0), WT(3, 0), WT(4, 0), WT(5, 0), WT(6, 0), WT(7, 0), WT(8, 0), WT(9, 0), WT(10, 0),
            WT(11, 0), WT(12, 0), WT(13, 0), WT(14, 0), WT(15, 0), WT(16, 0)],
        3: [WT(0, 0), WT(1, 0), WT(2, 0), WT(4, 0), WT(5, 0), WT(6, 0), WT(7, 0), WT(8, 0), WT(9, 0), WT(10, 0),
            WT(11, 0), WT(12, 0), WT(13, 0), WT(14, 0), WT(15, 0), WT(16, 0)],
        4: [WT(0, 0), WT(1, 0), WT(2, 0), WT(3, 0), WT(5, 0), WT(6, 0), WT(7, 0), WT(8, 0), WT(9, 0), WT(10, 0),
            WT(11, 0), WT(12, 0), WT(13, 0), WT(14, 0), WT(15, 0), WT(16, 0)],
        5: [WT(0, 0), WT(1, 0), WT(2, 0), WT(3, 0), WT(4, 0), WT(6, 0), WT(7, 0), WT(8, 0), WT(9, 0), WT(10, 0),
            WT(11, 0), WT(12, 0), WT(13, 0), WT(14, 0), WT(15, 0), WT(16, 0)],
        6: [WT(0, 0), WT(1, 0), WT(2, 0), WT(3, 0), WT(4, 0), WT(5, 0), WT(7, 0), WT(8, 0), WT(9, 0), WT(10, 0),
            WT(11, 0), WT(12, 0), WT(13, 0), WT(14, 0), WT(15, 0), WT(16, 0)],
        7: [WT(0, 0), WT(1, 0), WT(2, 0), WT(3, 0), WT(4, 0), WT(5, 0), WT(6, 0), WT(8, 0), WT(9, 0), WT(10, 0),
            WT(11, 0), WT(12, 0), WT(13, 0), WT(14, 0), WT(15, 0), WT(16, 0)],
        8: [WT(0, 0), WT(1, 0), WT(2, 0), WT(3, 0), WT(4, 0), WT(5, 0), WT(6, 0), WT(7, 0), WT(9, 0), WT(10, 0),
            WT(11, 0), WT(12, 0), WT(13, 0), WT(14, 0), WT(15, 0), WT(16, 0)],
        9: [WT(0, 0), WT(1, 0), WT(2, 0), WT(3, 0), WT(4, 0), WT(5, 0), WT(6, 0), WT(7, 0), WT(8, 0), WT(10, 0),
            WT(11, 0), WT(12, 0), WT(13, 0), WT(14, 0), WT(15, 0), WT(16, 0)],
        10: [WT(0, 0), WT(1, 0), WT(2, 0), WT(3, 0), WT(4, 0), WT(5, 0), WT(6, 0), WT(7, 0), WT(8, 0), WT(9, 0),
             WT(11, 0), WT(12, 0), WT(13, 0), WT(14, 0), WT(15, 0), WT(16, 0)],
        11: [WT(0, 0), WT(1, 0), WT(2, 0), WT(3, 0), WT(4, 0), WT(5, 0), WT(6, 0), WT(7, 0), WT(8, 0), WT(9, 0),
             WT(10, 0), WT(12, 0), WT(13, 0), WT(14, 0), WT(15, 0), WT(16, 0)],
        12: [WT(0, 0), WT(1, 0), WT(2, 0), WT(3, 0), WT(4, 0), WT(5, 0), WT(6, 0), WT(7, 0), WT(8, 0), WT(9, 0),
             WT(10, 0), WT(11, 0), WT(13, 0), WT(14, 0), WT(15, 0), WT(16, 0)],
        13: [WT(0, 0), WT(1, 0), WT(2, 0), WT(3, 0), WT(4, 0), WT(5, 0), WT(6, 0), WT(7, 0), WT(8, 0), WT(9, 0),
             WT(10, 0), WT(11, 0), WT(12, 0), WT(14, 0), WT(15, 0), WT(16, 0)],
        14: [WT(0, 0), WT(1, 0), WT(2, 0), WT(3, 0), WT(4, 0), WT(5, 0), WT(6, 0), WT(7, 0), WT(8, 0), WT(9, 0),
             WT(10, 0), WT(11, 0), WT(12, 0), WT(13, 0), WT(15, 0), WT(16, 0)],
        15: [WT(0, 0), WT(1, 0), WT(2, 0), WT(3, 0), WT(4, 0), WT(5, 0), WT(6, 0), WT(7, 0), WT(8, 0), WT(9, 0),
             WT(10, 0), WT(11, 0), WT(12, 0), WT(13, 0), WT(14, 0), WT(16, 0)],
        16: [WT(0, 0), WT(1, 0), WT(2, 0), WT(3, 0), WT(4, 0), WT(5, 0), WT(6, 0), WT(7, 0), WT(8, 0), WT(9, 0),
             WT(10, 0), WT(11, 0), WT(12, 0), WT(13, 0), WT(14, 0), WT(15, 0)],
    },
    'Map_Route_35': {
        0: [WT(1, 0), WT(2, 0), WT(3, 0)],
        1: [WT(0, 0), WT(2, 0), WT(3, 0)],
        2: [WT(0, 0), WT(1, 0), WT(3, 0)],
        3: [WT(0, 0), WT(1, 0), WT(2, 0)],
    },
    'Map_Route_36': {
        0: [WT(1, 0), WT(2, 0), WT(3, 0), WT(4, 0), WT(5, 0)],
        1: [WT(0, 0), WT(2, 0), WT(3, 0), WT(4, 0), WT(5, 0)],
        2: [WT(0, 0), WT(1, 0), WT(3, 0), WT(4, 0), WT(5, 0)],
        3: [WT(0, 0), WT(1, 0), WT(2, 0), WT(4, 0), WT(5, 0)],
        4: [WT(0, 0), WT(1, 0), WT(2, 0), WT(3, 0), WT(5, 0)],
        5: [WT(0, 0), WT(1, 0), WT(2, 0), WT(3, 0), WT(4, 0)],
    },
    'Map_Ecruteak_City': {
        0: [WT(1, 0), WT(2, 0), WT(3, 0), WT(4, 0), WT(5, 0), WT(6, 0), WT(7, 0), WT(8, 0), WT(9, 0), WT(10, 0),
            WT(11, 0)],
        1: [WT(0, 0), WT(2, 0), WT(3, 0), WT(4, 0), WT(5, 0), WT(6, 0), WT(7, 0), WT(8, 0), WT(9, 0), WT(10, 0),
            WT(11, 0)],
        2: [WT(0, 0), WT(1, 0), WT(3, 0), WT(4, 0), WT(5, 0), WT(6, 0), WT(7, 0), WT(8, 0), WT(9, 0), WT(10, 0),
            WT(11, 0)],
        3: [WT(0, 0), WT(1, 0), WT(2, 0), WT(4, 0), WT(5, 0), WT(6, 0), WT(7, 0), WT(8, 0), WT(9, 0), WT(10, 0),
            WT(11, 0)],
        4: [WT(0, 0), WT(1, 0), WT(2, 0), WT(3, 0), WT(5, 0), WT(6, 0), WT(7, 0), WT(8, 0), WT(9, 0), WT(10, 0),
            WT(11, 0)],
        5: [WT(0, 0), WT(1, 0), WT(2, 0), WT(3, 0), WT(4, 0), WT(6, 0), WT(7, 0), WT(8, 0), WT(9, 0), WT(10, 0),
            WT(11, 0)],
        6: [WT(0, 0), WT(1, 0), WT(2, 0), WT(3, 0), WT(4, 0), WT(5, 0), WT(7, 0), WT(8, 0), WT(9, 0), WT(10, 0),
            WT(11, 0)],
        7: [WT(0, 0), WT(1, 0), WT(2, 0), WT(3, 0), WT(4, 0), WT(5, 0), WT(6, 0), WT(8, 0), WT(9, 0), WT(10, 0),
            WT(11, 0)],
        8: [WT(0, 0), WT(1, 0), WT(2, 0), WT(3, 0), WT(4, 0), WT(5, 0), WT(6, 0), WT(7, 0), WT(9, 0), WT(10, 0),
            WT(11, 0)],
        9: [WT(0, 0), WT(1, 0), WT(2, 0), WT(3, 0), WT(4, 0), WT(5, 0), WT(6, 0), WT(7, 0), WT(8, 0), WT(10, 0),
            WT(11, 0)],
        10: [WT(0, 0), WT(1, 0), WT(2, 0), WT(3, 0), WT(4, 0), WT(5, 0), WT(6, 0), WT(7, 0), WT(8, 0), WT(9, 0),
             WT(11, 0)],
        11: [WT(0, 0), WT(1, 0), WT(2, 0), WT(3, 0), WT(4, 0), WT(5, 0), WT(6, 0), WT(7, 0), WT(8, 0), WT(9, 0),
             WT(10, 0)],
    },
    'Map_Cianwood_City': {
        0: [WT(1, 0), WT(2, 0), WT(3, 0), WT(4, 0), WT(5, 0), WT(6, 0), WT(7, 0)],
        1: [WT(0, 0), WT(2, 0), WT(3, 0), WT(4, 0), WT(5, 0), WT(6, 0), WT(7, 0)],
        2: [WT(0, 0), WT(1, 0), WT(3, 0), WT(4, 0), WT(5, 0), WT(6, 0), WT(7, 0)],
        3: [WT(0, 0), WT(1, 0), WT(2, 0), WT(4, 0), WT(5, 0), WT(6, 0), WT(7, 0)],
        4: [WT(0, 0), WT(1, 0), WT(2, 0), WT(3, 0), WT(5, 0), WT(6, 0), WT(7, 0)],
        5: [WT(0, 0), WT(1, 0), WT(2, 0), WT(3, 0), WT(4, 0), WT(6, 0), WT(7, 0)],
        6: [WT(0, 0), WT(1, 0), WT(2, 0), WT(3, 0), WT(4, 0), WT(5, 0), WT(7, 0)],
        7: [WT(0, 0), WT(1, 0), WT(2, 0), WT(3, 0), WT(4, 0), WT(5, 0), WT(6, 0)],
    },
    'Map_Olivine_City': {
        0: [WT(1, 0), WT(2, 0), WT(3, 0), WT(4, 0), WT(5, 0), WT(6, 0), WT(7, 0), WT(8, 0)],
        1: [WT(0, 0), WT(2, 0), WT(3, 0), WT(4, 0), WT(5, 0), WT(6, 0), WT(7, 0), WT(8, 0)],
        2: [WT(0, 0), WT(1, 0), WT(3, 0), WT(4, 0), WT(5, 0), WT(6, 0), WT(7, 0), WT(8, 0)],
        3: [WT(0, 0), WT(1, 0), WT(2, 0), WT(4, 0), WT(5, 0), WT(6, 0), WT(7, 0), WT(8, 0)],
        4: [WT(0, 0), WT(1, 0), WT(2, 0), WT(3, 0), WT(5, 0), WT(6, 0), WT(7, 0), WT(8, 0)],
        5: [WT(0, 0), WT(1, 0), WT(2, 0), WT(3, 0), WT(4, 0), WT(6, 0), WT(7, 0), WT(8, 0)],
        6: [WT(0, 0), WT(1, 0), WT(2, 0), WT(3, 0), WT(4, 0), WT(5, 0), WT(7, 0), WT(8, 0)],
        7: [WT(0, 0), WT(1, 0), WT(2, 0), WT(3, 0), WT(4, 0), WT(5, 0), WT(6, 0), WT(8, 0)],
        8: [WT(0, 0), WT(1, 0), WT(2, 0), WT(3, 0), WT(4, 0), WT(5, 0), WT(6, 0), WT(7, 0)],
    },
    'Map_Route_41': {
        0: [WT(1, [SURF_FLAG, WHIRLPOOL_FLAG]), WT(2, [SURF_FLAG, WHIRLPOOL_FLAG]), WT(3, [SURF_FLAG, WHIRLPOOL_FLAG])],
        1: [WT(0, [SURF_FLAG, WHIRLPOOL_FLAG]), WT(2, [SURF_FLAG, WHIRLPOOL_FLAG]), WT(3, [SURF_FLAG, WHIRLPOOL_FLAG])],
        2: [WT(0, [SURF_FLAG, WHIRLPOOL_FLAG]), WT(1, [SURF_FLAG, WHIRLPOOL_FLAG]), WT(3, [SURF_FLAG, WHIRLPOOL_FLAG])],
        3: [WT(0, [SURF_FLAG, WHIRLPOOL_FLAG]), WT(1, [SURF_FLAG, WHIRLPOOL_FLAG]), WT(2, [SURF_FLAG, WHIRLPOOL_FLAG])],
    },
    'Map_Route_42': {
        0: [WT(1, 0), WT(2, 0), WT(3, [SURF_FLAG]), WT(5, [SURF_FLAG])],
        1: [WT(0, 0), WT(2, 0), WT(3, [SURF_FLAG]), WT(5, [SURF_FLAG])],
        2: [WT(0, 0), WT(1, 0), WT(3, [SURF_FLAG]), WT(5, [SURF_FLAG])],
        3: [WT(0, [SURF_FLAG]), WT(1, [SURF_FLAG]), WT(2, [SURF_FLAG]), WT(5, [SURF_FLAG])],
        5: [WT(0, [SURF_FLAG]), WT(1, [SURF_FLAG]), WT(2, [SURF_FLAG]), WT(3, [SURF_FLAG])],
    },
    'Map_Route_43': {
        0: [WT(1, 0), WT(2, 0), WT(3, 0), WT(4, 0), WT(5, 0)],
        1: [WT(0, 0), WT(2, 0), WT(3, 0), WT(4, 0), WT(5, 0)],
        2: [WT(0, 0), WT(1, 0), WT(3, 0), WT(4, 0), WT(5, 0)],
        3: [WT(0, 0), WT(1, 0), WT(2, 0), WT(4, 0), WT(5, 0)],
        4: [WT(0, 0), WT(1, 0), WT(2, 0), WT(3, 0), WT(5, 0)],
        5: [WT(0, 0), WT(1, 0), WT(2, 0), WT(3, 0), WT(4, 0)],
    },
    'Map_Mahogany_Town': {
        0: [WT(1, 0), WT(2, 0), WT(3, 0), WT(4, 0), WT(5, 0)],
        1: [WT(0, 0), WT(2, 0), WT(3, 0), WT(4, 0), WT(5, 0)],
        2: [WT(0, 0), WT(1, 0), WT(3, 0), WT(4, 0), WT(5, 0)],
        3: [WT(0, 0), WT(1, 0), WT(2, 0), WT(4, 0), WT(5, 0)],
        4: [WT(0, 0), WT(1, 0), WT(2, 0), WT(3, 0), WT(5, 0)],
        5: [WT(0, 0), WT(1, 0), WT(2, 0), WT(3, 0), WT(4, 0)],
    },
    'Map_Lake_of_Rage': {
        0: [WT(1, [CUT_FLAG, SURF_FLAG])],
        1: [WT(0, [CUT_FLAG, SURF_FLAG])]
    },
    'Map_Route_46': {
        2: [WT(0, 0), WT(1, 0)],
    },
    'Map_Blackthorn_City': { #why are these flagged with waterfall ? warp 2 is accessible with surf only. ill put waterfall too for translation purposes, but it may not be needed
        0: [WT(1, 0), WT(3, 0), WT(4, 0), WT(5, 0), WT(6, 0), WT(7, 0), WT(2, [SURF_FLAG, WATERFALL_FLAG])],
        1: [WT(0, 0), WT(3, 0), WT(4, 0), WT(5, 0), WT(6, 0), WT(7, 0), WT(2, [SURF_FLAG, WATERFALL_FLAG])],
        2: [WT(0, [SURF_FLAG, WATERFALL_FLAG]), WT(1, [SURF_FLAG, WATERFALL_FLAG]), WT(3, [SURF_FLAG, WATERFALL_FLAG]), WT(4, [SURF_FLAG, WATERFALL_FLAG]), WT(5, [SURF_FLAG, WATERFALL_FLAG]), WT(6, [SURF_FLAG, WATERFALL_FLAG]), WT(7, [SURF_FLAG, WATERFALL_FLAG])],
        3: [WT(0, 0), WT(1, 0), WT(4, 0), WT(5, 0), WT(6, 0), WT(7, 0), WT(2, [SURF_FLAG, WATERFALL_FLAG])],
        4: [WT(0, 0), WT(1, 0), WT(3, 0), WT(5, 0), WT(6, 0), WT(7, 0), WT(2, [SURF_FLAG, WATERFALL_FLAG])],
        5: [WT(0, 0), WT(1, 0), WT(3, 0), WT(4, 0), WT(6, 0), WT(7, 0), WT(2, [SURF_FLAG, WATERFALL_FLAG])],
        6: [WT(0, 0), WT(1, 0), WT(3, 0), WT(4, 0), WT(5, 0), WT(7, 0), WT(2, [SURF_FLAG, WATERFALL_FLAG])],
        7: [WT(0, 0), WT(1, 0), WT(3, 0), WT(4, 0), WT(5, 0), WT(6, 0), WT(2, [SURF_FLAG, WATERFALL_FLAG])],
    },
    'Map_Route_2': {
        0: [WT(1, 0), WT(2, [CUT_FLAG]), WT(3, [CUT_FLAG])],
        1: [WT(0, 0), WT(2, [CUT_FLAG]), WT(3, [CUT_FLAG])],
        2: [WT(3, 0), WT(0, [CUT_FLAG]), WT(1, [CUT_FLAG])],
        3: [WT(2, 0), WT(0, [CUT_FLAG]), WT(1, [CUT_FLAG])],
    },
    'Map_Route_28': {
        2: [WT(0, 0), WT(1, 0)],
    },
    'Map_Viridian_City': {
        0: [WT(1, 0), WT(2, 0), WT(3, 0), WT(4, 0), WT(5, 0), WT(6, 0)],
        1: [WT(0, [UNLOCK_VIRIDIAN_GYM_FLAG]), WT(2, 0), WT(3, 0), WT(4, 0), WT(5, 0), WT(6, 0)],
        2: [WT(0, [UNLOCK_VIRIDIAN_GYM_FLAG]), WT(1, 0), WT(3, 0), WT(4, 0), WT(5, 0), WT(6, 0)],
        3: [WT(0, [UNLOCK_VIRIDIAN_GYM_FLAG]), WT(1, 0), WT(2, 0), WT(4, 0), WT(5, 0), WT(6, 0)],
        4: [WT(0, [UNLOCK_VIRIDIAN_GYM_FLAG]), WT(1, 0), WT(2, 0), WT(3, 0), WT(5, 0), WT(6, 0)],
        5: [WT(0, [UNLOCK_VIRIDIAN_GYM_FLAG]), WT(1, 0), WT(2, 0), WT(3, 0), WT(4, 0), WT(6, 0)],
        6: [WT(0, [UNLOCK_VIRIDIAN_GYM_FLAG]), WT(1, 0), WT(2, 0), WT(3, 0), WT(4, 0), WT(5, 0)],
    },
    # 'Map_Indigo_Plateau': {
    # },
    # 'Map_Mount_Silver': {
    # },
    'Map_Route_6': {
        0: [WT(1, 0), WT(2, [KANTO_POWER_PLANT_FLAG])],
        1: [WT(0, 0), WT(2, [KANTO_POWER_PLANT_FLAG])],
        2: [WT(0, 0), WT(1, 0)],
    },
    'Map_Route_11': {
        0: [WT(1, 0), WT(2, 0)],
        1: [WT(0, 0), WT(2, 0)],
        2: [WT(0, 0), WT(1, 0)],
    },
    'Map_Vermilion_City': { #warp 6 can also be reached with cut, unsure if i put both flags or only one of em. (cut is the earliet one)
        0: [WT(1, 0), WT(2, 0), WT(3, 0), WT(4, 0), WT(5, 0), WT(7, 0), WT(6, [SURF_FLAG])],
        1: [WT(0, 0), WT(2, 0), WT(3, 0), WT(4, 0), WT(5, 0), WT(7, 0), WT(6, [SURF_FLAG])],
        2: [WT(0, 0), WT(1, 0), WT(3, 0), WT(4, 0), WT(5, 0), WT(7, 0), WT(6, [SURF_FLAG])],
        3: [WT(0, 0), WT(1, 0), WT(2, 0), WT(4, 0), WT(5, 0), WT(7, 0), WT(6, [SURF_FLAG])],
        4: [WT(0, 0), WT(1, 0), WT(2, 0), WT(3, 0), WT(5, 0), WT(7, 0), WT(6, [SURF_FLAG])],
        5: [WT(0, 0), WT(1, 0), WT(2, 0), WT(3, 0), WT(4, 0), WT(7, 0), WT(6, [SURF_FLAG])],
        6: [WT(0, 0), WT(1, 0), WT(2, 0), WT(3, 0), WT(4, 0), WT(5, 0), WT(7, 0)], #unsure about this one. if you spawn on warp 6, youre locked out. ill leave like that for now 
        7: [WT(0, 0), WT(1, 0), WT(2, 0), WT(3, 0), WT(4, 0), WT(5, 0), WT(6, [SURF_FLAG])],
    },
    'Map_Saffron_City': {
        0: [WT(1, 0), WT(2, 0), WT(3, 0), WT(4, 0), WT(5, 0), WT(6, 0), WT(7, 0), WT(8, 0), WT(9, 0), WT(10, 0),
            WT(11, 0), WT(12, 0), WT(13, 0), WT(14, 0), WT(15, 0), WT(16, 0)],
        1: [WT(0, 0), WT(2, 0), WT(3, 0), WT(4, 0), WT(5, 0), WT(6, 0), WT(7, 0), WT(8, 0), WT(9, 0), WT(10, 0),
            WT(11, 0), WT(12, 0), WT(13, 0), WT(14, 0), WT(15, 0), WT(16, 0)],
        2: [WT(0, 0), WT(1, 0), WT(3, 0), WT(4, 0), WT(5, 0), WT(6, 0), WT(7, 0), WT(8, 0), WT(9, 0), WT(10, 0),
            WT(11, 0), WT(12, 0), WT(13, 0), WT(14, 0), WT(15, 0), WT(16, 0)],
        3: [WT(0, 0), WT(1, 0), WT(2, 0), WT(4, 0), WT(5, 0), WT(6, 0), WT(7, 0), WT(8, 0), WT(9, 0), WT(10, 0),
            WT(11, 0), WT(12, 0), WT(13, 0), WT(14, 0), WT(15, 0), WT(16, 0)],
        4: [WT(0, 0), WT(1, 0), WT(2, 0), WT(3, 0), WT(5, 0), WT(6, 0), WT(7, 0), WT(8, 0), WT(9, 0), WT(10, 0),
            WT(11, 0), WT(12, 0), WT(13, 0), WT(14, 0), WT(15, 0), WT(16, 0)],
        5: [WT(0, 0), WT(1, 0), WT(2, 0), WT(3, 0), WT(4, 0), WT(6, 0), WT(7, 0), WT(8, 0), WT(9, 0), WT(10, 0),
            WT(11, 0), WT(12, 0), WT(13, 0), WT(14, 0), WT(15, 0), WT(16, 0)],
        6: [WT(0, 0), WT(1, 0), WT(2, 0), WT(3, 0), WT(4, 0), WT(5, 0), WT(7, 0), WT(8, 0), WT(9, 0), WT(10, 0),
            WT(11, 0), WT(12, 0), WT(13, 0), WT(14, 0), WT(15, 0), WT(16, 0)],
        7: [WT(0, 0), WT(1, 0), WT(2, 0), WT(3, 0), WT(4, 0), WT(5, 0), WT(6, 0), WT(8, 0), WT(9, 0), WT(10, 0),
            WT(11, 0), WT(12, 0), WT(13, 0), WT(14, 0), WT(15, 0), WT(16, 0)],
        8: [WT(0, 0), WT(1, 0), WT(2, 0), WT(3, 0), WT(4, 0), WT(5, 0), WT(6, 0), WT(7, 0), WT(9, 0), WT(10, 0),
            WT(11, 0), WT(12, 0), WT(13, 0), WT(14, 0), WT(15, 0), WT(16, 0)],
        9: [WT(0, 0), WT(1, 0), WT(2, 0), WT(3, 0), WT(4, 0), WT(5, 0), WT(6, 0), WT(7, 0), WT(8, 0), WT(10, 0),
            WT(11, 0), WT(12, 0), WT(13, 0), WT(14, 0), WT(15, 0), WT(16, 0)],
        10: [WT(0, 0), WT(1, 0), WT(2, 0), WT(3, 0), WT(4, 0), WT(5, 0), WT(6, 0), WT(7, 0), WT(8, 0), WT(9, 0),
             WT(11, 0), WT(12, 0), WT(13, 0), WT(14, 0), WT(15, 0), WT(16, 0)],
        11: [WT(0, 0), WT(1, 0), WT(2, 0), WT(3, 0), WT(4, 0), WT(5, 0), WT(6, 0), WT(7, 0), WT(8, 0), WT(9, 0),
             WT(10, 0), WT(12, 0), WT(13, 0), WT(14, 0), WT(15, 0), WT(16, 0)],
        12: [WT(0, 0), WT(1, 0), WT(2, 0), WT(3, 0), WT(4, 0), WT(5, 0), WT(6, 0), WT(7, 0), WT(8, 0), WT(9, 0),
             WT(10, 0), WT(11, 0), WT(13, 0), WT(14, 0), WT(15, 0), WT(16, 0)],
        13: [WT(0, 0), WT(1, 0), WT(2, 0), WT(3, 0), WT(4, 0), WT(5, 0), WT(6, 0), WT(7, 0), WT(8, 0), WT(9, 0),
             WT(10, 0), WT(11, 0), WT(12, 0), WT(14, 0), WT(15, 0), WT(16, 0)],
        14: [WT(0, 0), WT(1, 0), WT(2, 0), WT(3, 0), WT(4, 0), WT(5, 0), WT(6, 0), WT(7, 0), WT(8, 0), WT(9, 0),
             WT(10, 0), WT(11, 0), WT(12, 0), WT(13, 0), WT(15, 0), WT(16, 0)],
        15: [WT(0, 0), WT(1, 0), WT(2, 0), WT(3, 0), WT(4, 0), WT(5, 0), WT(6, 0), WT(7, 0), WT(8, 0), WT(9, 0),
             WT(10, 0), WT(11, 0), WT(12, 0), WT(13, 0), WT(14, 0), WT(16, 0)],
        16: [WT(0, 0), WT(1, 0), WT(2, 0), WT(3, 0), WT(4, 0), WT(5, 0), WT(6, 0), WT(7, 0), WT(8, 0), WT(9, 0),
             WT(10, 0), WT(11, 0), WT(12, 0), WT(13, 0), WT(14, 0), WT(15, 0)],
    },
    'Map_Route_5': {
        0: [WT(1, 0), WT(2, [KANTO_POWER_PLANT_FLAG])],
        1: [WT(0, 0), WT(2, [KANTO_POWER_PLANT_FLAG])],
        2: [WT(0, 0), WT(1, 0)],
        3: [WT(0, 0), WT(1, 0), WT(2, [KANTO_POWER_PLANT_FLAG])],
    },
    'Map_Route_10': {
        0: [WT(1, [SURF_FLAG]), WT(2, 0)],
        1: [WT(0, [SURF_FLAG]), WT(2, [SURF_FLAG])],
        2: [WT(0, 0), WT(1, [SURF_FLAG])]
    },
    'Map_Cerulean_City': {  # proposed fix. we can remove the badge requirement if we remove the guy blocking the way, leaving surf the only requirement
        0: [WT(1, 0), WT(2, 0), WT(3, 0), WT(4, 0), WT(5, 0), WT(6, 0), WT(7, [SURF_FLAG, ROCKCLIMB_FLAG])],
        1: [WT(0, 0), WT(2, 0), WT(3, 0), WT(4, 0), WT(5, 0), WT(6, 0), WT(7, [SURF_FLAG, ROCKCLIMB_FLAG])],
        2: [WT(0, 0), WT(1, 0), WT(3, 0), WT(4, 0), WT(5, 0), WT(6, 0), WT(7, [SURF_FLAG, ROCKCLIMB_FLAG])],
        3: [WT(0, 0), WT(1, 0), WT(2, 0), WT(4, 0), WT(5, 0), WT(6, 0), WT(7, [SURF_FLAG, ROCKCLIMB_FLAG])],
        4: [WT(0, 0), WT(1, 0), WT(2, 0), WT(3, 0), WT(5, 0), WT(6, 0), WT(7, [SURF_FLAG, ROCKCLIMB_FLAG])],
        5: [WT(0, 0), WT(1, 0), WT(2, 0), WT(3, 0), WT(4, 0), WT(6, 0), WT(7, [SURF_FLAG, ROCKCLIMB_FLAG])],
        6: [WT(0, 0), WT(1, 0), WT(2, 0), WT(3, 0), WT(4, 0), WT(5, 0), WT(7, [SURF_FLAG, ROCKCLIMB_FLAG])],
        7: [WT(0, [SURF_FLAG]), WT(1, [SURF_FLAG]), WT(2, [SURF_FLAG]), WT(3, [SURF_FLAG]), WT(4, [SURF_FLAG]), WT(5, [SURF_FLAG]), WT(6, [SURF_FLAG])]
    },
    # 'Map_Route_8': {
    # },
    'Map_Route_12': {
        0: [WT(1, 0), WT(2, 0)],
        1: [WT(0, 0), WT(2, 0)],
        2: [WT(0, 0), WT(1, 0)],
    },
    # 'Map_Route_15': {
    # },
    'Map_Lavender_Town': {
        0: [WT(1, 0), WT(2, 0), WT(3, 0), WT(4, 0), WT(5, 0), WT(6, 0)],
        1: [WT(0, 0), WT(2, 0), WT(3, 0), WT(4, 0), WT(5, 0), WT(6, 0)],
        2: [WT(0, 0), WT(1, 0), WT(3, 0), WT(4, 0), WT(5, 0), WT(6, 0)],
        3: [WT(0, 0), WT(1, 0), WT(2, 0), WT(4, 0), WT(5, 0), WT(6, 0)],
        4: [WT(0, 0), WT(1, 0), WT(2, 0), WT(3, 0), WT(5, 0), WT(6, 0)],
        5: [WT(0, 0), WT(1, 0), WT(2, 0), WT(3, 0), WT(4, 0), WT(6, 0)],
        6: [WT(0, 0), WT(1, 0), WT(2, 0), WT(3, 0), WT(4, 0), WT(5, 0)],
    },
    # 'Map_Route_7': {
    # },
    'Map_Celadon_City': {
        0: [WT(1, 0), WT(2, 0), WT(3, 0), WT(4, 0), WT(6, 0), WT(5, [CUT_FLAG])],
        1: [WT(0, 0), WT(2, 0), WT(3, 0), WT(4, 0), WT(6, 0), WT(5, [CUT_FLAG])],
        2: [WT(0, 0), WT(1, 0), WT(3, 0), WT(4, 0), WT(6, 0), WT(5, [CUT_FLAG])],
        3: [WT(0, 0), WT(1, 0), WT(2, 0), WT(4, 0), WT(6, 0), WT(5, [CUT_FLAG])],
        4: [WT(0, 0), WT(1, 0), WT(2, 0), WT(3, 0), WT(6, 0), WT(5, [CUT_FLAG])],
        5: [WT(0, [CUT_FLAG]), WT(1, [CUT_FLAG]), WT(2, [CUT_FLAG]), WT(3, [CUT_FLAG]), WT(4, [CUT_FLAG]), WT(6, [CUT_FLAG])],
        6: [WT(0, 0), WT(1, 0), WT(2, 0), WT(3, 0), WT(4, 0), WT(5, [CUT_FLAG])],
    },
    'Map_Route_16_Room02_00': {
        0: [WT(1, 0), WT(2, [CUT_FLAG])],
        1: [WT(0, 0), WT(2, [CUT_FLAG])],
        2: [WT(0, [CUT_FLAG]), WT(1, [CUT_FLAG])],
    },
    # 'Map_Route_16': {
    # },
    # 'Map_Route_18': {
    # },
    'Map_Fuchsia_City': {
        0: [WT(1, 0), WT(2, 0), WT(3, 0), WT(4, 0), WT(5, 0), WT(6, 0), WT(7, 0), WT(8, 0), WT(9, 0), WT(10, 0)],
        1: [WT(0, 0), WT(2, 0), WT(3, 0), WT(4, 0), WT(5, 0), WT(6, 0), WT(7, 0), WT(8, 0), WT(9, 0), WT(10, 0)],
        2: [WT(0, 0), WT(1, 0), WT(3, 0), WT(4, 0), WT(5, 0), WT(6, 0), WT(7, 0), WT(8, 0), WT(9, 0), WT(10, 0)],
        3: [WT(0, 0), WT(1, 0), WT(2, 0), WT(4, 0), WT(5, 0), WT(6, 0), WT(7, 0), WT(8, 0), WT(9, 0), WT(10, 0)],
        4: [WT(0, 0), WT(1, 0), WT(2, 0), WT(3, 0), WT(5, 0), WT(6, 0), WT(7, 0), WT(8, 0), WT(9, 0), WT(10, 0)],
        5: [WT(0, 0), WT(1, 0), WT(2, 0), WT(3, 0), WT(4, 0), WT(6, 0), WT(7, 0), WT(8, 0), WT(9, 0), WT(10, 0)],
        6: [WT(0, 0), WT(1, 0), WT(2, 0), WT(3, 0), WT(4, 0), WT(5, 0), WT(7, 0), WT(8, 0), WT(9, 0), WT(10, 0)],
        7: [WT(0, 0), WT(1, 0), WT(2, 0), WT(3, 0), WT(4, 0), WT(5, 0), WT(6, 0), WT(8, 0), WT(9, 0), WT(10, 0)],
        8: [WT(0, 0), WT(1, 0), WT(2, 0), WT(3, 0), WT(4, 0), WT(5, 0), WT(6, 0), WT(7, 0), WT(9, 0), WT(10, 0)],
        9: [WT(0, 0), WT(1, 0), WT(2, 0), WT(3, 0), WT(4, 0), WT(5, 0), WT(6, 0), WT(7, 0), WT(8, 0), WT(10, 0)],
        10: [WT(0, 0), WT(1, 0), WT(2, 0), WT(3, 0), WT(4, 0), WT(5, 0), WT(6, 0), WT(7, 0), WT(8, 0), WT(9, 0)],
    },
    # 'Map_Route_3': {
    # },
    'Map_Pewter_City': {
        0: [WT(1, 0), WT(2, 0), WT(3, 0), WT(4, 0), WT(5, 0)],
        1: [WT(0, 0), WT(2, 0), WT(3, 0), WT(4, 0), WT(5, 0)],
        2: [WT(0, 0), WT(1, 0), WT(3, 0), WT(4, 0), WT(5, 0)],
        3: [WT(0, 0), WT(1, 0), WT(2, 0), WT(4, 0), WT(5, 0)],
        4: [WT(0, 0), WT(1, 0), WT(2, 0), WT(3, 0), WT(5, 0)],
        5: [WT(0, 0), WT(1, 0), WT(2, 0), WT(3, 0), WT(4, 0)],
    },
    'Map_Route_2_Room00_00': {
        0: [WT(1, 0), WT(2, [CUT_FLAG]), WT(3, [CUT_FLAG]), WT(4, [CUT_FLAG]), WT(5, [CUT_FLAG])],
        1: [WT(0, 0), WT(2, [CUT_FLAG]), WT(3, [CUT_FLAG]), WT(4, [CUT_FLAG]), WT(5, [CUT_FLAG])],
        2: [WT(3, 0), WT(4, 0), WT(5, 0), WT(0, [CUT_FLAG]), WT(1, [CUT_FLAG])],
        3: [WT(2, 0), WT(4, 0), WT(5, 0), WT(0, [CUT_FLAG]), WT(1, [CUT_FLAG])],
        4: [WT(2, 0), WT(3, 0), WT(5, 0), WT(0, [CUT_FLAG]), WT(1, [CUT_FLAG])],
        5: [WT(2, 0), WT(3, 0), WT(4, 0), WT(0, [CUT_FLAG]), WT(1, [CUT_FLAG])],
    },
    'Map_Pallet_Town': {
        0: [WT(1, 0), WT(2, 0)],
        1: [WT(0, 0), WT(2, 0)],
        2: [WT(0, 0), WT(1, 0)],
    },
    # 'Map_Route_19': {
    # },
    # 'Map_Route_20': {
    # },
    'Map_Route_47': {
        0: [WT(1, 0)],
        1: [WT(0, 0)],
        2: [WT(6, [SURF_FLAG, ROCKCLIMB_FLAG])],
        #3: [WT(0, 0), WT(1, 0), WT(2, 0)],
        6: [WT(2, [SURF_FLAG, ROCKCLIMB_FLAG])]
    },
    'Map_Safari_Zone_Gate': {
        0: [WT(1, 0), WT(2, 0)],
        1: [WT(0, 0), WT(2, 0)],
        2: [WT(0, 0), WT(1, 0)],
    },
    'Map_Ruins_of_Alph_Room00_00': {
        0: [WT(1, 0), WT(2, 0), WT(3, 0), WT(4, 0), WT(8, 0), WT(9, 0), WT(10, 0), WT(11, 0), WT(12, 0), WT(13, 0),
            WT(14, 0), WT(5, [SURF_FLAG])],
        1: [WT(0, 0), WT(2, 0), WT(3, 0), WT(4, 0), WT(8, 0), WT(9, 0), WT(10, 0), WT(11, 0), WT(12, 0), WT(13, 0),
            WT(14, 0), WT(5, [SURF_FLAG])],
        2: [WT(0, 0), WT(1, 0), WT(3, 0), WT(4, 0), WT(8, 0), WT(9, 0), WT(10, 0), WT(11, 0), WT(12, 0), WT(13, 0),
            WT(14, 0), WT(5, [SURF_FLAG])],
        3: [WT(0, 0), WT(1, 0), WT(2, 0), WT(4, 0), WT(8, 0), WT(9, 0), WT(10, 0), WT(11, 0), WT(12, 0), WT(13, 0),
            WT(14, 0), WT(5, [SURF_FLAG])],
        4: [WT(0, 0), WT(1, 0), WT(2, 0), WT(3, 0), WT(8, 0), WT(9, 0), WT(10, 0), WT(11, 0), WT(12, 0), WT(13, 0),
            WT(14, 0), WT(5, [SURF_FLAG])],
        5: [WT(0, [SURF_FLAG]), WT(1, [SURF_FLAG]), WT(2, [SURF_FLAG]), WT(3, [SURF_FLAG]), WT(4, [SURF_FLAG]), WT(8, [SURF_FLAG]), WT(9, [SURF_FLAG]), WT(10, [SURF_FLAG]), WT(11, [SURF_FLAG]),
            WT(12, [SURF_FLAG]), WT(13, [SURF_FLAG]), WT(14, [SURF_FLAG])],
        6: [WT(5, 0), WT(15, 0), WT(0, [SURF_FLAG]), WT(1, [SURF_FLAG]), WT(2, [SURF_FLAG]), WT(3, [SURF_FLAG]), WT(4, [SURF_FLAG]), WT(8, [SURF_FLAG]), WT(9, [SURF_FLAG]),
            WT(10, [SURF_FLAG]), WT(11, [SURF_FLAG]), WT(12, [SURF_FLAG]), WT(13, [SURF_FLAG]), WT(14, [SURF_FLAG])],
        8: [WT(0, 0), WT(1, 0), WT(2, 0), WT(3, 0), WT(4, 0), WT(9, 0), WT(10, 0), WT(12, 0), WT(14, 0), WT(5, [SURF_FLAG])],
        9: [WT(0, 0), WT(1, 0), WT(2, 0), WT(3, 0), WT(4, 0), WT(8, 0), WT(10, 0), WT(11, 0), WT(13, 0), WT(5, [SURF_FLAG])],
        10: [WT(0, 0), WT(1, 0), WT(2, 0), WT(3, 0), WT(4, 0), WT(8, 0), WT(9, 0), WT(11, 0), WT(12, 0), WT(13, 0),
             WT(14, 0), WT(5, [SURF_FLAG])],
        11: [WT(0, 0), WT(1, 0), WT(2, 0), WT(3, 0), WT(4, 0), WT(9, 0), WT(10, 0), WT(12, 0), WT(14, 0), WT(5, [SURF_FLAG])],
        12: [WT(0, 0), WT(1, 0), WT(2, 0), WT(3, 0), WT(4, 0), WT(8, 0), WT(10, 0), WT(11, 0), WT(13, 0), WT(5, [SURF_FLAG])],
        13: [WT(0, 0), WT(1, 0), WT(2, 0), WT(3, 0), WT(4, 0), WT(9, 0), WT(10, 0), WT(12, 0), WT(14, 0), WT(5, [SURF_FLAG])],
        14: [WT(0, 0), WT(1, 0), WT(2, 0), WT(3, 0), WT(4, 0), WT(8, 0), WT(10, 0), WT(11, 0), WT(13, 0), WT(5, [SURF_FLAG])],
        15: [WT(5, 0), WT(6, 0), WT(0, 64), WT(1, [SURF_FLAG]), WT(2, [SURF_FLAG]), WT(3, [SURF_FLAG]), WT(4, [SURF_FLAG]), WT(8, [SURF_FLAG]), WT(9, [SURF_FLAG]),
             WT(10, [SURF_FLAG]), WT(11, [SURF_FLAG]), WT(12, [SURF_FLAG]), WT(13, [SURF_FLAG]), WT(14, [SURF_FLAG])],
    },
    'Map_Digletts_Cave_Room00_00': {
        2: [WT(3, 0), WT(4, 0), WT(5, 0)],
        3: [WT(2, 0), WT(4, 0), WT(5, 0)],
        4: [WT(2, 0), WT(3, 0), WT(5, 0)],
        5: [WT(2, 0), WT(3, 0), WT(4, 0)],
    },
    'Map_Mount_Moon_Room00_00': {
        0: [WT(1, 0), WT(2, 0), WT(5, 0)],
        1: [WT(0, 0), WT(2, 0), WT(5, 0)],
        2: [WT(0, 0), WT(1, 0), WT(5, 0)],
        3: [WT(0, 0), WT(1, 0), WT(2, 0), WT(4, 0), WT(5, 0)],
        4: [WT(0, 0), WT(1, 0), WT(2, 0), WT(3, 0), WT(5, 0)],
        5: [WT(0, 0), WT(1, 0), WT(2, 0)],
    },
    # 'Map_Mount_Moon_Room00_01': {
    # },
    'Map_Mount_Moon_Room00_02': {
        0: [WT(1, 0), WT(2, 0)],
        1: [WT(0, 0), WT(2, 0)],
        2: [WT(0, 0), WT(1, 0)],
    },
    # 'Map_Rock_Tunnel_Room00_00': {
    # },
    'Map_Rock_Tunnel_Room00_01': {
        0: [WT(1, 0), WT(4, 0), WT(5, 0)],
        1: [WT(0, 0), WT(4, 0), WT(5, 0)],
        2: [WT(3, 0), WT(6, 0), WT(7, 0)],
        3: [WT(2, 0), WT(6, 0), WT(7, 0)],
        4: [WT(0, 0), WT(1, 0), WT(5, 0)],
        5: [WT(0, 0), WT(1, 0), WT(4, 0)],
        6: [WT(2, 0), WT(3, 0), WT(7, 0)],
        7: [WT(2, 0), WT(3, 0), WT(6, 0)],
    },
    # 'Map_Pal_Park_Room00_00': {
    # },
    'Map_Sprout_Tower_Room00_00': {
        0: [WT(1, 0), WT(5, 0)],
        1: [WT(0, 0), WT(5, 0)],
        2: [WT(3, 0), WT(4, 0), WT(6, 0)],
        3: [WT(2, 0), WT(4, 0), WT(6, 0)],
        4: [WT(2, 0), WT(3, 0), WT(6, 0)],
        5: [WT(0, 0), WT(1, 0)],
        6: [WT(2, 0), WT(3, 0), WT(4, 0)],
    },
    # 'Map_Sprout_Tower_Room00_01': {
    # },
    'Map_Bell_Tower_Room00_00': {
        0: [WT(1, 0), WT(2, 0)],
        1: [WT(0, 0), WT(2, 0)],
        2: [WT(0, 0), WT(1, 0)],
    },
    'Map_Bell_Tower_Room00_01': {
        0: [WT(1, 0), WT(2, 0)],
        1: [WT(0, 0), WT(2, 0)],
        2: [WT(0, 0), WT(1, 0)],
    },
    'Map_Bell_Tower_Room00_02': {
        0: [WT(1, 0), WT(2, 0)],
        1: [WT(0, 0), WT(2, 0)],
        2: [WT(0, 0), WT(1, 0)],
    },
    'Map_Bell_Tower_Room00_03': {
        0: [WT(1, 0), WT(2, 0), WT(3, 0), WT(4, 0), WT(5, 0), WT(6, 0)],
        1: [WT(0, 0), WT(2, 0), WT(3, 0), WT(4, 0), WT(5, 0), WT(6, 0)],
        2: [WT(0, 0), WT(1, 0), WT(3, 0), WT(4, 0), WT(5, 0), WT(6, 0)],
        3: [WT(0, 0), WT(1, 0), WT(2, 0), WT(4, 0), WT(5, 0), WT(6, 0)],
        4: [WT(0, 0), WT(1, 0), WT(2, 0), WT(3, 0), WT(5, 0), WT(6, 0)],
        5: [WT(0, 0), WT(1, 0), WT(2, 0), WT(3, 0), WT(4, 0), WT(6, 0)],
        6: [WT(0, 0), WT(1, 0), WT(2, 0), WT(3, 0), WT(4, 0), WT(5, 0)],
    },
    'Map_Bell_Tower_Room00_04': {
        0: [WT(1, 0), WT(2, 0), WT(3, 0), WT(4, 0)],
        #1: [],
        #2: [],
        3: [WT(1, 0), WT(4, 0)],
        4: [WT(1, 0), WT(3, 0)],
    },
    'Map_Bell_Tower_Room00_05': {
        0: [WT(1, 0), WT(2, 0)],
        1: [WT(0, 0), WT(2, 0)],
        2: [WT(0, 0), WT(1, 0)],
    },
    'Map_Bell_Tower_Room00_06': {
        0: [WT(1, 0), WT(4, 0)],
        1: [WT(0, 0), WT(4, 0)],
        4: [WT(0, 0), WT(1, 0)],
    },
    'Map_Bell_Tower_Room00_07': {
        0: [WT(1, 0)],
        1: [WT(0, 0)],
        2: [WT(4, 0)],
        4: [WT(2, 0)],
    },
    'Map_Bell_Tower_Room00_08': {
        2: [WT(6, 0), WT(7, 0)],
        3: [WT(4, 0), WT(5, 0)],
        4: [WT(3, 0), WT(5, 0)],
        5: [WT(3, 0), WT(4, 0)],
        6: [WT(2, 0), WT(7, 0)],
        7: [WT(2, 0), WT(6, 0)],
    },
    'Map_National_Park_Room00_00': {
        0: [WT(1, 0), WT(2, 0), WT(3, 0)],
        1: [WT(0, 0), WT(2, 0), WT(3, 0)],
        2: [WT(0, 0), WT(1, 0), WT(3, 0)],
        3: [WT(0, 0), WT(1, 0), WT(2, 0)],
        5: [],
        6: [],
    },
    'Map_National_Park_Room00_01': {
        0: [WT(1, 0), WT(2, 0), WT(3, 0)],
        1: [WT(0, 0), WT(2, 0), WT(3, 0)],
        2: [WT(0, 0), WT(1, 0), WT(3, 0)],
        3: [WT(0, 0), WT(1, 0), WT(2, 0)],
        5: [WT(0, 0), WT(1, 0), WT(2, 0), WT(3, 0)],
        6: [WT(0, 0), WT(1, 0), WT(2, 0), WT(3, 0)],
    },
    'Map_Radio_Tower_Room00_01': {
        0: [WT(1, [WHIRLPOOL_FLAG])],
        1: [WT(0, 0)]
    },
    'Map_Radio_Tower_Room00_02': {
        0: [WT(1, 0), WT(2, 0)],
        1: [WT(0, 0), WT(2, 0)],
        2: [WT(0, 0), WT(1, 0)],
    },
    'Map_Radio_Tower_Room00_03': {
        0: [WT(1, 0)],
        1: [WT(0, 0)],
        2: [WT(3, 0)],
        3: [WT(4, 0)]
    },
    'Map_Radio_Tower_Room00_04': {
        1: [WT(2, 0)],
        2: [WT(1, 0)]
    },
    'Map_Union_Cave_Room00_00': {
        0: [WT(1, 0), WT(2, 0), WT(3, [SURF_FLAG])],
        1: [WT(0, 0), WT(2, 0), WT(3, [SURF_FLAG])],
        2: [WT(0, 0), WT(1, 0), WT(3, [SURF_FLAG])],
        3: [WT(0, [SURF_FLAG]), WT(1, [SURF_FLAG]), WT(2, [SURF_FLAG])],
    },
    'Map_Union_Cave_Room00_01': {
        0: [WT(3, [SURF_FLAG]), WT(4, [STRENGTH_FLAG, SURF_FLAG])],
        3: [WT(0, [SURF_FLAG]), WT(4, [STRENGTH_FLAG])],
        4: [WT(3, [STRENGTH_FLAG]), WT(0, [STRENGTH_FLAG, SURF_FLAG])],
    },
    'Map_Union_Cave_Room00_02': {
        1: [WT(3, [SURF_FLAG])],
        2: [WT(4, 0)],
        3: [WT(1, [SURF_FLAG])],
        4: [WT(2, 0)]
    },
    'Map_Slowpoke_Well_Room00_01': {
        0: [WT(1, [STRENGTH_FLAG, SURF_FLAG])],
        1: [WT(0, [STRENGTH_FLAG, SURF_FLAG])]
    },
    'Map_Lighthouse_Room00_00': {
        0: [WT(1, 0), WT(2, 0)],
        1: [WT(0, 0), WT(2, 0)],
        2: [WT(0, 0), WT(1, 0)],
    },
    'Map_Lighthouse_Room00_01': {
        0: [WT(1, 0), WT(2, 0)],
        1: [WT(0, 0), WT(2, 0)],
        2: [WT(0, 0), WT(1, 0)],
    },
    'Map_Lighthouse_Room00_03': {
        0: [WT(1, 0), WT(2, 0)],
        1: [WT(0, 0), WT(2, 0)],
        2: [WT(0, 0), WT(1, 0)],
        3: [WT(4, 0), WT(5, 0)],
        4: [WT(3, 0), WT(5, 0)],
        5: [WT(3, 0), WT(4, 0)],
    },
    'Map_Lighthouse_Room00_04': {
        1: [WT(2, 0), WT(3, 0)],
        2: [WT(1, 0), WT(3, 0)],
        3: [WT(1, 0), WT(2, 0)],
    },
    'Map_Lighthouse_Room00_05': {
        0: [WT(1, 0), WT(2, 0)],
        1: [WT(0, 0), WT(2, 0)],
        2: [WT(0, 0), WT(1, 0)],
    },
    'Map_Team_Rocket_HQ_Room00_02': {
        0: [WT(1, 0)],
        1: [WT(0, 0)],
        3: [WT(4, 0)],
        4: [WT(3, 0)]
    },
    'Map_Team_Rocket_HQ_Room00_03': {
        0: [WT(3, 0)],
        1: [WT(2, 0)],
        2: [WT(1, 0)],
        3: [WT(0, 0)]
    },
    'Map_Ilex_Forest_Room00_00': {
        0: [WT(1, 0), WT(2, [CUT_FLAG]), WT(3, [CUT_FLAG]), WT(4, [CUT_FLAG]), WT(5, [CUT_FLAG])],
        1: [WT(0, 0), WT(2, [CUT_FLAG]), WT(3, [CUT_FLAG]), WT(4, [CUT_FLAG]), WT(5, [CUT_FLAG])],
        2: [WT(0, [CUT_FLAG]), WT(1, [CUT_FLAG]), WT(3, 0), WT(4, 0), WT(5, 0)],
        3: [WT(0, [CUT_FLAG]), WT(1, [CUT_FLAG]), WT(2, 0), WT(4, 0), WT(5, 0)],
        4: [WT(0, [CUT_FLAG]), WT(1, [CUT_FLAG]), WT(2, 0), WT(3, 0), WT(5, 0)],
        5: [WT(0, [CUT_FLAG]), WT(1, [CUT_FLAG]), WT(2, 0), WT(3, 0), WT(4, 0)],
    },
    'Map_Goldenrod_Tunnel_Room00_00': {
        0: [WT(2, 0), WT(6, 0), WT(7, 0)],
        1: [WT(3, 0), WT(8, 0), WT(9, 0)],
        2: [WT(0, 0), WT(6, 0), WT(7, 0)],
        3: [WT(1, 0), WT(8, 0), WT(9, 0)],
        4: [WT(5, 0)], #4 and 5 to hideout
        5: [WT(4, 0)],
        6: [WT(0, 0), WT(2, 0), WT(7, 0)],
        7: [WT(0, 0), WT(2, 0), WT(6, 0)],
        8: [WT(1, 0), WT(3, 0), WT(9, 0)],
        9: [WT(1, 0), WT(3, 0), WT(8, 0)],
    },
    'Map_Goldenrod_Tunnel_Room00_01': { #warp 6 is blocked by radiotower_1 in one direction, so im giving 1024 since it unlocks during event after beating petrel
        0: [WT(1, 0), WT(2, 0), WT(4, 0), WT(5, 0), WT(6, [RADIOTOWER2_FLAG])],
        1: [WT(0, 0), WT(2, 0), WT(4, 0), WT(5, 0), WT(6, [RADIOTOWER2_FLAG])],
        2: [WT(0, 0), WT(1, 0), WT(4, 0), WT(5, 0), WT(6, [RADIOTOWER2_FLAG])],
        4: [WT(0, 0), WT(1, 0), WT(2, 0), WT(5, 0), WT(6, [RADIOTOWER2_FLAG])],
        5: [WT(0, 0), WT(1, 0), WT(2, 0), WT(4, 0), WT(6, [RADIOTOWER2_FLAG])],
        6: [WT(0, 0), WT(1, 0), WT(2, 0), WT(4, 0), WT(5, 0)],
    },
    'Map_Goldenrod_City_Room00_02': {
        0: [WT(1, [RADIOTOWER2_FLAG])],
        1: [WT(0, [RADIOTOWER2_FLAG])]
    },
     'Map_Mount_Mortar_Room00_00': {  # todo fix this
        0: [WT(4, 0)],
        1: [WT(10, 0), WT(9,[SURF_FLAG, WATERFALL_FLAG])],
        2: [WT(6, 0), WT(5, 0), WT(3, 0)],
        3: [WT(5, 0), WT(2, [ROCKCLIMB_FLAG]), WT(6, [ROCKCLIMB_FLAG])],
        4: [WT(0, 0)],
        5: [WT(3, 0), WT(2, [ROCKCLIMB_FLAG]), WT(6, [ROCKCLIMB_FLAG])],
        6: [WT(2, 0), WT(5, [ROCKCLIMB_FLAG]), WT(3, [ROCKCLIMB_FLAG])],
        7: [],
        8: [],
        9: [WT(1, [SURF_FLAG, WATERFALL_FLAG]), WT(10, [SURF_FLAG, WATERFALL_FLAG])],
        10: [WT(1, 0), WT(9, [SURF_FLAG, WATERFALL_FLAG])],
     },
    'Map_Mount_Mortar_Room00_01': {
        0: [WT(1, 0), WT(3, 0), WT(4, 0), WT(5, 0), WT(6, 0)],
        1: [WT(0, 0), WT(3, 0), WT(4, 0), WT(5, 0), WT(6, 0)],
        3: [WT(0, 0), WT(1, 0), WT(4, 0), WT(5, 0), WT(6, 0)],
        4: [WT(0, 0), WT(1, 0), WT(3, 0), WT(5, 0), WT(6, 0)],
        5: [WT(0, 0), WT(1, 0), WT(3, 0), WT(4, 0), WT(6, 0)],
        6: [WT(0, 0), WT(1, 0), WT(3, 0), WT(4, 0), WT(5, 0)],
        7: [WT(0, 0), WT(1, 0), WT(3, 0), WT(4, 0), WT(5, 0), WT(6, 0), WT(8, 0), WT(9, 0)],
        8: [WT(0, 0), WT(1, 0), WT(3, 0), WT(4, 0), WT(5, 0), WT(6, 0), WT(7, 0), WT(9, 0)],
        9: [WT(0, 0), WT(1, 0), WT(3, 0), WT(4, 0), WT(5, 0), WT(6, 0), WT(7, 0), WT(8, 0)],
    },
     'Map_Mount_Mortar_Room00_02': {
        0: [WT(1, [SURF_FLAG])],
        1: [WT(0, 0)],
     },
    'Map_Mount_Mortar_Room00_03': {
        0: [WT(3, 0), WT(1, [STRENGTH_FLAG, SURF_FLAG]), WT(2, [STRENGTH_FLAG, SURF_FLAG])],
        1: [WT(2, 0), WT(0, [STRENGTH_FLAG, SURF_FLAG]), WT(3, [STRENGTH_FLAG, SURF_FLAG])],
        2: [WT(1, 0), WT(0, [STRENGTH_FLAG, SURF_FLAG]), WT(3, [STRENGTH_FLAG, SURF_FLAG])],
        3: [WT(0, 0), WT(1, [STRENGTH_FLAG, SURF_FLAG]), WT(2, [STRENGTH_FLAG, SURF_FLAG])],
    },
    'Map_Route_26_Room00_00': { #here
        0: [WT(1, 0), WT(2, 0), WT(3, [ROCKCLIMB_FLAG])],
        1: [WT(0, 0), WT(2, 0), WT(3, [ROCKCLIMB_FLAG])],
        2: [WT(0, 0), WT(1, 0), WT(3, [ROCKCLIMB_FLAG])],
        3: [WT(0, 0), WT(1, 0), WT(2, 0)],
    },
    'Map_Bellchime_Trail_Room10_00': {
        0: [WT(1, 0), WT(2, 0)],
        1: [WT(0, 0), WT(2, 0)],
        2: [WT(0, 0), WT(1, 0)],
    },
    'Map_Ecruteak_City_Room01_00': { #surf as requirement?
        0: [WT(1, [SURF_FLAG])],
        1: [WT(0, 0)]
    },
    'Map_Ecruteak_City_PokemonCenter00_00': {
        0: [WT(2, 0)],
        2: [WT(0, 0)],
    },
    'Map_Cerulean_Cave_Room00_00': {
        0: [WT(1, [SURF_FLAG]), WT(3, [SURF_FLAG]), WT(4, [SURF_FLAG]), WT(6, [SURF_FLAG]), WT(8, [SURF_FLAG]), WT(9, [SURF_FLAG]), WT(10, [SURF_FLAG]), WT(11, [SURF_FLAG]), WT(13, [SURF_FLAG]),
            WT(14, [SURF_FLAG])],
        1: [WT(9, 0), WT(0, [SURF_FLAG]), WT(3, [SURF_FLAG]), WT(4, [SURF_FLAG]), WT(6, [SURF_FLAG]), WT(8, [SURF_FLAG]), WT(10, [SURF_FLAG]), WT(11, [SURF_FLAG]), WT(13, [SURF_FLAG]),
            WT(14, [SURF_FLAG])],
        2: [WT(0, [SURF_FLAG]), WT(1, [SURF_FLAG]), WT(3, [SURF_FLAG]), WT(4, [SURF_FLAG]), WT(6, [SURF_FLAG]), WT(8, [SURF_FLAG]), WT(9, [SURF_FLAG]), WT(10, [SURF_FLAG]), WT(11, [SURF_FLAG]),
            WT(13, [SURF_FLAG]), WT(14, [SURF_FLAG])],
        3: [WT(0, 0), WT(4, 0), WT(6, 0), WT(8, 0), WT(10, 0), WT(11, 0), WT(13, 0), WT(14, 0), WT(1, [SURF_FLAG]), WT(9, [SURF_FLAG])],
        4: [WT(0, 0), WT(3, 0), WT(6, 0), WT(8, 0), WT(10, 0), WT(11, 0), WT(13, 0), WT(14, 0), WT(1, [SURF_FLAG]), WT(9, [SURF_FLAG])],
        5: [WT(7, 0), WT(12, 0)],
        6: [WT(0, 0), WT(3, 0), WT(4, 0), WT(8, 0), WT(10, 0), WT(11, 0), WT(13, 0), WT(14, 0), WT(1, [SURF_FLAG]), WT(9, [SURF_FLAG])],
        7: [WT(5, 0), WT(12, 0)],
        8: [WT(0, 0), WT(3, 0), WT(4, 0), WT(6, 0), WT(10, 0), WT(11, 0), WT(13, 0), WT(14, 0), WT(1, 64), WT(9, [SURF_FLAG])],
        9: [WT(1, 0), WT(0, [SURF_FLAG]), WT(3, [SURF_FLAG]), WT(4, [SURF_FLAG]), WT(6, [SURF_FLAG]), WT(8, [SURF_FLAG]), WT(10, [SURF_FLAG]), WT(11, [SURF_FLAG]), WT(13, [SURF_FLAG]),
            WT(14, [SURF_FLAG])],
        10: [WT(0, 0), WT(3, 0), WT(4, 0), WT(6, 0), WT(8, 0), WT(11, 0), WT(13, 0), WT(14, 0), WT(1, [SURF_FLAG]), WT(9, [SURF_FLAG])],
        11: [WT(0, 0), WT(3, 0), WT(4, 0), WT(6, 0), WT(8, 0), WT(10, 0), WT(13, 0), WT(14, 0), WT(1, [SURF_FLAG]), WT(9, [SURF_FLAG])],
        12: [WT(5, 0), WT(7, 0)],
        13: [WT(0, 0), WT(3, 0), WT(4, 0), WT(6, 0), WT(8, 0), WT(10, 0), WT(11, 0), WT(14, 0), WT(1, [SURF_FLAG]), WT(9, [SURF_FLAG])],
        14: [WT(0, 0), WT(3, 0), WT(4, 0), WT(6, 0), WT(8, 0), WT(10, 0), WT(11, 0), WT(13, 0), WT(1, [SURF_FLAG]), WT(9, [SURF_FLAG])],
    },
    'Map_Cerulean_Cave_Room00_01': {
        0: [WT(5, 0)],
        1: [],
        2: [],
        3: [],
        4: [],
        5: [WT(0, 0)]
     },
    'Map_Cerulean_Cave_Room00_02': {
        0: [WT(3, 0), WT(1, [SURF_FLAG]), WT(2, [SURF_FLAG])],
        1: [WT(2, 0), WT(0, [SURF_FLAG]), WT(3, [SURF_FLAG])],
        2: [WT(1, 0), WT(0, [SURF_FLAG]), WT(3, [SURF_FLAG])],
        3: [WT(0, 0), WT(1, [SURF_FLAG]), WT(2, [SURF_FLAG])],
    },
    'Map_Seafoam_Islands_Room00_00': {
        0: [WT(2, 0), WT(4, 0), WT(5, 0)],
        2: [WT(0, 0), WT(4, 0), WT(5, 0)],
        4: [WT(0, 0), WT(2, 0), WT(5, 0)],
        5: [WT(0, 0), WT(2, 0), WT(4, 0)],
    },
    'Map_Seafoam_Islands_Room00_01': { #here
        0: [WT(1, [STRENGTH_FLAG]), WT(2, [STRENGTH_FLAG]), WT(3, [STRENGTH_FLAG]), WT(4, [STRENGTH_FLAG]), WT(5, [STRENGTH_FLAG])],
        1: [WT(0, [STRENGTH_FLAG]), WT(2, [STRENGTH_FLAG]), WT(3, [STRENGTH_FLAG]), WT(4, [STRENGTH_FLAG]), WT(5, [STRENGTH_FLAG])],
        2: [WT(3, 0), WT(4, 0), WT(0, [STRENGTH_FLAG]), WT(1, [STRENGTH_FLAG]), WT(5, [STRENGTH_FLAG])],
        3: [WT(2, 0), WT(4, 0), WT(0, [STRENGTH_FLAG]), WT(1, [STRENGTH_FLAG]), WT(5, [STRENGTH_FLAG])],
        4: [WT(2, 0), WT(3, 0), WT(0, [STRENGTH_FLAG]), WT(1, [STRENGTH_FLAG]), WT(5, [STRENGTH_FLAG])],
        5: [WT(0, [STRENGTH_FLAG]), WT(1, [STRENGTH_FLAG]), WT(2, [STRENGTH_FLAG]), WT(3, [STRENGTH_FLAG]), WT(4, [STRENGTH_FLAG])],
    },
    'Map_Seafoam_Islands_Room00_02': {
        1: [WT(0, 0), WT(8, 0), WT(10, 0)],
        2: [WT(0, 0), WT(4, 0), WT(5, 0), WT(6, 0), WT(8, 0), WT(9, 0)],
        3: [WT(7, 0), WT(11, 0)],
        4: [WT(0, 0), WT(2, 0), WT(5, 0), WT(6, 0), WT(8, 0), WT(9, 0)],
        5: [WT(0, 0), WT(2, 0), WT(4, 0), WT(6, 0), WT(8, 0), WT(9, 0)],
        6: [WT(0, 0), WT(2, 0), WT(4, 0), WT(5, 0), WT(8, 0), WT(9, 0)],
        7: [WT(3, 0), WT(11, 0)],
        9: [WT(0, 0), WT(2, 0), WT(4, 0), WT(5, 0), WT(6, 0), WT(8, 0)],
        10: [WT(0, 0), WT(1, 0), WT(8, 0)],
        11: [WT(3, 0), WT(7, 0)],
    },
    'Map_Seafoam_Islands_Room00_03': {
        0: [WT(5, 0), WT(6, 0), WT(8, 0), WT(11, 0)],
        1: [WT(4, 0), WT(10, 0)],
        2: [WT(7, 0), WT(12, 0)],
        3: [WT(9, 0), WT(13, 0)],
        4: [WT(1, 0), WT(10, 0)],
        5: [WT(0, 0), WT(6, 0), WT(8, 0), WT(11, 0)],
        6: [WT(0, 0), WT(5, 0), WT(8, 0), WT(11, 0)],
        7: [WT(2, 0), WT(12, 0)],
        8: [WT(0, 0), WT(5, 0), WT(6, 0), WT(11, 0)],
        9: [WT(3, 0), WT(13, 0)],
        10: [WT(1, 0), WT(4, 0)],
        11: [WT(0, 0), WT(5, 0), WT(6, 0), WT(8, 0)],
        12: [WT(2, 0), WT(7, 0)],
        13: [WT(3, 0), WT(9, 0)],
    },
    'Map_Seafoam_Islands_Room00_04': {
        0: [WT(11, 0), WT(5, [SURF_FLAG]), WT(10, [SURF_FLAG])],
        3: [WT(8, 0), WT(4, [SURF_FLAG]), WT(9, [SURF_FLAG])],
        4: [WT(9, 0), WT(3, [SURF_FLAG]), WT(8, [SURF_FLAG])],
        5: [WT(10, 0), WT(0, [SURF_FLAG]), WT(11, [SURF_FLAG])],
        8: [WT(3, 0), WT(4, [SURF_FLAG]), WT(9, [SURF_FLAG])],
        9: [WT(4, 0), WT(3, [SURF_FLAG]), WT(8, [SURF_FLAG])],
        10: [WT(5, 0), WT(0, [SURF_FLAG]), WT(11, [SURF_FLAG])],
        11: [WT(0, 0), WT(5, [SURF_FLAG]), WT(10, [SURF_FLAG])],
    },
    'Map_Viridian_Forest_Room00_00': {
        0: [WT(1, 0), WT(2, 0), WT(3, 0), WT(4, 0), WT(5, 0)],
        1: [WT(0, 0), WT(2, 0), WT(3, 0), WT(4, 0), WT(5, 0)],
        2: [WT(0, 0), WT(1, 0), WT(3, 0), WT(4, 0), WT(5, 0)],
        3: [WT(0, 0), WT(1, 0), WT(2, 0), WT(4, 0), WT(5, 0)],
        4: [WT(0, 0), WT(1, 0), WT(2, 0), WT(3, 0), WT(5, 0)],
        5: [WT(0, 0), WT(1, 0), WT(2, 0), WT(3, 0), WT(4, 0)],
    },
    # 'Map_Dark_Cave_Room00_00': {
    # },
    'Map_Dark_Cave_Room00_01': {
        0: [WT(1, [SURF_FLAG]), WT(2, [STRENGTH_FLAG, SURF_FLAG])],
        1: [WT(0, [SURF_FLAG]), WT(2, [STRENGTH_FLAG, SURF_FLAG])],
        2: [WT(0, [ROCKSMASH_FLAG, STRENGTH_FLAG]), WT(1, [ROCKSMASH_FLAG, STRENGTH_FLAG, SURF_FLAG])],
    },
    # commenting for test
    #'Map_Goldenrod_City_Room04_00': {
    #    0: [WT(1, 0), WT(2, 0)],
    #},
    'Map_Goldenrod_City_Room09_00': {
        0: [WT(1, 0), WT(2, 0)],
        1: [WT(0, 0), WT(2, 0)],
        2: [WT(0, 0), WT(1, 0)],
    },
    'Map_Goldenrod_City_Room09_01': {
        0: [WT(1, 0), WT(2, 0)],
        1: [WT(0, 0), WT(2, 0)],
        2: [WT(0, 0), WT(1, 0)],
    },
    'Map_Goldenrod_City_Room09_02': {
        0: [WT(1, 0), WT(2, 0)],
        1: [WT(0, 0), WT(2, 0)],
        2: [WT(0, 0), WT(1, 0)],
    },
    'Map_Goldenrod_City_Room09_03': {
        0: [WT(1, 0), WT(2, 0)],
        1: [WT(0, 0), WT(2, 0)],
        2: [WT(0, 0), WT(1, 0)],
    },
    'Map_Goldenrod_City_Room09_04': {
        0: [WT(1, 0), WT(2, 0)],
        1: [WT(0, 0), WT(2, 0)],
        2: [WT(0, 0), WT(1, 0)],
    },
    'Map_Ice_Path_Room00_00': {
        0: [WT(2, 0)],
        1: [WT(3, 0)],
        2: [WT(0, 0)],
        3: [WT(1, 0)]
    },
    'Map_Ice_Path_Room00_01': {
        0: [WT(1, 0), WT(2, 0)],
        1: [WT(0, 0), WT(2, 0)],
        2: [WT(0, 0), WT(1, 0)],
        3: [WT(4, 0), WT(5, 0)],
        4: [WT(3, 0), WT(5, 0)],
        5: [WT(3, 0), WT(4, 0)],
    },
    'Map_Ice_Path_Room00_02': {
        0: [WT(1, 0), WT(2, 0)],
        1: [WT(0, 0), WT(2, 0)],
        2: [WT(0, 0), WT(1, 0)],
        3: [WT(4, 0), WT(5, 0)],
        4: [WT(3, 0), WT(5, 0)],
        5: [WT(3, 0), WT(4, 0)],
    },
    'Map_Ice_Path_Room00_03': {
        0: [WT(1, 0), WT(2, 0), WT(3, 0)],
        1: [WT(0, 0), WT(2, 0), WT(3, 0)],
        2: [WT(0, 0), WT(1, 0), WT(3, 0)],
        3: [WT(0, 0), WT(1, 0), WT(2, 0)],
    },
    'Map_Olivine_City_Room00_00': {
        0: [WT(2, 0)],
        2: [WT(0, 0)],
    },
    'Map_Mahogany_Town_Room00_00': {
        0: [WT(1, [LAKEOFRAGE_FLAG])],
        1: [WT(0, 0)]
    },
    'Map_Whirl_Islands_Room00_00': {
        0: [WT(1, 0), WT(2, 0)],
        5: [WT(6, 0), WT(7, [SURF_FLAG])],
        6: [WT(5, 0), WT(7, [SURF_FLAG])],
        7: [WT(5, [SURF_FLAG]), WT(6, [SURF_FLAG])],
    },
    'Map_Whirl_Islands_Room00_01': {
        0: [WT(1, 0), WT(2, 0), WT(3, 0), WT(4, 0), WT(5, 0), WT(6, 0), WT(9, [STRENGTH_FLAG]), WT(10, [STRENGTH_FLAG]), WT(12, [STRENGTH_FLAG]), WT(13, [STRENGTH_FLAG])],
        1: [WT(0, 0), WT(2, 0), WT(3, 0), WT(4, 0), WT(5, 0), WT(6, 0), WT(9, [STRENGTH_FLAG]), WT(10, [STRENGTH_FLAG]), WT(12, [STRENGTH_FLAG]), WT(13, [STRENGTH_FLAG])],
        2: [WT(3, 0), WT(9, [STRENGTH_FLAG]), WT(10, [STRENGTH_FLAG]), WT(12, [STRENGTH_FLAG]), WT(13, [STRENGTH_FLAG])],
        3: [WT(2, 0), WT(9, [STRENGTH_FLAG]), WT(10, [STRENGTH_FLAG]), WT(12, [STRENGTH_FLAG]), WT(13, [STRENGTH_FLAG])],
        4: [WT(0, 0), WT(1, 0), WT(2, 0), WT(3, 0), WT(5, 0), WT(6, 0), WT(9, [STRENGTH_FLAG]), WT(10, [STRENGTH_FLAG]), WT(12, [STRENGTH_FLAG]), WT(13, [STRENGTH_FLAG])],
        5: [WT(0, 0), WT(1, 0), WT(2, 0), WT(3, 0), WT(4, 0), WT(6, 0), WT(9, [STRENGTH_FLAG]), WT(10, [STRENGTH_FLAG]), WT(12, [STRENGTH_FLAG]), WT(13, [STRENGTH_FLAG])],
        6: [WT(0, 0), WT(1, 0), WT(2, 0), WT(3, 0), WT(4, 0), WT(5, 0), WT(9, [STRENGTH_FLAG]), WT(10, [STRENGTH_FLAG]), WT(12, [STRENGTH_FLAG]), WT(13, [STRENGTH_FLAG])],
        7: [WT(2, 0), WT(3, 0), WT(8, 0), WT(11, 0), WT(9, [STRENGTH_FLAG]), WT(10, [STRENGTH_FLAG]), WT(12, [STRENGTH_FLAG]), WT(13, [STRENGTH_FLAG])],
        8: [WT(2, 0), WT(3, 0), WT(7, 0), WT(11, 0), WT(9, [STRENGTH_FLAG]), WT(10, [STRENGTH_FLAG]), WT(12, [STRENGTH_FLAG]), WT(13, [STRENGTH_FLAG])],
        9: [WT(10, 0), WT(12, 0), WT(13, 0), WT(2, [STRENGTH_FLAG]), WT(3, [STRENGTH_FLAG])],
        10: [WT(9, 0), WT(12, 0), WT(13, 0), WT(2, [STRENGTH_FLAG]), WT(3, [STRENGTH_FLAG])],
        11: [WT(2, 0), WT(3, 0), WT(7, 0), WT(8, 0), WT(9, [STRENGTH_FLAG]), WT(10, [STRENGTH_FLAG]), WT(12, [STRENGTH_FLAG]), WT(13, [STRENGTH_FLAG])],
        12: [WT(9, 0), WT(10, 0), WT(13, 0), WT(2, [STRENGTH_FLAG]), WT(3, [STRENGTH_FLAG])],
        13: [WT(9, 0), WT(10, 0), WT(12, 0), WT(2, [STRENGTH_FLAG]), WT(3, [STRENGTH_FLAG])],
    },
    'Map_Whirl_Islands_Room00_03': {
        2: [WT(3, 0), WT(4, 0), WT(5, 0)],
        3: [WT(2, 0), WT(4, 0), WT(5, 0)],
        4: [WT(2, 0), WT(3, 0), WT(5, 0)],
        5: [WT(2, 0), WT(3, 0), WT(4, 0)],
    },
    'Map_Dragons_Den_Room00_01': {
        0: [WT(1, 0), WT(2, [SURF_FLAG, WHIRLPOOL_FLAG])],
        1: [WT(0, 0), WT(2, [SURF_FLAG, WHIRLPOOL_FLAG])],
        2: [WT(0, [SURF_FLAG, WHIRLPOOL_FLAG]), WT(1, [SURF_FLAG, WHIRLPOOL_FLAG])],
    },
    'Map_Pokemon_League_Room00_00': {
        0: [WT(1, 0), WT(2, 0)],
        1: [WT(0, 0), WT(2, 0)],
        2: [WT(0, 0), WT(1, 0)],
    },
    'Map_Tohjo_Falls_Room00_00': {
        0: [WT(1, [SURF_FLAG, WATERFALL_FLAG]), WT(2, [SURF_FLAG, WATERFALL_FLAG])],
        1: [WT(0, [SURF_FLAG, WATERFALL_FLAG]), WT(2, [SURF_FLAG, WATERFALL_FLAG])],
        2: [WT(0, [SURF_FLAG, WATERFALL_FLAG]), WT(1, [SURF_FLAG, WATERFALL_FLAG])],
    },
    # 'Map_Cliff_Edge_Gate_Room00_00': {
    # },
    'Map_Pokeathlon_Dome': {
        0: [WT(1, 0), WT(2, 0), WT(3, 0)],
        1: [WT(0, 0), WT(2, 0), WT(3, 0)],
        2: [WT(0, 0), WT(1, 0), WT(3, 0)],
        3: [WT(0, 0), WT(1, 0), WT(2, 0)],
    },
    'Map_Pokeathlon_Dome_Room00_00': {
        0: [WT(1, 0), WT(2, 0)],
        1: [WT(0, 0), WT(2, 0)],
        2: [WT(0, 0), WT(1, 0)],
    },
    'Map_Victory_Road_Room00_00': {
        0: [WT(1, [STRENGTH_FLAG]), WT(2, [STRENGTH_FLAG])],
        1: [WT(2, 0), WT(0, [STRENGTH_FLAG])],
        2: [WT(1, 0), WT(0, [STRENGTH_FLAG])],
    },
    'Map_Victory_Road_Room00_01': {
        0: [WT(3, 0), WT(4, 0), WT(7, [STRENGTH_FLAG]), WT(8, [STRENGTH_FLAG])],
        3: [WT(0, 0), WT(4, 0), WT(7, [STRENGTH_FLAG]), WT(8, [STRENGTH_FLAG])],
        4: [WT(0, 0), WT(3, 0), WT(7, [STRENGTH_FLAG]), WT(8, [STRENGTH_FLAG])],
        5: [WT(6, 0), WT(0, [STRENGTH_FLAG]), WT(3, [STRENGTH_FLAG]), WT(4, [STRENGTH_FLAG]), WT(7, [STRENGTH_FLAG]), WT(8, [STRENGTH_FLAG])],
        6: [WT(5, 0), WT(0, [STRENGTH_FLAG]), WT(3, [STRENGTH_FLAG]), WT(4, [STRENGTH_FLAG]), WT(7, [STRENGTH_FLAG]), WT(8, [STRENGTH_FLAG])],
        7: [WT(8, 0), WT(0, [STRENGTH_FLAG]), WT(3, [STRENGTH_FLAG]), WT(4, [STRENGTH_FLAG])],
        8: [WT(7, 0), WT(0, [STRENGTH_FLAG]), WT(3, [STRENGTH_FLAG]), WT(4, [STRENGTH_FLAG])],
    },
    'Map_Victory_Road_Room00_02': {
        0: [WT(1, 0), WT(5, 0)],
        1: [WT(0, 0), WT(5, 0)],
        4: [WT(0, 0), WT(1, 0), WT(5, 0)],
        5: [WT(0, 0), WT(1, 0)],
    },
    'Map_Pokemon_League_Room01_00': {
        0: [WT(1, 0), WT(2, 0), WT(3, 0)],
        1: [WT(2, 0), WT(3, 0)],
        2: [WT(1, 0), WT(3, 0)],
        3: [WT(1, 0), WT(2, 0)],
    },
    'Map_Pokemon_League_Room02_00': {
        0: [WT(1, 0), WT(2, 0), WT(3, 0)],
        1: [WT(2, 0), WT(3, 0)],
        2: [WT(1, 0), WT(3, 0)],
        3: [WT(1, 0), WT(2, 0)],
    },
    'Map_Pokemon_League_Room03_00': {
        0: [WT(1, 0), WT(2, 0), WT(3, 0)],
        1: [WT(2, 0), WT(3, 0)],
        2: [WT(1, 0), WT(3, 0)],
        3: [WT(1, 0), WT(2, 0)],
    },
    'Map_Pokemon_League_Room04_00': {
        0: [WT(1, 0), WT(2, 0), WT(3, 0)],
        1: [WT(2, 0), WT(3, 0)],
        2: [WT(1, 0), WT(3, 0)],
        3: [WT(1, 0), WT(2, 0)],
    },
    'Map_Pokemon_League_Room05_00': {
        0: [WT(1, 0)],
        1: []
    },
    'Map_SS_Aqua_Room02_00': {
        0: [WT(1, 0), WT(2, 0), WT(3, 0), WT(4, 0), WT(5, 0), WT(6, 0), WT(7, 0), WT(8, 0), WT(9, 0)],
        1: [WT(0, 0), WT(2, 0), WT(3, 0), WT(4, 0), WT(5, 0), WT(6, 0), WT(7, 0), WT(8, 0), WT(9, 0), WT(12, 0)],
        2: [WT(0, 0), WT(1, 0), WT(3, 0), WT(4, 0), WT(5, 0), WT(6, 0), WT(7, 0), WT(8, 0), WT(9, 0), WT(12, 0)],
        3: [WT(0, 0), WT(1, 0), WT(2, 0), WT(4, 0), WT(5, 0), WT(6, 0), WT(7, 0), WT(8, 0), WT(9, 0), WT(12, 0)],
        4: [WT(0, 0), WT(1, 0), WT(2, 0), WT(3, 0), WT(5, 0), WT(6, 0), WT(7, 0), WT(8, 0), WT(9, 0), WT(12, 0)],
        5: [WT(0, 0), WT(1, 0), WT(2, 0), WT(3, 0), WT(4, 0), WT(6, 0), WT(7, 0), WT(8, 0), WT(9, 0), WT(12, 0)],
        6: [WT(0, 0), WT(1, 0), WT(2, 0), WT(3, 0), WT(4, 0), WT(5, 0), WT(7, 0), WT(8, 0), WT(9, 0), WT(12, 0)],
        7: [WT(0, 0), WT(1, 0), WT(2, 0), WT(3, 0), WT(4, 0), WT(5, 0), WT(6, 0), WT(8, 0), WT(9, 0), WT(12, 0)],
        8: [WT(0, 0), WT(1, 0), WT(2, 0), WT(3, 0), WT(4, 0), WT(5, 0), WT(6, 0), WT(7, 0), WT(9, 0), WT(12, 0)],
        9: [WT(0, 0), WT(1, 0), WT(2, 0), WT(3, 0), WT(4, 0), WT(5, 0), WT(6, 0), WT(7, 0), WT(8, 0), WT(12, 0)],
        12: [WT(1, 0), WT(2, 0), WT(3, 0), WT(4, 0), WT(5, 0), WT(6, 0), WT(7, 0), WT(8, 0), WT(9, 0)],
    },
    # 'Map_SS_Aqua_Room02_02': {
    # },
    # 'Map_SS_Aqua_Room02_03': {
    # },
    # 'Map_SS_Aqua_Room02_04': {
    # },
    # 'Map_SS_Aqua_Room02_05': {
    # },
    'Map_SS_Aqua_Room02_06': {
        0: [WT(1, 0), WT(2, 0)],
        1: [WT(0, 0), WT(2, 0)],
        2: [WT(0, 0), WT(1, 0)],
    },
    'Map_Olivine_City_Room00_01': {
        0: [WT(1, 0)],
        1: [WT(0, 0)]
    },
    'Map_Ruins_of_Alph_Room01_10': {
        0: [WT(1, 0)],
        1: [WT(0, 0)],
        2: [WT(3, 0)],
        3: [WT(2, 0)]
    },
    'Map_Bell_Tower_Room00_11': {
        0: [WT(1, 0), WT(2, 0)],
        1: [WT(0, 0), WT(2, 0)],
        2: [WT(0, 0), WT(1, 0)],
    },
    'Map_Cliff_Cave_Room00_00': {
        0: [WT(3, 0), WT(4, 0), WT(6, 0)],
        1: [WT(7, 0), WT(8, 0)],
        3: [WT(0, 0), WT(4, 0), WT(6, 0)],
        4: [WT(0, 0), WT(3, 0), WT(6, 0)],
        6: [WT(0, 0), WT(3, 0), WT(4, 0)],
        7: [WT(1, 0), WT(8, 0)],
        8: [WT(1, 0), WT(7, 0)],
    },
    # 'Map_Vermilion_City_Room00_02': {
    # },
    #test for station
    #'Map_Saffron_City_Room05_00': {
    #    0: [WT(1, 0), WT(2, 0)],
    #    1: [WT(0, 0), WT(2, 0)],
    #    2: [WT(0, 0), WT(1, 0)],
    #},
    # 'Map_Saffron_City_Room06_00': {
    # },
    'Map_Route_35_Room01_00': {
        0: [WT(1, 0), WT(2, 0)],
        1: [WT(0, 0), WT(2, 0)],
        2: [WT(0, 0), WT(1, 0)],
    },
    'Map_Celadon_City_Room00_00': {
        0: [WT(1, 0), WT(2, 0)],
        1: [WT(0, 0), WT(2, 0)],
        2: [WT(0, 0), WT(1, 0)],
    },
    'Map_Celadon_City_Room00_01': {
        0: [WT(1, 0), WT(2, 0)],
        1: [WT(0, 0), WT(2, 0)],
        2: [WT(0, 0), WT(1, 0)],
    },
    'Map_Celadon_City_Room00_02': {
        0: [WT(1, 0), WT(2, 0)],
        1: [WT(0, 0), WT(2, 0)],
        2: [WT(0, 0), WT(1, 0)],
    },
    'Map_Celadon_City_Room00_03': {
        0: [WT(1, 0), WT(2, 0)],
        1: [WT(0, 0), WT(2, 0)],
        2: [WT(0, 0), WT(1, 0)],
    },
    'Map_Celadon_City_Room00_04': {
        0: [WT(1, 0), WT(2, 0)],
        1: [WT(0, 0), WT(2, 0)],
        2: [WT(0, 0), WT(1, 0)],
    },
    'Map_Celadon_City_Room01_00': {
        0: [WT(1, 0), WT(2, 0)],
        1: [WT(0, 0), WT(2, 0)],
        2: [WT(0, 0), WT(1, 0)],
    },
    'Map_Celadon_City_Room01_03': {
        0: [WT(2, 0)],
        2: [WT(0, 0)]
    },
    'Map_Battle_Frontier': {
        0: [WT(1, 0), WT(2, 0), WT(3, 0), WT(4, 0), WT(5, 0), WT(6, 0), WT(7, 0), WT(8, 0), WT(9, 0), WT(10, 0),
            WT(11, 0), WT(12, 0), WT(13, 0), WT(14, 0), WT(15, 0)],
        1: [WT(0, 0), WT(2, 0), WT(3, 0), WT(4, 0), WT(5, 0), WT(6, 0), WT(7, 0), WT(8, 0), WT(9, 0), WT(10, 0),
            WT(11, 0), WT(12, 0), WT(13, 0), WT(14, 0), WT(15, 0)],
        2: [WT(0, 0), WT(1, 0), WT(3, 0), WT(4, 0), WT(5, 0), WT(6, 0), WT(7, 0), WT(8, 0), WT(9, 0), WT(10, 0),
            WT(11, 0), WT(12, 0), WT(13, 0), WT(14, 0), WT(15, 0)],
        3: [WT(0, 0), WT(1, 0), WT(2, 0), WT(4, 0), WT(5, 0), WT(6, 0), WT(7, 0), WT(8, 0), WT(9, 0), WT(10, 0),
            WT(11, 0), WT(12, 0), WT(13, 0), WT(14, 0), WT(15, 0)],
        4: [WT(0, 0), WT(1, 0), WT(2, 0), WT(3, 0), WT(5, 0), WT(6, 0), WT(7, 0), WT(8, 0), WT(9, 0), WT(10, 0),
            WT(11, 0), WT(12, 0), WT(13, 0), WT(14, 0), WT(15, 0)],
        5: [WT(0, 0), WT(1, 0), WT(2, 0), WT(3, 0), WT(4, 0), WT(6, 0), WT(7, 0), WT(8, 0), WT(9, 0), WT(10, 0),
            WT(11, 0), WT(12, 0), WT(13, 0), WT(14, 0), WT(15, 0)],
        6: [WT(0, 0), WT(1, 0), WT(2, 0), WT(3, 0), WT(4, 0), WT(5, 0), WT(7, 0), WT(8, 0), WT(9, 0), WT(10, 0),
            WT(11, 0), WT(12, 0), WT(13, 0), WT(14, 0), WT(15, 0)],
        7: [WT(0, 0), WT(1, 0), WT(2, 0), WT(3, 0), WT(4, 0), WT(5, 0), WT(6, 0), WT(8, 0), WT(9, 0), WT(10, 0),
            WT(11, 0), WT(12, 0), WT(13, 0), WT(14, 0), WT(15, 0)],
        8: [WT(0, 0), WT(1, 0), WT(2, 0), WT(3, 0), WT(4, 0), WT(5, 0), WT(6, 0), WT(7, 0), WT(9, 0), WT(10, 0),
            WT(11, 0), WT(12, 0), WT(13, 0), WT(14, 0), WT(15, 0)],
        9: [WT(0, 0), WT(1, 0), WT(2, 0), WT(3, 0), WT(4, 0), WT(5, 0), WT(6, 0), WT(7, 0), WT(8, 0), WT(10, 0),
            WT(11, 0), WT(12, 0), WT(13, 0), WT(14, 0), WT(15, 0)],
        10: [WT(0, 0), WT(1, 0), WT(2, 0), WT(3, 0), WT(4, 0), WT(5, 0), WT(6, 0), WT(7, 0), WT(8, 0), WT(9, 0),
             WT(11, 0), WT(12, 0), WT(13, 0), WT(14, 0), WT(15, 0)],
        11: [WT(0, 0), WT(1, 0), WT(2, 0), WT(3, 0), WT(4, 0), WT(5, 0), WT(6, 0), WT(7, 0), WT(8, 0), WT(9, 0),
             WT(10, 0), WT(12, 0), WT(13, 0), WT(14, 0), WT(15, 0)],
        12: [WT(0, 0), WT(1, 0), WT(2, 0), WT(3, 0), WT(4, 0), WT(5, 0), WT(6, 0), WT(7, 0), WT(8, 0), WT(9, 0),
             WT(10, 0), WT(11, 0), WT(13, 0), WT(14, 0), WT(15, 0)],
        13: [WT(0, 0), WT(1, 0), WT(2, 0), WT(3, 0), WT(4, 0), WT(5, 0), WT(6, 0), WT(7, 0), WT(8, 0), WT(9, 0),
             WT(10, 0), WT(11, 0), WT(12, 0), WT(14, 0), WT(15, 0)],
        14: [WT(0, 0), WT(1, 0), WT(2, 0), WT(3, 0), WT(4, 0), WT(5, 0), WT(6, 0), WT(7, 0), WT(8, 0), WT(9, 0),
             WT(10, 0), WT(11, 0), WT(12, 0), WT(13, 0), WT(15, 0)],
        15: [WT(0, 0), WT(1, 0), WT(2, 0), WT(3, 0), WT(4, 0), WT(5, 0), WT(6, 0), WT(7, 0), WT(8, 0), WT(9, 0),
             WT(10, 0), WT(11, 0), WT(12, 0), WT(13, 0), WT(14, 0)],
    },
    'Map_Battle_Frontier_Room00_00': {
        0: [WT(1, 0), WT(2, 0), WT(3, 0), WT(4, 0), WT(5, 0)],
        1: [WT(0, 0), WT(2, 0), WT(3, 0), WT(4, 0), WT(5, 0)],
        2: [WT(0, 0), WT(1, 0), WT(3, 0), WT(4, 0), WT(5, 0)],
        3: [WT(0, 0), WT(1, 0), WT(2, 0), WT(4, 0), WT(5, 0)],
        4: [WT(0, 0), WT(1, 0), WT(2, 0), WT(3, 0), WT(5, 0)],
        5: [WT(0, 0), WT(1, 0), WT(2, 0), WT(3, 0), WT(4, 0)],
    },
    'Map_Battle_Tower_Room01_00': {
        0: [WT(1, 0), WT(2, 0)],
        1: [WT(0, 0), WT(2, 0)],
        2: [WT(0, 0), WT(1, 0)],
    },
    'Map_Battle_Factory_Room02_00': {
        0: [WT(1, 0), WT(2, 0)],
        1: [WT(0, 0), WT(2, 0)],
        2: [WT(0, 0), WT(1, 0)],
    },
    'Map_Battle_Hall_Room03_00': {
        0: [WT(1, 0), WT(2, 0)],
        1: [WT(0, 0), WT(2, 0)],
        2: [WT(0, 0), WT(1, 0)],
    },
    'Map_Battle_Castle_Room04_00': {
        0: [WT(1, 0), WT(2, 0)],
        1: [WT(0, 0), WT(2, 0)],
        2: [WT(0, 0), WT(1, 0)],
    },
    'Map_Battle_Arcade_Room05_00': {
        0: [WT(1, 0), WT(2, 0)],
        1: [WT(0, 0), WT(2, 0)],
        2: [WT(0, 0), WT(1, 0)],
    },
    'Map_Global_Terminal_Room11_00': {
        0: [WT(1, 0), WT(2, 0)],
        1: [WT(0, 0), WT(2, 0)],
        2: [WT(0, 0), WT(1, 0)],
    },
    'Map_Frontier_Access_Room00_01': {
        0: [WT(1, 0), WT(2, 0), WT(3, 0), WT(4, 0), WT(5, 0), WT(6, 0)],
        1: [WT(0, 0), WT(2, 0), WT(3, 0), WT(4, 0), WT(5, 0), WT(6, 0)],
        2: [WT(0, 0), WT(1, 0), WT(3, 0), WT(4, 0), WT(5, 0), WT(6, 0)],
        3: [WT(0, 0), WT(1, 0), WT(2, 0), WT(4, 0), WT(5, 0), WT(6, 0)],
        4: [WT(0, 0), WT(1, 0), WT(2, 0), WT(3, 0), WT(5, 0), WT(6, 0)],
        5: [WT(0, 0), WT(1, 0), WT(2, 0), WT(3, 0), WT(4, 0), WT(6, 0)],
        6: [WT(0, 0), WT(1, 0), WT(2, 0), WT(3, 0), WT(4, 0), WT(5, 0)],
    },
    'Map_Route_5_Room01_01': {
        0: [WT(1, 0), WT(2, 0), WT(3, 0), WT(4, 0), WT(5, 0)],
        1: [WT(0, 0), WT(2, 0), WT(3, 0), WT(4, 0), WT(5, 0)],
        2: [WT(0, 0), WT(1, 0), WT(3, 0), WT(4, 0), WT(5, 0)],
        3: [WT(0, 0), WT(1, 0), WT(2, 0), WT(4, 0), WT(5, 0)],
        4: [WT(0, 0), WT(1, 0), WT(2, 0), WT(3, 0), WT(5, 0)],
        5: [WT(0, 0), WT(1, 0), WT(2, 0), WT(3, 0), WT(4, 0)],
    },
    'Map_Route_5_Room01_00': {
        0: [WT(1, 0), WT(2, 0), WT(3, 0)],
        1: [WT(0, 0), WT(2, 0), WT(3, 0)],
        2: [WT(0, 0), WT(1, 0), WT(3, 0)],
        3: [WT(0, 0), WT(1, 0), WT(2, 0)],
    },
    'Map_Route_6_Room00_00': {
        0: [WT(1, 0), WT(2, 0), WT(3, 0)],
        1: [WT(0, 0), WT(2, 0), WT(3, 0)],
        2: [WT(0, 0), WT(1, 0), WT(3, 0)],
        3: [WT(0, 0), WT(1, 0), WT(2, 0)],
    },
    'Map_Saffron_City_Gym_00': {
        2: [WT(3, 0), WT(16, 0), WT(17, 0)],
        3: [WT(2, 0), WT(16, 0), WT(17, 0)],
        4: [WT(5, 0), WT(24, 0), WT(25, 0)],
        5: [WT(4, 0), WT(24, 0), WT(25, 0)],
        6: [WT(7, 0), WT(20, 0), WT(21, 0)],
        7: [WT(6, 0), WT(20, 0), WT(21, 0)],
        8: [WT(9, 0), WT(28, 0), WT(29, 0)],
        9: [WT(8, 0), WT(28, 0), WT(29, 0)],
        10: [WT(11, 0), WT(22, 0), WT(23, 0)],
        11: [WT(10, 0), WT(22, 0), WT(23, 0)],
        12: [WT(13, 0), WT(18, 0), WT(19, 0)],
        13: [WT(12, 0), WT(18, 0), WT(19, 0)],
        14: [WT(15, 0), WT(26, 0), WT(27, 0)],
        15: [WT(14, 0), WT(26, 0), WT(27, 0)],
        16: [WT(2, 0), WT(3, 0), WT(17, 0)],
        17: [WT(2, 0), WT(3, 0), WT(16, 0)],
        18: [WT(12, 0), WT(13, 0), WT(19, 0)],
        19: [WT(12, 0), WT(13, 0), WT(18, 0)],
        20: [WT(6, 0), WT(7, 0), WT(21, 0)],
        21: [WT(6, 0), WT(7, 0), WT(20, 0)],
        22: [WT(10, 0), WT(11, 0), WT(23, 0)],
        23: [WT(10, 0), WT(11, 0), WT(22, 0)],
        24: [WT(4, 0), WT(5, 0), WT(25, 0)],
        25: [WT(4, 0), WT(5, 0), WT(24, 0)],
        26: [WT(14, 0), WT(15, 0), WT(27, 0)],
        27: [WT(14, 0), WT(15, 0), WT(26, 0)],
        28: [WT(8, 0), WT(9, 0), WT(29, 0)],
        29: [WT(8, 0), WT(9, 0), WT(28, 0)],
    },
    'Map_Mount_Silver_Cave_Room00_00': {
        0: [WT(1, [SURF_FLAG, WATERFALL_FLAG, ROCKCLIMB_FLAG]), WT(2, [SURF_FLAG, WATERFALL_FLAG]), WT(3, [ROCKCLIMB_FLAG]), WT(4, [SURF_FLAG, WATERFALL_FLAG, ROCKCLIMB_FLAG]), WT(6, [SURF_FLAG, WATERFALL_FLAG, ROCKCLIMB_FLAG])],
        1: [WT(0, [SURF_FLAG, WATERFALL_FLAG, ROCKCLIMB_FLAG]), WT(2, [SURF_FLAG, WATERFALL_FLAG, ROCKCLIMB_FLAG]), WT(3, [SURF_FLAG, WATERFALL_FLAG, ROCKCLIMB_FLAG]), WT(4, [SURF_FLAG, WATERFALL_FLAG, ROCKCLIMB_FLAG]), WT(6, [SURF_FLAG, WATERFALL_FLAG, ROCKCLIMB_FLAG])],
        2: [WT(0, [SURF_FLAG, WATERFALL_FLAG]), WT(1, [SURF_FLAG, WATERFALL_FLAG, ROCKCLIMB_FLAG]), WT(3, [SURF_FLAG, WATERFALL_FLAG, ROCKCLIMB_FLAG]), WT(4, [SURF_FLAG, ROCKCLIMB_FLAG]), WT(6, [SURF_FLAG, ROCKCLIMB_FLAG])],
        3: [WT(0, [ROCKCLIMB_FLAG]), WT(1, [SURF_FLAG, WATERFALL_FLAG, ROCKCLIMB_FLAG]), WT(2, [SURF_FLAG, WATERFALL_FLAG, ROCKCLIMB_FLAG]), WT(4, [SURF_FLAG, WATERFALL_FLAG, ROCKCLIMB_FLAG]), WT(6, [SURF_FLAG, WATERFALL_FLAG, ROCKCLIMB_FLAG])],
        4: [WT(0, [SURF_FLAG, WATERFALL_FLAG, ROCKCLIMB_FLAG]), WT(1, [SURF_FLAG, WATERFALL_FLAG, ROCKCLIMB_FLAG]), WT(2, [SURF_FLAG, ROCKCLIMB_FLAG]), WT(3, [SURF_FLAG, WATERFALL_FLAG, ROCKCLIMB_FLAG]), WT(6, 0)],
        5: [],
        6: [WT(0, [SURF_FLAG, WATERFALL_FLAG, ROCKCLIMB_FLAG]), WT(1, [SURF_FLAG, WATERFALL_FLAG, ROCKCLIMB_FLAG]),WT(2, [SURF_FLAG, WATERFALL_FLAG, ROCKCLIMB_FLAG]), WT(3, [SURF_FLAG, WATERFALL_FLAG, ROCKCLIMB_FLAG]), WT(4, 0)]
    },
    'Map_Mount_Silver_Cave_Room00_01': {
        0: [WT(1, 0), WT(2, 0)],
        1: [WT(0, 0), WT(2, 0)],
        2: [WT(0, 0), WT(1, 0)],
        3: [WT(4, 0), WT(5, [ROCKCLIMB_FLAG, ROCKCLIMB_FLAG]), WT(6, [ROCKCLIMB_FLAG, ROCKCLIMB_FLAG])],
        4: [WT(3, 0), WT(5, [ROCKCLIMB_FLAG, ROCKCLIMB_FLAG]), WT(6, [ROCKCLIMB_FLAG, ROCKCLIMB_FLAG])],
        5: [WT(6, [ROCKCLIMB_FLAG, ROCKCLIMB_FLAG]), WT(4, [ROCKCLIMB_FLAG, ROCKCLIMB_FLAG]), WT(3, [ROCKCLIMB_FLAG, ROCKCLIMB_FLAG])],
        6: [WT(5, [ROCKCLIMB_FLAG, ROCKCLIMB_FLAG]), WT(4, [ROCKCLIMB_FLAG, ROCKCLIMB_FLAG]), WT(3, [ROCKCLIMB_FLAG, ROCKCLIMB_FLAG])],
    },
    'Map_Mount_Silver_Cave_Room00_02': {
        0: [WT(1, 0), WT(2, 0)],
        1: [WT(0, 0), WT(2, 0)],
        2: [WT(0, 0), WT(1, 0)],
    },
    'Map_Mount_Silver_Cave_Room00_05': {
        0: [WT(1, 0)],
        1: [WT(0, 0)],
        2: [],
        3: [WT(4, 0)],
        4: [WT(3, 0)],
        5: [WT(6, 0)],
        6: [WT(5, 0)]
    },
    'Map_Mount_Silver_Cave_Room00_06': {
        0: [WT(1, [ROCKCLIMB_FLAG])],
        1: [WT(0, [ROCKCLIMB_FLAG])]
    },
    # 'Map_Sinjoh_Ruins_Room00_00': {
    # },
    # 'Map_Mount_Moon_Room00_03': {
    # },
}

# TODO Fill Out Later

map_to_map_warp_accessibility = {
    'Map_Route_16': {
        'Map_Route_17': WT(0, 0)
    },
    'Map_Route_18' : {
        'Map_Route_17': WT(0, 0),
        'Map_Fuchsia_City': WT(2, 0)
    },
    'Map_Safari_Zone_Gate': {
        'Map_Route_48': WT(2, 0)
    },
    'Map_Route_47': {
        'Map_Route_48': WT(3, 0)
    }
}

cant_go_back_warps = { #missing champion room
    'Map_Pokemon_League_Room01_00': [0],
    'Map_Pokemon_League_Room02_00': [0],
    'Map_Pokemon_League_Room03_00': [0],
    'Map_Pokemon_League_Room04_00': [0],
    'Map_Pokemon_League_Room05_00': [0],
    'Map_Bell_Tower_Room00_04': [1, 2], #after you get there you cant jump back
}

# Handles Connection Requirements
rocksmash_needed = [  # TODO make work
    'Map_Route_32',  # this is here because of the gym and sprout tower requirement to pass the miracle seed guy
]
cut_needed = [  # TODO make work
    'Map_Route_32'
]
surf_needed = [  # TODO make work
    'Map_Route_41'
]
strength_or_spraypail_needed = [  # TODO make work
    'Map_Route_36'
]
bike_needed = [

]
whirlpool_needed = [

]

# TODO finish work
dont_randomize = [
    'Map_New_Bark_Town_Room00_00', 'Map_New_Bark_Town_Room01_01', 'Map_New_Bark_Town_Room02_00', 'Map_New_Bark_Town_Room01_00',
    'Map_New_Bark_Town_Room03_01', 'Map_New_Bark_Town_Room00_01', 'Map_Route_30_Room00_00', 'Map_Azalea_Town_Gym_01',
    'Map_Mahogany_Town_Gym_01', 'Map_Mahogany_Town_Gym_00', 'Map_Saffron_City_Room06_02', 'Map_ROTOMs_Room',
    'Map_Goldenrod_City_Room09_06', 'Map_Celadon_City_Room00_06', 'Map_Celadon_City_Room01_02',
    'Map_Radio_Tower_Room00_05'
    'Map_Celadon_City_Room01_05',
    'Map_Celadon_City_Room01_06',
    'Map_Lighthouse_Room00_07',
    'Map_Battle_Frontier_Room00_00',
    'Map_Frontier_Access_Room00_01',
    'Map_Battle_Frontier',
    'Map_Safari_Zone_Gate_Room00_00',
    'Map_Pal_Park_Room01_00',
    'Map_Pal_Park_Room00_00',
    'Map_New_Bark_Town_Room01_01',
    'Map_New_Bark_Town_Room03_01',
    'Map_Battle_Tower',
    'Map_Battle_Factory',
    'Map_Battle_Hall',
    'Map_Battle_Castle',
    'Map_Battle_Arcade',
    'Map_Safari_Zone_Room00_01',  # this is like some weird map in the safari zone that points to Map_None as well, no clue what's going on here until I can get DSPRE going
    'Map_Route_34_Room00_00', #lyra brings u here so we can change the actual daycare entrance instead
]

dont_randomize_warp = {  # TODO finish work - should probably add all of the entrances to elevators
    'Map_Saffron_City_Room06_00': [1],
    'Map_Ecruteak_City_PokemonCenter00_00': [1],
    'Map_Mount_Moon_Room00_01': [4, 5],
    'Map_National_Park_Room00_00': [4, 5 ,6],
    'Map_Whirl_Islands_Room00_05': [4], #thats dummy
    'Map_Route_47': [4, 5], #groudon and kyogre entrances
    'Map_Goldenrod_City_Room04_00': [1, 2], #warps going to the actual station, removing for good measure,
    'Map_Saffron_City_Room05_00': [1, 2], #warps going to the actual train to saffron, removing for good measure cuz scripted like above
    'Map_Olivine_City_Room00_00': [1], #blocked warp by ss aqua ticket
}

not_needed = [  # TODO finish work, this likely is partially incorrect thanks to ends containing some maps which it shouldn't/missing some that it should
    'Map_New_Bark_Town_Room00_00', 'Map_New_Bark_Town_Room01_01', 'Map_New_Bark_Town_Room02_00',
    'Map_New_Bark_Town_Room03_01', 'Map_New_Bark_Town_Room00_01',
    'Map_Goldenrod_City_PokemonCenter00_01',
    'Map_Goldenrod_City_Special00_00', 'Map_Goldenrod_City_Room04_02', 'Map_Goldenrod_City_Room03_00',
    'Map_Goldenrod_City_Room02_00', 'Map_Goldenrod_City_Room07_00', 'Map_Goldenrod_City_Room08_00',
    'Map_Azalea_Town_PokemonCenter00_01', 'Map_Azalea_Town_Room01_00',
    #'Map_Azalea_Town_Mart00_00',
     'Map_Slowpoke_Well_Room00_02',
    'Map_Ruins_of_Alph_Room01_11', 'Map_Ruins_of_Alph_Room01_12', 'Map_Ruins_of_Alph_Room01_14',
    'Map_Ruins_of_Alph_Room01_13', 'Map_Ruins_of_Alph_Room01_04', 'Map_Ruins_of_Alph_Room01_15',
    'Map_Ruins_of_Alph_Room00_01', 'Map_Ruins_of_Alph_Room01_17', 'Map_Route_32_PokemonCenter00_01',
     'Map_Pokeathlon_Dome', 'Map_Pokeathlon_Dome_Room00_06', 'Map_Pokeathlon_Dome_Room00_01',
    'Map_Pokeathlon_Dome_Room01_00', 'Map_Ecruteak_City_Room03_00',
    'Map_Ecruteak_City_Room07_00', 'Map_Mystery_Zone',
    'Map_Ecruteak_City_PokemonCenter00_04', 
    #'Map_Ecruteak_City_Mart00_00', 
    'Map_Olivine_City_PokemonCenter00_01',
    #'Map_Olivine_City_Mart00_00',
    'Map_Lighthouse_Room00_02', 'Map_Olivine_City_Room05_00', 'Map_Olivine_City_Room06_00',
    'Map_Olivine_City_Room02_00', 'Map_Olivine_City_Room04_00', 
    'Map_SS_Aqua_Room02_01',
    'Map_Vermilion_City_Room00_00',
    'Map_Vermilion_City_PokemonCenter00_01', 'Map_Vermilion_City_Room02_00', 'Map_Vermilion_City_Room03_00',
    #'Map_Vermilion_City_Mart00_00', 
    'Map_Vermilion_City_Room05_00',
    'Map_Route_12_Room00_00', 
    #'Map_Seafoam_Islands_Room00_05', #blaine gym
    'Map_Cinnabar_Island_PokemonCenter00_01',
    'Map_Pallet_Town_Room00_01', 'Map_Pallet_Town_Room01_01',
    'Map_Viridian_City_Room01_00', 'Map_Viridian_City_Room02_01', 
    #'Map_Viridian_City_Mart00_00',
    'Map_Viridian_City_PokemonCenter00_01', 'Map_Route_26_Room01_00', 
    'Map_Tohjo_Falls_Room00_01', #giovani fight in celebi event. might need to set as dont randomize
    'Map_Route_27_Room00_00', 
    'Map_Pokemon_League_Room06_00', #hall of fame, might need to set in dont randomize ?
    'Map_Pokemon_League_Room07_00', 'Map_Route_28_Room00_00',
    'Map_Mount_Silver_Cave_Room00_04', #moltres room. do we leave here or include in randomisation ? need rock climb
    'Map_Mount_Silver_Cave_Room00_03', 
    #'Map_Mount_Silver_Cave_Room00_07', #this is Top of mount silver, fight against Red
    'Map_Mount_Silver_PokemonCenter00_01', 'Map_Route_2_Room01_00', 
    'Map_Pewter_City_Room00_00', #fossils, as well as interaction with steven about latios and latias
    'Map_Pewter_City_Room01_00', 
    #'Map_Pewter_City_Mart00_00',
    'Map_Pewter_City_PokemonCenter00_01', 'Map_Pewter_City_Room05_00', 'Map_Cerulean_City_Room00_00',
    'Map_Cerulean_City_Room01_00', 'Map_Cerulean_City_Room02_00', 'Map_Cerulean_City_PokemonCenter00_01',
    #'Map_Cerulean_City_Mart00_00', 
    'Map_Cerulean_City_Room03_00',
    'Map_Lavender_Town_PokemonCenter00_01', 'Map_Lavender_Town_Room01_00', 'Map_Lavender_Town_Room02_00',
    'Map_Lavender_Town_Room03_00', 
    #'Map_Lavender_Town_Mart00_00', 
    'Map_Lavender_Town_Room05_00',
    'Map_Lavender_Town_Room06_00', 
    #'Map_Power_Plant_Room01_00', #this room is super important as it restores power in kanto after gaining the marchine part from team rocket. leaving here for now, might be required
    'Map_Route_10_PokemonCenter00_01',
    'Map_Saffron_City_Room05_02', #train station room. unsure if this is scripted. might need to throw in dont_randomize
    #'Map_Saffron_City_Room07_01', #this room is useful cause thats where you get the train pass. lets see what we do with it
    'Map_Saffron_City_Room06_00', #only useful with rotom, but we banned rotom room so
    'Map_Saffron_City_Room00_00', 
    #'Map_Saffron_City_Mart00_00',
    'Map_Saffron_City_PokemonCenter00_01', 'Map_Saffron_City_Room04_00', 'Map_Celadon_City_Room01_01',
    'Map_Celadon_City_PokemonCenter00_01', 'Map_Celadon_City_Special00_00', 'Map_Celadon_City_Room04_00',
    'Map_Celadon_City_Room06_00', 'Map_Route_16_Room00_00', 'Map_Route_5_Room03_00',
    'Map_Route_25_Room00_00', 
    #'Map_Mount_Moon_Mart00_00', 
    'Map_Route_3_PokemonCenter00_01',
    #'Map_Fuchsia_City_Mart00_00', 
    'Map_Pal_Park_Room01_00', #might be smart to throw in dont randomize, or define in unreachable ?
    'Map_Fuchsia_City_Room03_00',
    'Map_Fuchsia_City_PokemonCenter00_01', 'Map_Fuchsia_City_Room05_00', 'Map_Battle_Tower_Room01_00',
    'Map_Battle_Factory_Room02_00', 'Map_Battle_Hall_Room03_00', 'Map_Battle_Castle_Room04_00',
    'Map_Battle_Arcade_Room05_00', 'Map_Frontier_Access_PokemonCenter00_01', 'Map_Frontier_Access_Mart00_00',
    'Map_Frontier_Access_Room00_02', 
    'Map_Whirl_Islands_Room00_05', #assuming we make the silver feather available, we could do something with this room ?
    'Map_Cianwood_City_PokemonCenter00_01',
    'Map_Cianwood_City_Room01_00', 'Map_Cianwood_City_Room06_00', 'Map_Cianwood_City_Room05_00',
    'Map_Embedded_Tower_Room00_00', #groudon will be there
    'Map_Embedded_Tower_Room00_01', #kyogre will be there
    'Map_Embedded_Tower_Room00_02', #rayquaza will be there. These affect r47 because its 3 warps on the same tile. we could give an orb so at least 1 warp is always set, like jade orb
    'Map_Safari_Zone_Gate_Room00_00', 'Map_Safari_Zone_Gate_PokemonCenter00_01', 'Map_Cianwood_City_Room07_00',
    'Map_Lake_of_Rage_Room00_00', 'Map_Lake_of_Rage_Room01_00',
    'Map_Mahogany_Town_PokemonCenter00_01', 'Map_Mahogany_Town_Room01_00', 'Map_Blackthorn_City_Room01_00',
    'Map_Blackthorn_City_Room02_00',
    #'Map_Blackthorn_City_Mart00_00', 
    'Map_Blackthorn_City_PokemonCenter00_01', 'Map_Blackthorn_City_Room05_00',
    'Map_Violet_City_Room02_00', 'Map_Violet_City_PokemonCenter00_01',
    'Map_Violet_City_Room03_00', 'Map_Violet_City_Room05_00', 
    #'Map_Violet_City_Mart00_00', 
    #'Map_Route_30_Room01_00', #this is mr.pokemon's house. pre much MANDATORY to go here at the start of the game unless we fix it in script. Players can start warping VERY early in the first town !!!!!
    'Map_Route_30_Room00_00', 'Map_Cherrygrove_City_PokemonCenter00_01', 
    #'Map_Cherrygrove_City_Mart00_00',
    'Map_Cherrygrove_City_Room02_00', 'Map_Cherrygrove_City_Room03_00', 'Map_Cherrygrove_City_Room04_00',
    'Map_Pal_Park_Room00_00', 
    'Map_Goldenrod_City_Room10_00', #this is the slots game corner, if we restored the text 100% would be usable
    'Map_Celadon_City_Room03_00', #samr thing but in celadon
    'Map_Celadon_City_Room01_03', 'Map_Celadon_City_Room01_04', 'Map_Goldenrod_City_Room09_06',
    'Map_Celadon_City_Room00_06',
    'Map_Mount_Moon_Room00_03', #this seems to be a duplicate, we will remove it
]

non_navigable_connections = [  # TODO finish work

]

connection_to_connection_rules = {
    'Map_Route_36': {'Map_Ecruteak_City': 32},
    'Map_Route_40': {'Map_Route_41': 64}
}

grouped_warps = {

}

other_overwrites = {
    "League Will":{
        'resource_folder': 'league_will',
        'script_overwrite': 820,
        'event_overwrite': 272
    },
    "League Koga": {
        'resource_folder': 'league_koga',
        'script_overwrite': 821,
        'event_overwrite': 273
    },
    'League Bruno':{
        'resource_folder': 'league_bruno',
        'script_overwrite': 822,
        'event_overwrite': 274
    },
    'League Karen': {
        'resource_folder': 'league_karen',
        'script_overwrite': 823,
        'event_overwrite': 275
    },
    'League Champion': {
        'resource_folder': 'league_champ',
        'script_overwrite': 824,
        'event_overwrite': 276
    },
    'New Bark Mom Start': {
        'resource_folder': 'new_bark_mom',
        'script_overwrite': 845
    },
    'Rocket Hideout BF2 Mahogany': {
        'resource_folder': 'mahogany_hideout_bf2',
        'script_overwrite': 90
    },
    'SS Aqua' : {
        'resource_folder': 'ss_aqua',
        'script_overwrite': 156
    },
    'Blackthorn Gym': {
        'resource_folder': 'blackthorn_gym',
        'script_overwrite': 943
    },
    'Goldenrod Tunnel Lyra Interaction': {
        'resource_folder': 'goldenrod_tunnel_lyra',
        'script_overwrite': 93
    },
    'Pokeathlon Trophy Room' :{
        'resource_folder': 'pokeathlon_trophy_room',
        'event_overwrite' : 256
    },
    'Mt Moon Exterior': {
        'resource_folder': 'mt_moon_exterior',
        'script_overwrite': 9
    },
    'Ss Aqua harbor exterior': {
        'resource_folder': 'ss_aqua_harbor_exterior',
        'event_overwrite': 301
    }
}

override_maps = [

]


def search_for_needed_maps(event_maps, accesible_maps):
    ret = True
    for req in event_maps:
        map_name = req
        warp_parts = []
        if ':' in req:
            map_name = req.split(':')[0]
            warp_parts = req.split(':')
        if map_name not in accesible_maps:
            ret = False
            break
        if len(warp_parts) != 0:
            original_length = len(warp_parts)
            for warp in accesible_maps[map_name]:
                if str(warp) in warp_parts:
                    warp_parts.remove(str(warp))
            if len(warp_parts) == original_length:
                ret = False
                break
    return ret


def check_progession_blockers(flag, accesible_maps):  # TODO make work
    for flag_num in range(len(FLAG_EVENT_LIST)):
        if flag_num == flag:
            return search_for_needed_maps(FLAG_EVENT_LIST[flag], accesible_maps)
    return False


# If warp_id = -1 we check connection, otherwise we check if there is an accessible warp from warp id
# noinspection DuplicatedCode
def is_map_progressable(map, accesible_maps, warp_id, ignore=False):  # TODO make work
    if not check_progession_blockers(SURF_FLAG, accesible_maps) and map in surf_needed:
        return False
    if not check_progession_blockers(ROCKSMASH_FLAG, accesible_maps) and map in rocksmash_needed:
        return False
    if not check_progession_blockers(CUT_FLAG, accesible_maps) and map in cut_needed:
        return False
    if not check_progession_blockers(BIKE_FLAG, accesible_maps) and map in bike_needed:
        return False
    if not check_progession_blockers(STRENGTH_FLAG, accesible_maps) and map in strength_or_spraypail_needed:
        return False
    if not check_progession_blockers(WHIRLPOOL_FLAG, accesible_maps) and map in whirlpool_needed:
        return False
    if warp_id == -1 and not ignore:
        if map not in map_warp_accessibility:
            return True
        map_warps = map_warp_accessibility[map].keys()
        for map_warp in map_warps:
            if is_map_progressable(map, accesible_maps, map_warp):
                return True
        return False
    if warp_id != -1:
        if map not in map_warp_accessibility:
            return True
        if warp_id not in map_warp_accessibility[map]:
            return True
        potential_warps = map_warp_accessibility[map][warp_id]
        if len(potential_warps) == 0:
            return True
        for potential_warp in potential_warps:
            bits = bin(potential_warp.flag)
            index = 0
            warp_pass = True
            for bit in reversed(bits):
                if bit == '1':
                    if not check_progession_blockers(index, accesible_maps):
                        warp_pass = False
                        break
                index = index + 1
            if warp_pass:
                return True
        return False
    else:
        return True


def is_warp_to_warp_valid(map, accesible_maps, from_warp_id, to_warp_id):
    if map not in map_warp_accessibility:
        return True  # If map doesn't specify warp routing all warps are accessible
    if from_warp_id not in map_warp_accessibility[map]:
        return False  # If warp id isnt in map specifications, warp is not meant to be randomized
    potential_warps = map_warp_accessibility[map][from_warp_id]
    for potential_warp in potential_warps:
        if potential_warp.warp_id != to_warp_id:
            continue
        bits = bin(potential_warp.flag)
        index = 0
        warp_pass = True
        for bit in reversed(bits):
            if bit == '1':
                if not check_progession_blockers(index, accesible_maps):
                    warp_pass = False
                    break
            index = index + 1
        if warp_pass:
            return True
    return False


def is_warp_ready(warp_tuple: WT, accesible_maps):
    bits = bin(warp_tuple.flag)
    index = 0
    warp_pass = True
    for bit in reversed(bits):
        if bit == '1':
            if not check_progession_blockers(index, accesible_maps):
                warp_pass = False
                break
        index = index + 1
    return warp_pass
