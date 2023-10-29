"""
EmeraldWarpMapInfo.py

Pokemon Emerald Warp Randomizer rules definitions

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
        if isinstance(warp_id, int) and isinstance(flag, int):
            self.warp_id = warp_id
            self.flag = flag
        else:
            raise ValueError("Invalid Warp Tuple")


# Event/HM Dependencies
# Any Warp/Connection that has an Event/HM Dependency will have a corresponding blocker flag
# Based off bits set in flag, we will know what dependencies are required to traverse
TUTORIAL_FLAG = 0
CUT_FLAG = 1
FLASH_FLAG = 2
OCEANIC_MUSEUM_FLAG = 3
ROCKSMASH_FLAG = 4
BIKE_FLAG = 5
METEOR_FALLS_FLAG = 6
MT_CHIMNEY_FLAG = 7
GOGGLES_FLAG = 8
STRENGTH_FLAG = 9
SURF_FLAG = 10
WEATHER_INSTITUTE_FLAG = 11
FLY_FLAG = 12
DEVON_SCOPE_FLAG = 13
SUMMIT_FLAG = 14
LEGENDARIES_BATTLE_FLAG = 15
DIVE_FLAG = 16
CAVE_OF_ORIGIN_FLAG = 17
END_STORY_FLAG = 18
WATERFALL_FLAG = 19

END_FLAG = WATERFALL_FLAG

tutorial_event = ['MAP_PETALBURG_CITY_GYM']
cut_event = ['MAP_RUSTBORO_CITY_GYM', 'MAP_RUSTBORO_CITY_CUTTERS_HOUSE']
flash_event = ['MAP_RUSTBORO_CITY_GYM', 'MAP_DEWFORD_TOWN_GYM', 'MAP_GRANITE_CAVE_1F']
oceanic_museum_event = ['MAP_SLATEPORT_CITY_STERNS_SHIPYARD_1F', 'MAP_SLATEPORT_CITY_OCEANIC_MUSEUM_2F']
rocksmash_event = ['MAP_RUSTBORO_CITY_GYM', 'MAP_DEWFORD_TOWN_GYM', 'MAP_MAUVILLE_CITY_GYM', 'MAP_MAUVILLE_CITY_HOUSE1']
bike_event = ['MAP_MAUVILLE_CITY_BIKE_SHOP']
meteor_falls_event = ['MAP_METEOR_FALLS_1F_1R:0:1']
mt_chimney_event = ['MAP_MT_CHIMNEY:0:1']
goggles_event = ['MAP_LAVARIDGE_TOWN_GYM_1F', 'MAP_LAVARIDGE_TOWN']
strength_event = ['MAP_RUSTBORO_CITY_GYM', 'MAP_DEWFORD_TOWN_GYM', 'MAP_MAUVILLE_CITY_GYM', 'MAP_LAVARIDGE_TOWN_GYM_1F',
                  'MAP_RUSTURF_TUNNEL:1:2']
surf_event = ['MAP_RUSTBORO_CITY_GYM', 'MAP_DEWFORD_TOWN_GYM', 'MAP_MAUVILLE_CITY_GYM', 'MAP_LAVARIDGE_TOWN_GYM_1F',
              'MAP_PETALBURG_CITY_GYM', 'MAP_PETALBURG_CITY_WALLYS_HOUSE']
weather_institute_event = ['MAP_ROUTE119_WEATHER_INSTITUTE_2F']
fly_event = ['MAP_FORTREE_CITY', 'MAP_FORTREE_CITY_GYM']
devon_scope_event = ['MAP_ROUTE120']
summit_event = ['MAP_MT_PYRE_SUMMIT']
legendaries_battle_event = ['MAP_MAGMA_HIDEOUT_4F', 'MAP_SLATEPORT_CITY', 'MAP_SLATEPORT_CITY_HARBOR',
                            'MAP_SEAFLOOR_CAVERN_ROOM9']
dive_event = ['MAP_MOSSDEEP_CITY_SPACE_CENTER_2F', 'MAP_MOSSDEEP_CITY_STEVENS_HOUSE', 'MAP_MOSSDEEP_CITY_GYM']
cave_of_origin_event = ['MAP_SOOTOPOLIS_CITY', 'MAP_CAVE_OF_ORIGIN_B1F']
end_story_event = ['MAP_SKY_PILLAR_ENTRANCE', 'MAP_SKY_PILLAR_TOP', 'MAP_SOOTOPOLIS_CITY']
waterfall_event = ['MAP_SOOTOPOLIS_CITY_GYM_1F']

FORCED_FLAG_ORDER = [CUT_FLAG, FLASH_FLAG, ROCKSMASH_FLAG, STRENGTH_FLAG, SURF_FLAG, FLY_FLAG, DIVE_FLAG,
                     WATERFALL_FLAG]
FLAG_EVENT_LIST = [tutorial_event, cut_event, flash_event, oceanic_museum_event, rocksmash_event, bike_event,
                   meteor_falls_event, mt_chimney_event, goggles_event, strength_event, surf_event,
                   weather_institute_event, fly_event, devon_scope_event, summit_event, legendaries_battle_event,
                   dive_event, cave_of_origin_event, end_story_event, waterfall_event]

no_event_allowed = ['MAP_EVER_GRANDE_CITY:1:2', 'MAP_EVER_GRANDE_CITY:0:3']
map_chain_breaks = ["MAP_ROUTE110_TRICK_HOUSE_PUZZLE1", "TERRA"]

# Not Needed for Emerald
grouped_warps = {}

# Event Based Warps and Warp Connections
# If map not specified, assume that all warps are accessible
map_warp_accessibility = {
    'MAP_PETALBURG_CITY': {
        0: [WT(1, 1), WT(2, 0), WT(3, 0), WT(4, 0), WT(5, 0)],
        1: [WT(0, 0), WT(2, 0), WT(3, 0), WT(4, 0), WT(5, 0)],
        2: [WT(0, 0), WT(1, 1), WT(3, 0), WT(4, 0), WT(5, 0)],
        3: [WT(0, 0), WT(1, 1), WT(2, 0), WT(4, 0), WT(5, 0)],
        4: [WT(0, 0), WT(1, 1), WT(2, 0), WT(3, 0), WT(5, 0)],
        5: [WT(0, 0), WT(1, 1), WT(2, 0), WT(3, 0), WT(4, 0)]
    },
    'MAP_SLATEPORT_CITY': {
        0: [WT(1, 0), WT(2, 0), WT(3, 0), WT(4, 0), WT(5, 8), WT(6, 0), WT(7, 8), WT(8, 0), WT(10, 0)],
        1: [WT(0, 0), WT(2, 0), WT(3, 0), WT(4, 0), WT(5, 8), WT(6, 0), WT(7, 8), WT(8, 0), WT(10, 0)],
        2: [WT(0, 0), WT(1, 0), WT(3, 0), WT(4, 0), WT(5, 8), WT(6, 0), WT(7, 8), WT(8, 0), WT(10, 0)],
        3: [WT(0, 0), WT(1, 0), WT(2, 0), WT(4, 0), WT(5, 8), WT(6, 0), WT(7, 8), WT(8, 0), WT(10, 0)],
        4: [WT(0, 0), WT(1, 0), WT(2, 0), WT(3, 0), WT(5, 8), WT(6, 0), WT(7, 8), WT(8, 0), WT(10, 0)],
        5: [WT(0, 0), WT(1, 0), WT(2, 0), WT(3, 0), WT(4, 0), WT(5, 0), WT(7, 8), WT(8, 0), WT(10, 0)],
        6: [WT(0, 0), WT(1, 0), WT(2, 0), WT(3, 0), WT(4, 0), WT(5, 8), WT(7, 8), WT(8, 0), WT(10, 0)],
        7: [WT(1, 0), WT(2, 0), WT(3, 0), WT(4, 0), WT(5, 8), WT(6, 0), WT(0, 0), WT(8, 0), WT(10, 0)],
        8: [WT(1, 0), WT(2, 0), WT(3, 0), WT(4, 0), WT(5, 8), WT(6, 0), WT(7, 8), WT(0, 0), WT(10, 0)],
        10: [WT(1, 0), WT(2, 0), WT(3, 0), WT(4, 0), WT(5, 8), WT(6, 0), WT(7, 8), WT(8, 0), WT(0, 0)]
    },
    'MAP_FORTREE_CITY': {
        0: [WT(1, 0), WT(2, 8192), WT(3, 0), WT(4, 0), WT(5, 0), WT(6, 0), WT(7, 0), WT(8, 0)],
        1: [WT(0, 0), WT(2, 8192), WT(3, 0), WT(4, 0), WT(5, 0), WT(6, 0), WT(7, 0), WT(8, 0)],
        2: [WT(1, 8192), WT(0, 8192), WT(3, 8192), WT(4, 8192), WT(5, 8192), WT(6, 8192), WT(7, 8192), WT(8, 8192)],
        3: [WT(1, 0), WT(2, 8192), WT(0, 0), WT(4, 0), WT(5, 0), WT(6, 0), WT(7, 0), WT(8, 0)],
        4: [WT(1, 0), WT(2, 8192), WT(3, 0), WT(0, 0), WT(5, 0), WT(6, 0), WT(7, 0), WT(8, 0)],
        5: [WT(1, 0), WT(2, 8192), WT(3, 0), WT(4, 0), WT(0, 0), WT(6, 0), WT(7, 0), WT(8, 0)],
        6: [WT(1, 0), WT(2, 8192), WT(3, 0), WT(4, 0), WT(5, 0), WT(0, 0), WT(7, 0), WT(8, 0)],
        7: [WT(1, 0), WT(2, 8192), WT(3, 0), WT(4, 0), WT(5, 0), WT(6, 0), WT(0, 0), WT(8, 0)],
        8: [WT(1, 0), WT(2, 8192), WT(3, 0), WT(4, 0), WT(5, 0), WT(6, 0), WT(7, 0), WT(0, 0)],
    },
    'MAP_LILYCOVE_CITY': {
        0: [WT(1, 0), WT(2, 0), WT(3, 0), WT(4, 0), WT(5, 0), WT(6, 1024), WT(7, 0), WT(8, 0), WT(9, 0), WT(10, 0),
            WT(11, 0), WT(12, 0), WT(13, 0)],
        1: [WT(0, 0), WT(2, 0), WT(3, 0), WT(4, 0), WT(5, 0), WT(6, 1024), WT(7, 0), WT(8, 0), WT(9, 0), WT(10, 0),
            WT(11, 0), WT(12, 0), WT(13, 0)],
        2: [WT(1, 0), WT(0, 0), WT(3, 0), WT(4, 0), WT(5, 0), WT(6, 1024), WT(7, 0), WT(8, 0), WT(9, 0), WT(10, 0),
            WT(11, 0), WT(12, 0), WT(13, 0)],
        3: [WT(1, 0), WT(2, 0), WT(0, 0), WT(4, 0), WT(5, 0), WT(6, 1024), WT(7, 0), WT(8, 0), WT(9, 0), WT(10, 0),
            WT(11, 0), WT(12, 0), WT(13, 0)],
        4: [WT(1, 0), WT(2, 0), WT(3, 0), WT(0, 0), WT(5, 0), WT(6, 1024), WT(7, 0), WT(8, 0), WT(9, 0), WT(10, 0),
            WT(11, 0), WT(12, 0), WT(13, 0)],
        5: [WT(1, 0), WT(2, 0), WT(3, 0), WT(4, 0), WT(0, 0), WT(6, 1024), WT(7, 0), WT(8, 0), WT(9, 0), WT(10, 0),
            WT(11, 0), WT(12, 0), WT(13, 0)],
        6: [WT(1, 0), WT(2, 0), WT(3, 0), WT(4, 0), WT(5, 0), WT(0, 0), WT(7, 0), WT(8, 0), WT(9, 0), WT(10, 0),
            WT(11, 0), WT(12, 0), WT(13, 0)],
        7: [WT(1, 0), WT(2, 0), WT(3, 0), WT(4, 0), WT(5, 0), WT(6, 1024), WT(0, 0), WT(8, 0), WT(9, 0), WT(10, 0),
            WT(11, 0), WT(12, 0), WT(13, 0)],
        8: [WT(1, 0), WT(2, 0), WT(3, 0), WT(4, 0), WT(5, 0), WT(6, 1024), WT(7, 0), WT(0, 0), WT(9, 0), WT(10, 0),
            WT(11, 0), WT(12, 0), WT(13, 0)],
        9: [WT(1, 0), WT(2, 0), WT(3, 0), WT(4, 0), WT(5, 0), WT(6, 1024), WT(7, 0), WT(8, 0), WT(0, 0), WT(10, 0),
            WT(11, 0), WT(12, 0), WT(13, 0)],
        10: [WT(1, 0), WT(2, 0), WT(3, 0), WT(4, 0), WT(5, 0), WT(6, 1024), WT(7, 0), WT(8, 0), WT(9, 0), WT(0, 0),
             WT(11, 0), WT(12, 0), WT(13, 0)],
        11: [WT(1, 0), WT(2, 0), WT(3, 0), WT(4, 0), WT(5, 0), WT(6, 1024), WT(7, 0), WT(8, 0), WT(9, 0), WT(10, 0),
             WT(0, 0), WT(12, 0), WT(13, 0)],
        12: [WT(1, 0), WT(2, 0), WT(3, 0), WT(4, 0), WT(5, 0), WT(6, 1024), WT(7, 0), WT(8, 0), WT(9, 0), WT(10, 0),
             WT(11, 0), WT(0, 0), WT(13, 0)],
        13: [WT(1, 0), WT(2, 0), WT(3, 0), WT(4, 0), WT(5, 0), WT(6, 1024), WT(7, 0), WT(8, 0), WT(9, 0), WT(10, 0),
             WT(11, 0), WT(12, 0), WT(0, 0)]
    },
    'MAP_SOOTOPOLIS_CITY': {
        0: [WT(1, 1024), WT(2, 263168), WT(4, 1024), WT(5, 0), WT(6, 1024), WT(7, 0), WT(8, 1024), WT(9, 0),
            WT(10, 1024), WT(11, 0), WT(12, 0)],
        5: [WT(1, 1024), WT(2, 263168), WT(4, 1024), WT(0, 0), WT(6, 1024), WT(7, 0), WT(8, 1024), WT(9, 0),
            WT(10, 1024), WT(11, 0), WT(12, 0)],
        7: [WT(1, 1024), WT(2, 263168), WT(4, 1024), WT(5, 0), WT(6, 1024), WT(0, 0), WT(8, 1024), WT(9, 0),
            WT(10, 1024), WT(11, 0), WT(12, 0)],
        9: [WT(1, 1024), WT(2, 263168), WT(4, 1024), WT(5, 0), WT(6, 1024), WT(7, 0), WT(8, 1024), WT(0, 0),
            WT(10, 1024), WT(11, 0), WT(12, 0)],
        11: [WT(1, 1024), WT(2, 263168), WT(4, 1024), WT(5, 0), WT(6, 1024), WT(7, 0), WT(8, 1024), WT(9, 0),
             WT(10, 1024), WT(0, 0), WT(12, 0)],
        12: [WT(1, 1024), WT(2, 263168), WT(4, 1024), WT(5, 0), WT(6, 1024), WT(7, 0), WT(8, 1024), WT(9, 0),
             WT(10, 1024), WT(11, 0), WT(0, 0)],
        2: [WT(1, 1024), WT(0, 1024), WT(4, 1024), WT(5, 1024), WT(6, 1024), WT(7, 1024), WT(8, 1024), WT(9, 1024),
            WT(10, 1024), WT(11, 1024), WT(12, 1024)],
        1: [WT(0, 1024), WT(2, 263168), WT(4, 0), WT(5, 1024), WT(6, 0), WT(7, 1024), WT(8, 0), WT(9, 1024),
            WT(10, 0), WT(11, 1024), WT(12, 1024)],
        4: [WT(0, 1024), WT(2, 263168), WT(1, 0), WT(5, 1024), WT(6, 0), WT(7, 1024), WT(8, 0), WT(9, 1024),
            WT(10, 0), WT(11, 1024), WT(12, 1024)],
        6: [WT(0, 1024), WT(2, 263168), WT(4, 0), WT(5, 1024), WT(1, 0), WT(7, 1024), WT(8, 0), WT(9, 1024),
            WT(10, 0), WT(11, 1024), WT(12, 1024)],
        8: [WT(0, 1024), WT(2, 263168), WT(4, 0), WT(5, 1024), WT(6, 0), WT(7, 1024), WT(1, 0), WT(9, 1024),
            WT(10, 0), WT(11, 1024), WT(12, 1024)],
        10: [WT(0, 1024), WT(2, 263168), WT(4, 0), WT(5, 1024), WT(6, 0), WT(7, 1024), WT(8, 0), WT(9, 1024),
             WT(1, 0), WT(11, 1024), WT(12, 1024)]
    },
    'MAP_EVER_GRANDE_CITY': {
        0: [WT(3, 0)],
        3: [WT(0, 0)],
        1: [WT(2, 0)],
        2: [WT(1, 0)]
    },
    'MAP_LAVARIDGE_TOWN': {
        0: [WT(1, 0), WT(2, 0), WT(3, 0), WT(4, 0)],
        1: [WT(0, 0), WT(2, 0), WT(3, 0), WT(4, 0)],
        2: [WT(1, 0), WT(0, 0), WT(3, 0), WT(4, 0)],
        3: [WT(1, 0), WT(2, 0), WT(0, 0), WT(4, 0)],
        4: [WT(1, 0), WT(2, 0), WT(3, 0), WT(0, 0)],
        5: []
    },
    'MAP_ROUTE104': {
        0: [WT(4, 0), WT(5, 0)],
        1: [WT(2, 0), WT(3, 0)],
        2: [WT(1, 0), WT(3, 0)],
        3: [WT(1, 0), WT(2, 0)],
        4: [WT(0, 0), WT(5, 0)],
        5: [WT(4, 0), WT(0, 0)],
        6: [WT(0, 0), WT(4, 0), WT(5, 0), WT(7, 0)],
        7: [WT(0, 0), WT(4, 0), WT(5, 0), WT(6, 0)]
    },
    'MAP_ROUTE110': {
        0: [WT(1, 1024), WT(2, 1024), WT(4, 1032)],
        1: [WT(0, 1024), WT(2, 0), WT(4, 8)],
        2: [WT(0, 1024), WT(1, 0), WT(4, 8)],
        4: [WT(0, 1024), WT(1, 8), WT(2, 8)],
        3: [WT(5, 0)],
        5: [WT(3, 0)]
    },
    'MAP_ROUTE111': {
        0: [WT(1, 272), WT(2, 272), WT(3, 272), WT(4, 0)],
        1: [WT(0, 16), WT(2, 0), WT(3, 0), WT(4, 16)],
        2: [WT(1, 256), WT(0, 272), WT(3, 256), WT(4, 272)],
        3: [WT(1, 0), WT(2, 0), WT(0, 16), WT(4, 16)],
        4: [WT(1, 272), WT(2, 272), WT(3, 272), WT(0, 0)]
    },
    'MAP_ROUTE112': {
        0: [WT(1, 0), WT(4, 64)],
        1: [WT(0, 0), WT(4, 64)],
        4: [WT(0, 64), WT(1, 64)],
        2: [WT(0, 64), WT(1, 64), WT(3, 0), WT(4, 0)],
        3: [WT(0, 64), WT(1, 64), WT(2, 0), WT(4, 0)],
        5: []
    },
    'MAP_ROUTE116': {
        0: [],
        1: [],
        2: []
    },
    'MAP_ROUTE120': {
        0: [WT(1, 9216)],
        1: [WT(0, 8192)]
    },
    'MAP_UNDERWATER_ROUTE127': {
        0: [],
        1: []
    },
    'MAP_UNDERWATER_ROUTE129': {
        0: [],
        1: []
    },
    'MAP_UNDERWATER_ROUTE105': {
        0: [],
        1: []
    },
    'MAP_UNDERWATER_ROUTE125': {
        0: [],
        1: []
    },
    'MAP_EVER_GRANDE_CITY_SIDNEYS_ROOM': {
        0: [WT(1, 0)],
        1: []
    },
    'MAP_EVER_GRANDE_CITY_PHOEBES_ROOM': {
        0: [WT(1, 0)],
        1: []
    },
    'MAP_EVER_GRANDE_CITY_GLACIAS_ROOM': {
        0: [WT(1, 0)],
        1: []
    },
    'MAP_EVER_GRANDE_CITY_DRAKES_ROOM': {
        0: [WT(1, 0)],
        1: []
    },
    'MAP_METEOR_FALLS_1F_1R': {
        0: [WT(1, 0), WT(2, 525312)],
        1: [WT(0, 0), WT(2, 525312)],
        2: [WT(0, 1024), WT(1, 1024)],
        3: [WT(5, 0)],
        4: [],
        5: [WT(3, 0)]
    },
    'MAP_METEOR_FALLS_1F_2R': {
        1: [WT(0, 0), WT(2, 0), WT(3, 0)],
        2: [WT(0, 0), WT(3, 0)],
        0: [WT(3, 0)],
        3: [WT(0, 0)]
    },
    'MAP_METEOR_FALLS_B1F_1R': {
        0: [WT(2, 0), WT(4, 0)],
        1: [WT(3, 1024), WT(5, 1024)],
        2: [WT(0, 0), WT(4, 0)],
        3: [WT(1, 1024), WT(5, 1024)],
        4: [WT(0, 0), WT(2, 0)],
        5: [WT(1, 1024), WT(3, 1024)]
    },
    'MAP_RUSTURF_TUNNEL': {
        0: [WT(1, 16), WT(2, 16)],
        1: [WT(0, 16), WT(2, 0)],
        2: [WT(0, 16), WT(1, 0)]
    },
    'MAP_DESERT_RUINS': {
        0: [WT(1, 16)],
        1: [WT(0, 0)],
        2: []
    },
    'MAP_GRANITE_CAVE_1F': {
        0: [WT(2, 0)],
        1: [WT(0, 0), WT(2, 0), WT(3, 0)],
        2: [WT(0, 0)],
        3: [WT(0, 0), WT(1, 0), WT(2, 0)]
    },
    'MAP_GRANITE_CAVE_B1F': {
        0: [WT(2, 0)],
        2: [WT(0, 0)],
        1: [WT(3, 0), WT(4, 32), WT(5, 32), WT(6, 32)],
        3: [WT(1, 0), WT(4, 32), WT(5, 32), WT(6, 32)],
        4: [WT(3, 0), WT(1, 0), WT(5, 32), WT(6, 32)],
        5: [WT(3, 32), WT(4, 32), WT(1, 32), WT(6, 32)],
        6: [WT(3, 32), WT(4, 32), WT(5, 32), WT(1, 32)]
    },
    'MAP_GRANITE_CAVE_B2F': {
        0: [WT(1, 0)],
        1: [WT(0, 0)],
        4: [],
        2: [],
        3: [WT(2, 0)]
    },
    'MAP_MT_CHIMNEY': {
        0: [WT(1, 0), WT(2, 128), WT(3, 128)],
        1: [WT(0, 0), WT(2, 128), WT(3, 128)],
        2: [WT(0, 128), WT(1, 128), WT(3, 0)],
        3: [WT(0, 128), WT(1, 128), WT(2, 0)],
    },
    'MAP_JAGGED_PASS':{
        0: [WT(1, 0), WT(2, 32), WT(3, 32), WT(4, 16416)],
        1: [WT(0, 0), WT(2, 32), WT(3, 32), WT(4, 16416)],
        2: [WT(0, 0), WT(1, 0), WT(3, 0), WT(4, 16384)],
        3: [WT(0, 0), WT(1, 0), WT(2, 0), WT(4, 16384)],
        4: [WT(0, 0), WT(1, 0), WT(2, 32), WT(3, 32)]
    },
    'MAP_MT_PYRE_1F': {
        0: [WT(1, 0), WT(2, 0), WT(3, 0), WT(4, 0)],
        1: [WT(0, 0), WT(2, 0), WT(3, 0), WT(4, 0)],
        2: [WT(1, 0), WT(0, 0), WT(3, 0), WT(4, 0)],
        3: [WT(1, 0), WT(2, 0), WT(0, 0), WT(4, 0)],
        4: [WT(1, 0), WT(2, 0), WT(3, 0), WT(0, 0)],
        5: [WT(1, 0), WT(2, 0), WT(3, 0), WT(4, 0), WT(0, 0)]
    },
    'MAP_MT_PYRE_2F': {
        0: [WT(1, 0), WT(4, 0)],
        1: [WT(0, 0), WT(4, 0)],
        4: [WT(1, 0), WT(0, 0)],
        2: [WT(0, 0), WT(1, 0), WT(4, 0)],
        3: [WT(0, 0), WT(1, 0), WT(4, 0)],
    },
    'MAP_MT_PYRE_3F': {
        0: [WT(1, 0), WT(4, 0)],
        1: [WT(0, 0), WT(4, 0)],
        4: [WT(1, 0), WT(0, 0)],
        2: [WT(0, 0), WT(1, 0), WT(4, 0)],
        3: [WT(5, 0)],
        5: []
    },
    'MAP_MT_PYRE_4F': {
        0: [WT(1, 0), WT(4, 0)],
        1: [WT(0, 0), WT(4, 0)],
        4: [WT(1, 0), WT(0, 0)],
        2: [WT(0, 0), WT(1, 0), WT(4, 0)],
        3: [WT(5, 0)],
        5: []
    },
    'MAP_MT_PYRE_5F': {
        0: [WT(1, 0)],
        1: [WT(0, 0)],
        4: [WT(3, 0)],
        2: [WT(3, 0), WT(4, 0)],
        3: [WT(4, 0)]
    },
    'MAP_AQUA_HIDEOUT_B1F': {
        0: [WT(5, 0), WT(4, 0)],
        4: [WT(5, 0), WT(0, 0)],
        5: [WT(0, 0), WT(4, 0)],
        1: [WT(6, 0)],
        6: [WT(1, 0)],
        2: [WT(3, 0)],
        3: [WT(2, 0)],
        8: [WT(9, 0), WT(10, 0)],
        9: [WT(8, 0), WT(10, 0)],
        10: [WT(9, 0), WT(8, 0)],
        12: [WT(13, 0), WT(14, 0), WT(15, 0)],
        13: [WT(12, 0), WT(14, 0), WT(15, 0)],
        14: [WT(13, 0), WT(12, 0), WT(15, 0)],
        15: [WT(13, 0), WT(14, 0), WT(12, 0)],
        16: [WT(17, 0)],
        17: [WT(16, 0), WT(18, 0)],
        18: [WT(17, 0)],
        19: [WT(20, 0)],
        20: [WT(19, 0), WT(21, 0)],
        21: [WT(20, 0)],
        22: [WT(23, 0), WT(24, 0)],
        23: [WT(22, 0), WT(24, 0)],
        24: [WT(23, 0), WT(22, 0)],
        7: [],
        11: []
    },
    'MAP_AQUA_HIDEOUT_B2F': {
        0: [WT(6, 0), WT(3, 0)],
        3: [WT(6, 0), WT(0, 0)],
        6: [WT(0, 0), WT(3, 0)],
        1: [WT(4, 0)],
        4: [WT(1, 0)],
        2: [WT(5, 0)],
        5: [WT(2, 0)],
        7: [],
        8: [WT(9, 0)],
        9: [WT(8, 0)],
    },
    'MAP_SEAFLOOR_CAVERN_ROOM1': {
        0: [WT(1, 528), WT(2, 528)],
        1: [WT(0, 512), WT(2, 0)],
        2: [WT(1, 0), WT(0, 512)]
    },
    'MAP_SEAFLOOR_CAVERN_ROOM2': {
        0: [WT(1, 528), WT(2, 528), WT(3, 528)],
        1: [WT(0, 528), WT(2, 512), WT(3, 528)],
        2: [WT(1, 512), WT(0, 528), WT(3, 528)],
        3: []
    },
    'MAP_SEAFLOOR_CAVERN_ROOM4': {
        0: [WT(2, 0), WT(3, 0)],
        1: [WT(0, 0), WT(2, 0), WT(3, 0)],
        2: [WT(0, 0), WT(3, 0)],
        3: []
    },
    'MAP_SEAFLOOR_CAVERN_ROOM5': {
        0: [WT(1, 528), WT(2, 528)],
        1: [WT(0, 512), WT(2, 528)],
        2: [WT(1, 528), WT(0, 528)]
    },
    'MAP_SEAFLOOR_CAVERN_ROOM6': {
        0: [WT(1, 1024), WT(2, 1024)],
        1: [WT(2, 1024)],
        2: []
    },
    'MAP_SEAFLOOR_CAVERN_ROOM7': {
        0: [WT(1, 1024)],
        1: [WT(0, 1024)]
    },
    'MAP_SEAFLOOR_CAVERN_ROOM8': {
        0: [WT(1, 512)],
        1: [WT(0, 512)]
    },
    'MAP_VICTORY_ROAD_1F': {
        0: [WT(4, 0)],
        4: [WT(0, 0)],
        1: [WT(2, 0)],
        2: [WT(1, 0)],
        3: []
    },
    'MAP_VICTORY_ROAD_B1F': {
        0: [WT(4, 16), WT(2, 528)],
        4: [WT(0, 528), WT(2, 528)],
        2: [WT(0, 0), WT(4, 16)],
        3: [],
        1: [WT(6, 0), WT(5, 528)],
        6: [WT(1, 0), WT(5, 528)],
        5: [WT(6, 528), WT(1, 528)]
    },
    'MAP_VICTORY_ROAD_B2F': {
        0: [WT(1, 1024), WT(2, 1024), WT(3, 1024)],
        1: [WT(0, 0), WT(2, 1024), WT(3, 1024)],
        2: [WT(1, 524816), WT(0, 524816), WT(3, 1024)],
        3: [WT(1, 524816), WT(2, 1024), WT(0, 524816)]
    },
    'MAP_ABANDONED_SHIP_DECK': {
        0: [WT(1, 0), WT(2, 0)],
        1: [WT(0, 0), WT(2, 0)],
        2: [WT(1, 0), WT(0, 0)],
        3: [WT(4, 0)],
        4: [WT(3, 0)]
    },
    'MAP_ABANDONED_SHIP_CORRIDORS_1F': {
        0: [WT(1, 0), WT(4, 0), WT(5, 0), WT(6, 0), WT(7, 0), WT(9, 0)],
        1: [WT(0, 0), WT(4, 0), WT(5, 0), WT(6, 0), WT(7, 0), WT(9, 0)],
        4: [WT(0, 0), WT(0, 0), WT(5, 0), WT(6, 0), WT(7, 0), WT(9, 0)],
        5: [WT(0, 0), WT(4, 0), WT(0, 0), WT(6, 0), WT(7, 0), WT(9, 0)],
        6: [WT(0, 0), WT(4, 0), WT(5, 0), WT(0, 0), WT(7, 0), WT(9, 0)],
        7: [WT(0, 0), WT(4, 0), WT(5, 0), WT(6, 0), WT(0, 0), WT(9, 0)],
        9: [WT(0, 0), WT(4, 0), WT(5, 0), WT(6, 0), WT(7, 0), WT(0, 0)],
        2: [WT(8, 0), WT(10, 0), WT(11, 0)],
        8: [WT(0, 0), WT(10, 0), WT(11, 0)],
        10: [WT(8, 0), WT(0, 0), WT(11, 0)],
        11: [WT(8, 0), WT(10, 0), WT(0, 0)]
    },
    'MAP_ABANDONED_SHIP_ROOMS_1F': {
        0: [WT(1, 0), WT(3, 0), WT(4, 0), WT(5, 0)],
        1: [WT(0, 0), WT(3, 0), WT(4, 0), WT(5, 0)],
        3: [WT(1, 0), WT(0, 0), WT(4, 0), WT(5, 0)],
        4: [WT(1, 0), WT(3, 0), WT(0, 0), WT(5, 0)],
        5: [WT(1, 0), WT(3, 0), WT(4, 0), WT(0, 0)],
        2: []
    },
    'MAP_ABANDONED_SHIP_CORRIDORS_B1F': {
        0: [WT(1, 0), WT(2, 0), WT(3, 0), WT(4, 0), WT(6, 0), WT(7, 0)],
        1: [WT(0, 0), WT(2, 0), WT(3, 0), WT(4, 0), WT(6, 0), WT(7, 0)],
        2: [WT(1, 0), WT(0, 0), WT(3, 0), WT(4, 0), WT(6, 0), WT(7, 0)],
        3: [WT(1, 0), WT(2, 0), WT(0, 0), WT(4, 0), WT(6, 0), WT(7, 0)],
        4: [WT(1, 0), WT(2, 0), WT(3, 0), WT(0, 0), WT(6, 0), WT(7, 0)],
        5: [WT(1, 0), WT(2, 0), WT(3, 0), WT(4, 0), WT(6, 0), WT(7, 0)],
        6: [WT(1, 0), WT(2, 0), WT(3, 0), WT(4, 0), WT(0, 0), WT(7, 0)],
        7: [WT(1, 0), WT(2, 0), WT(3, 0), WT(4, 0), WT(6, 0), WT(0, 0)],
    },
    'MAP_ABANDONED_SHIP_ROOMS_B1F': {
        0: [],
        1: [],
        2: []
    },
    'MAP_ISLAND_CAVE': {
            0: [WT(1, 0)],
            1: [WT(0, 0)],
            2: []
        },
    'MAP_ANCIENT_TOMB': {
        0: [WT(1, 4)],
        1: [WT(0, 0)],
        2: []
    },
    'MAP_SKY_PILLAR_OUTSIDE': {
        0: [WT(1, 131072)],
        1: [WT(0, 0)],
    },
    'MAP_SKY_PILLAR_2F': {
        0: [WT(1, 32)],
        1: [WT(0, 32)],
    },
    'MAP_SKY_PILLAR_3F': {
        0: [WT(1, 0)],
        1: [WT(0, 0)],
        2: []
    },
    'MAP_SKY_PILLAR_4F': {
        1: [WT(2, 0)],
        2: [WT(1, 0)],
        0: []
    },
    'MAP_MAGMA_HIDEOUT_1F': {
        0: [WT(1, 512)],
        1: [WT(0, 512)],
        2: [],
        3: [WT(0, 512), WT(1, 0)]
    },
    'MAP_MIRAGE_TOWER_2F': {
        0: [WT(1, 32)],
        1: [WT(0, 32)],
    },
    'MAP_MIRAGE_TOWER_3F': {
        0: [WT(1, 16)],
        1: [WT(0, 16)],
    },
    'MAP_EVER_GRANDE_CITY_POKEMON_LEAGUE_1F': {
        0: [WT(1, 0), WT(2, 595478), WT(3, 595478), WT(4, 0)],
        1: [WT(0, 0), WT(2, 595478), WT(3, 595478), WT(4, 0)],
        2: [WT(1, 595478), WT(0, 595478), WT(3, 595478), WT(4, 595478)],
        3: [WT(1, 595478), WT(2, 595478), WT(0, 595478), WT(4, 595478)],
        4: [WT(1, 0), WT(2, 595478), WT(3, 595478), WT(0, 0)]
    }
}

# Basically we define the easiest warp to reach from one map to the next map (i.e. connections)
# We only need to define the easiest warp because once we define the easiest we can then know what it takes to get from
# that warp to all other warps based off map_warp_accessibility
# if not defined we can assume warp 0 is the easiest to reach with 0 flag requirements
map_to_map_warp_accessibility = {
    'MAP_ROUTE115': {
        'MAP_RUSTBORO_CITY': WT(0, 1024)
    },
    'MAP_ROUTE104': {
        'MAP_RUSTBORO_CITY': WT(1, 0)
    },
    'MAP_ROUTE110': {
        'MAP_MAUVILLE_CITY': WT(2, 0),
        'MAP_SLATEPORT_CITY': WT(4, 0)
    },
    'MAP_ROUTE111': {
        'MAP_ROUTE113': WT(2, 0)
    },
    'MAP_ROUTE112': {
        'MAP_ROUTE111': WT(4, 0),
        'MAP_LAVARIDGE_TOWN': WT(4, 0)
    },
    'MAP_ROUTE122': {
        'MAP_ROUTE121': WT(1024, 0)
    },
    'MAP_EVER_GRANDE_CITY': {
        'MAP_ROUTE128': WT(525312, 1)
    }
}

cant_go_back_warps = {
    'MAP_SOOTOPOLIS_CITY': [2],
    'MAP_EVER_GRANDE_CITY_SIDNEYS_ROOM': [0],
    'MAP_EVER_GRANDE_CITY_PHOEBES_ROOM': [0],
    'MAP_EVER_GRANDE_CITY_GLACIAS_ROOM': [0],
    'MAP_EVER_GRANDE_CITY_DRAKES_ROOM': [0],
    'MAP_DESERT_RUINS': [1],
    'MAP_JAGGED_PASS': [4],
    'MAP_MT_PYRE_1F': [5],
    'MAP_MT_PYRE_2F': [2, 3],
    'MAP_MT_PYRE_3F': [2, 3],
    'MAP_MT_PYRE_4F': [2, 3],
    'MAP_MT_PYRE_5F': [2],
    'MAP_ABANDONED_SHIP_CORRIDORS_B1F': [5],
    'MAP_ISLAND_CAVE': [1],
    'MAP_ANCIENT_TOMB': [1]
}

# Handles Connection Requirements
goggles_needed = ['MAP_ROUTE111']
rocksmash_needed = ['MAP_ROUTE111']
oceanic_museum_needed = ['MAP_ROUTE110']
cut_needed = ['MAP_ROUTE121']
surf_needed = ['MAP_ROUTE103', 'MAP_ROUTE105', 'MAP_ROUTE107', 'MAP_ROUTE108', 'MAP_ROUTE118',
               'MAP_ROUTE122', 'MAP_ROUTE124', 'MAP_ROUTE125', 'MAP_ROUTE126', 'MAP_ROUTE127', 'MAP_ROUTE128',
               'MAP_ROUTE129', 'MAP_ROUTE130', 'MAP_ROUTE131', 'MAP_ROUTE132', 'MAP_ROUTE133', 'MAP_ROUTE134']
dive_needed = ['MAP_ROUTE126', 'MAP_UNDERWATER_ROUTE124', 'MAP_UNDERWATER_ROUTE126', 'MAP_UNDERWATER_ROUTE127',
               'MAP_UNDERWATER_ROUTE128', 'MAP_UNDERWATER_ROUTE129', 'MAP_UNDERWATER_ROUTE105',
               'MAP_UNDERWATER_ROUTE125', 'UNDERWATER', 'MAP_MARINE_CAVE_ENTRANCE']

dont_randomize = ['LITTLEROOT_TOWN', 'MAP_EVER_GRANDE_CITY_HALL_OF_FAME', 'MAP_LAVARIDGE_TOWN_GYM_B1F', 'TRAINER_HILL',
                  'SAFARI_ZONE', 'LILYCOVE_MUSEUM', 'MAP_LILYCOVE_CITY_DEPARTMENT_STORE_ELEVATOR', 'SHOAL_CAVE',
                  'MAP_MARINE_CAVE_ENTRANCE', 'MAP_TERRA_CAVE_ENTRANCE',
                  'MAP_SOOTOPOLIS_CITY_GYM_B1F', 'MAP_ALTERING_CAVE', 'MAP_UNDERWATER_MARINE_CAVE',
                  'MAP_DESERT_UNDERPASS', 'MAP_SEALED_CHAMBER_INNER_ROOM', 'MAP_UNDERWATER_SOOTOPOLIS_CITY',
                  'MAP_UNDERWATER_SEAFLOOR_CAVERN']

dont_randomize_warp = {'MAP_SOOTOPOLIS_CITY': [3], 'MAP_SLATEPORT_CITY_HARBOR': [2, 3], 'MAP_ROUTE131': [0],
                       'MAP_SLATEPORT_CITY': [9]}

not_needed = ['MAP_OLDALE_TOWN_HOUSE1', 'MAP_OLDALE_TOWN_HOUSE2', 'MAP_OLDALE_TOWN_POKEMON_CENTER_2F',
              'MAP_OLDALE_TOWN_POKEMON_CENTER_2F', 'MAP_ALTERING_CAVE', 'MAP_ROUTE110_TRICK_HOUSE_ENTRANCE',
              'MAP_MAUVILLE_CITY_POKEMON_CENTER_2F', 'MAP_MAUVILLE_CITY_POKEMON_CENTER_2F', 'MAP_MAUVILLE_CITY_HOUSE2',
              'MAP_ROUTE111_WINSTRATE_FAMILYS_HOUSE', 'MAP_ROUTE111_OLD_LADYS_REST_STOP', 'MAP_ROUTE113_GLASS_WORKSHOP',
              'MAP_LAVARIDGE_TOWN_POKEMON_CENTER_2F', 'MAP_LAVARIDGE_TOWN_POKEMON_CENTER_2F',
              'MAP_LAVARIDGE_TOWN_HOUSE', 'MAP_FALLARBOR_TOWN_BATTLE_TENT_LOBBY',
              'MAP_FALLARBOR_TOWN_POKEMON_CENTER_2F', 'MAP_FALLARBOR_TOWN_POKEMON_CENTER_2F',
              'MAP_FALLARBOR_TOWN_COZMOS_HOUSE', 'MAP_RUSTBORO_CITY_FLAT1_2F', 'MAP_RUSTBORO_CITY_POKEMON_CENTER_2F',
              'MAP_RUSTBORO_CITY_POKEMON_CENTER_2F', 'MAP_RUSTBORO_CITY_HOUSE1', 'MAP_RUSTBORO_CITY_HOUSE2',
              'MAP_RUSTBORO_CITY_FLAT2_3F', 'MAP_RUSTBORO_CITY_HOUSE3', 'MAP_ROUTE104_PRETTY_PETAL_FLOWER_SHOP',
              'MAP_DEWFORD_TOWN_HALL', 'MAP_DEWFORD_TOWN_POKEMON_CENTER_2F', 'MAP_DEWFORD_TOWN_POKEMON_CENTER_2F',
              'MAP_DEWFORD_TOWN_HOUSE1', 'MAP_DEWFORD_TOWN_HOUSE2', 'MAP_SLATEPORT_CITY_POKEMON_CENTER_2F',
              'MAP_SLATEPORT_CITY_BATTLE_TENT_LOBBY', 'MAP_SLATEPORT_CITY_POKEMON_FAN_CLUB',
              'MAP_SLATEPORT_CITY_NAME_RATERS_HOUSE', 'MAP_SLATEPORT_CITY_HOUSE',
              'MAP_PACIFIDLOG_TOWN_POKEMON_CENTER_2F', 'MAP_PACIFIDLOG_TOWN_POKEMON_CENTER_2F',
              'MAP_PACIFIDLOG_TOWN_HOUSE1', 'MAP_PACIFIDLOG_TOWN_HOUSE2', 'MAP_PACIFIDLOG_TOWN_HOUSE3',
              'MAP_PACIFIDLOG_TOWN_HOUSE4', 'MAP_PACIFIDLOG_TOWN_HOUSE5', 'MAP_MOSSDEEP_CITY_HOUSE1',
              'MAP_MOSSDEEP_CITY_POKEMON_CENTER_2F', 'MAP_MOSSDEEP_CITY_POKEMON_CENTER_2F', 'MAP_MOSSDEEP_CITY_HOUSE2',
              'MAP_MOSSDEEP_CITY_HOUSE3', 'MAP_MOSSDEEP_CITY_HOUSE4', 'MAP_SHOAL_CAVE_LOW_TIDE_ICE_ROOM',
              'MAP_ROUTE124_DIVING_TREASURE_HUNTERS_HOUSE', 'MAP_SOOTOPOLIS_CITY_POKEMON_CENTER_2F',
              'MAP_SOOTOPOLIS_CITY_POKEMON_CENTER_2F', 'MAP_SOOTOPOLIS_CITY_HOUSE1',
              'MAP_SOOTOPOLIS_CITY_HOUSE2', 'MAP_SOOTOPOLIS_CITY_HOUSE3', 'MAP_SOOTOPOLIS_CITY_HOUSE4',
              'MAP_SOOTOPOLIS_CITY_HOUSE5', 'MAP_SOOTOPOLIS_CITY_HOUSE6', 'MAP_SOOTOPOLIS_CITY_HOUSE7',
              'MAP_SOOTOPOLIS_CITY_LOTAD_AND_SEEDOT_HOUSE', 'MAP_SOOTOPOLIS_CITY_MYSTERY_EVENTS_HOUSE_B1F',
              'MAP_LILYCOVE_CITY_COVE_LILY_MOTEL_2F', 'MAP_LILYCOVE_CITY_POKEMON_CENTER_2F',
              'MAP_LILYCOVE_CITY_POKEMON_CENTER_2F', 'MAP_SOOTOPOLIS_CITY_MYSTERY_EVENTS_HOUSE_1F',
              'MAP_LILYCOVE_CITY_POKEMON_TRAINER_FAN_CLUB', 'MAP_LILYCOVE_CITY_HOUSE1', 'MAP_LILYCOVE_CITY_HOUSE2',
              'MAP_LILYCOVE_CITY_HOUSE3', 'MAP_LILYCOVE_CITY_HOUSE4', 'MAP_LILYCOVE_CITY_HARBOR',
              'MAP_SAFARI_ZONE_REST_HOUSE', 'MAP_ROUTE123_BERRY_MASTERS_HOUSE',
              'MAP_ROUTE119_HOUSE', 'MAP_FORTREE_CITY_POKEMON_CENTER_2F', 'MAP_FORTREE_CITY_POKEMON_CENTER_2F',
              'MAP_FORTREE_CITY_HOUSE1', 'MAP_MOSSDEEP_CITY_MART', 'MAP_FORTREE_CITY_MART', 'MAP_FORTREE_CITY_HOUSE2',
              'MAP_FORTREE_CITY_HOUSE3', 'MAP_FORTREE_CITY_HOUSE4', 'MAP_FORTREE_CITY_HOUSE5',
              'MAP_FORTREE_CITY_DECORATION_SHOP', 'MAP_ANCIENT_TOMB', 'MAP_SCORCHED_SLAB',
              'MAP_EVER_GRANDE_CITY_HALL_OF_FAME', 'MAP_EVER_GRANDE_CITY_POKEMON_LEAGUE_2F',
              'MAP_EVER_GRANDE_CITY_POKEMON_LEAGUE_2F', 'MAP_EVER_GRANDE_CITY_POKEMON_CENTER_2F',
              'MAP_EVER_GRANDE_CITY_POKEMON_CENTER_2F', 'MAP_PETALBURG_CITY_HOUSE1',
              'MAP_PETALBURG_CITY_POKEMON_CENTER_2F', 'MAP_PETALBURG_CITY_HOUSE2',
              'MAP_VERDANTURF_TOWN_BATTLE_TENT_LOBBY', 'MAP_VERDANTURF_TOWN_MART',
              'MAP_VERDANTURF_TOWN_POKEMON_CENTER_2F', 'MAP_VERDANTURF_TOWN_POKEMON_CENTER_2F',
              'MAP_VERDANTURF_TOWN_WANDAS_HOUSE', 'MAP_VERDANTURF_TOWN_FRIENDSHIP_RATERS_HOUSE', ''
              'MAP_VERDANTURF_TOWN_HOUSE', 'MAP_ROUTE117_POKEMON_DAY_CARE', 'MAP_ROUTE116_TUNNELERS_REST_HOUSE',
              'MAP_ROUTE114_LANETTES_HOUSE', 'MAP_BIRTH_ISLAND_EXTERIOR', 'MAP_SHOAL_CAVE_HIGH_TIDE_ENTRANCE_ROOM',
              'MAP_UNDERWATER_MARINE_CAVE', 'MAP_NAVEL_ROCK_EXTERIOR',
              'MAP_FARAWAY_ISLAND_ENTRANCE', 'MAP_SHOAL_CAVE_HIGH_TIDE_INNER_ROOM', 'MAP_LILYCOVE_CITY_CONTEST_HALL',
              'MAP_EVER_GRANDE_CITY_HALL1', 'MAP_EVER_GRANDE_CITY_HALL2', 'MAP_EVER_GRANDE_CITY_HALL3',
              'MAP_EVER_GRANDE_CITY_HALL4', 'MAP_EVER_GRANDE_CITY_HALL5', 'MAP_AQUA_HIDEOUT_1F',
              'MAP_RUSTBORO_CITY_DEVON_CORP_1F', 'MAP_MOSSDEEP_CITY_GAME_CORNER_1F',
              'MAP_MOSSDEEP_CITY_GAME_CORNER_B1F', 'MAP_SEAFLOOR_CAVERN_ENTRANCE', 'MAP_NEW_MAUVILLE_ENTRANCE',
              'MAP_ABANDONED_SHIP_HIDDEN_FLOOR_CORRIDORS', 'MAP_ABANDONED_SHIP_HIDDEN_FLOOR_ROOMS',
              'MAP_ROUTE110_TRICK_HOUSE_PUZZLE1', 'MAP_ROUTE110_TRICK_HOUSE_CORRIDOR']

non_navigable_connections = [['MAP_VERDANTURF_TOWN', 'MAP_ROUTE116'], ['MAP_ROUTE104', 'MAP_RUSTBORO_CITY'],
                             ['MAP_ROUTE116', 'MAP_VERDANTURF_TOWN'], ['MAP_PETALBURG_CITY', 'MAP_ROUTE104'],
                             ['MAP_ROUTE112', 'MAP_ROUTE113', 'MAP_LAVARIDGE_TOWN'],
                             ['MAP_ROUTE113', 'MAP_ROUTE112'], ['MAP_ROUTE114', 'MAP_ROUTE115'],
                             ['MAP_ROUTE115', 'MAP_ROUTE114'], ['MAP_ROUTE123', 'MAP_ROUTE122'],
                             ['MAP_ROUTE124', 'MAP_ROUTE125', 'MAP_ROUTE126'], ['MAP_ROUTE126', 'MAP_ROUTE124'],
                             ['MAP_ROUTE125', 'MAP_ROUTE124'], ['MAP_ROUTE134', 'MAP_ROUTE133'],
                             ['MAP_EVER_GRANDE_CITY', 'MAP_ROUTE128']]

connection_to_connection_rules = {
    'MAP_ROUTE104': {'MAP_ROUTE105': 1024},
    'MAP_ROUTE106': {'MAP_ROUTE105': 1024},
    'MAP_DEWFORD_TOWN': {'MAP_ROUTE107': 1024},
    'MAP_ROUTE109': {'MAP_ROUTE108': 1024},
    'MAP_ROUTE121': {'MAP_ROUTE122': 1024},
    'MAP_LILYCOVE_CITY': {'MAP_ROUTE124': 1024},
    'MAP_MOSSDEEP_CITY': {'MAP_ROUTE124': 1024, 'MAP_ROUTE125': 1024, 'MAP_ROUTE127': 1024},
    'MAP_SLATEPORT_CITY': {'MAP_ROUTE124': 134},
    'MAP_PACIFIDLOG_TOWN': {'MAP_ROUTE131': 1024, 'MAP_ROUTE132': 1024}
}


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


def check_progession_blockers(flag, accesible_maps):
    if flag == TUTORIAL_FLAG:
        return search_for_needed_maps(tutorial_event, accesible_maps)
    elif flag == CUT_FLAG:
        return search_for_needed_maps(cut_event, accesible_maps)
    elif flag == FLASH_FLAG:
        return search_for_needed_maps(flash_event, accesible_maps)
    elif flag == OCEANIC_MUSEUM_FLAG:
        return search_for_needed_maps(oceanic_museum_event, accesible_maps)
    elif flag == ROCKSMASH_FLAG:
        return search_for_needed_maps(rocksmash_event, accesible_maps)
    elif flag == BIKE_FLAG:
        return search_for_needed_maps(bike_event, accesible_maps)
    elif flag == METEOR_FALLS_FLAG:
        return search_for_needed_maps(meteor_falls_event, accesible_maps)
    elif flag == MT_CHIMNEY_FLAG:
        return search_for_needed_maps(mt_chimney_event, accesible_maps)
    elif flag == GOGGLES_FLAG:
        return search_for_needed_maps(goggles_event, accesible_maps)
    elif flag == STRENGTH_FLAG:
        return search_for_needed_maps(strength_event, accesible_maps)
    elif flag == SURF_FLAG:
        return search_for_needed_maps(surf_event, accesible_maps)
    elif flag == WEATHER_INSTITUTE_FLAG:
        return search_for_needed_maps(weather_institute_event, accesible_maps)
    elif flag == FLY_FLAG:
        return search_for_needed_maps(fly_event, accesible_maps)
    elif flag == DEVON_SCOPE_FLAG:
        return search_for_needed_maps(devon_scope_event, accesible_maps)
    elif flag == SUMMIT_FLAG:
        return search_for_needed_maps(summit_event, accesible_maps)
    elif flag == LEGENDARIES_BATTLE_FLAG:
        return search_for_needed_maps(legendaries_battle_event, accesible_maps)
    elif flag == DIVE_FLAG:
        return search_for_needed_maps(dive_event, accesible_maps)
    elif flag == CAVE_OF_ORIGIN_FLAG:
        return search_for_needed_maps(cave_of_origin_event, accesible_maps)
    elif flag == END_STORY_FLAG:
        return search_for_needed_maps(end_story_event, accesible_maps)
    elif flag == WATERFALL_FLAG:
        return search_for_needed_maps(waterfall_event, accesible_maps)
    else:
        return False


# If warp_id = -1 we check connection, otherwise we check if there is an accessible warp from warp id
def is_map_progressable(map, accesible_maps, warp_id, ignore=False):
    if not check_progession_blockers(SURF_FLAG, accesible_maps) and map in surf_needed:
        return False
    if not check_progession_blockers(GOGGLES_FLAG, accesible_maps) and map in goggles_needed:
        return False
    if not check_progession_blockers(ROCKSMASH_FLAG, accesible_maps) and map in rocksmash_needed:
        return False
    if not check_progession_blockers(DIVE_FLAG, accesible_maps) and map in dive_needed:
        return False
    if not check_progession_blockers(DIVE_FLAG, accesible_maps):
        for dive_need in dive_needed:
            if dive_need in map:
                return False
    if not check_progession_blockers(OCEANIC_MUSEUM_FLAG, accesible_maps) and map in oceanic_museum_needed:
        return False
    if not check_progession_blockers(CUT_FLAG, accesible_maps) and map in cut_needed:
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
