"""
FireRedWarpMapInfo.py

Pokemon FRLG warp randomizer rules definitions

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
POKEDEX_FLAG = 0
FLASH_FLAG = 1
CUT_FLAG = 2
TEA_FLAG = 3
FLY_FLAG = 4
STRENGTH_EVENT = 5
SILPH_SCOPE_EVENT = 6
POKEFLUTE_EVENT = 7
SILPHCO_CARD_KEY_EVENT = 8
GIOVANNI_SILPHCO_EVENT = 9
ROCKSMASH_EVENT = 10
BIKE_EVENT = 11
SURF_EVENT = 12
MANSION_EVENT = 13
GYM8_UNLOCK_EVENT = 14
GYM8_EVENT = 15

END_FLAG = GYM8_EVENT

pokedex_event = ['MAP_VIRIDIAN_CITY_MART']
flash_event = ['MAP_PEWTER_CITY_GYM', 'MAP_ROUTE2_EAST_BUILDING']
cut_event = ['MAP_CERULEAN_CITY_GYM', 'MAP_ROUTE25_SEA_COTTAGE', 'MAP_SSANNE_CAPTAINS_OFFICE']
tea_event = ['MAP_CELADON_CITY_CONDOMINIUMS_1F:0:1:2:4']
fly_event = ['MAP_VERMILION_CITY_GYM', 'MAP_ROUTE16_HOUSE']
strength_event = ['MAP_CELADON_CITY_GYM', 'MAP_CERULEAN_CITY_GYM', 'MAP_ROUTE25_SEA_COTTAGE',
                  'MAP_SSANNE_CAPTAINS_OFFICE', 'MAP_FUCHSIA_CITY_SAFARI_ZONE_ENTRANCE',
                  'MAP_FUCHSIA_CITY_WARDENS_HOUSE']
silph_scope_event = ['MAP_ROCKET_HIDEOUT_B4F:0', 'MAP_ROCKET_HIDEOUT_B2F']
poke_flute_event = ['MAP_POKEMON_TOWER_7F', 'MAP_LAVENDER_TOWN_VOLUNTEER_POKEMON_HOUSE']
silphco_card_key_event = ['MAP_SILPH_CO_5F:3']
giovanni_silphco_event = ['MAP_SILPH_CO_5F:3', 'MAP_SILPH_CO_11F:1']
rocksmash_event = ['MAP_SAFFRON_CITY_GYM']  # , 'MAP_ONE_ISLAND_KINDLE_ROAD_EMBER_SPA'] TODO re-add when enable sevii
bike_event = ['MAP_VERMILION_CITY_POKEMON_FAN_CLUB', 'MAP_CERULEAN_CITY_BIKE_SHOP']
surf_event = ['MAP_SAFFRON_CITY_GYM', 'MAP_FUCHSIA_CITY_GYM', 'MAP_FUCHSIA_CITY_SAFARI_ZONE_ENTRANCE']
mansion_event = ['MAP_POKEMON_MANSION_B1F']
gym8_unlock_event = ['MAP_PEWTER_CITY_GYM', 'MAP_VERMILION_CITY_GYM', 'MAP_CELADON_CITY_GYM', 'MAP_SAFFRON_CITY_GYM',
                     'MAP_CERULEAN_CITY_GYM', 'MAP_FUCHSIA_CITY_GYM', 'MAP_CINNABAR_ISLAND_GYM']
gym8_event = ['MAP_VIRIDIAN_CITY_GYM']


FORCED_FLAG_ORDER = [POKEDEX_FLAG, FLASH_FLAG, CUT_FLAG, FLY_FLAG, STRENGTH_EVENT, SURF_EVENT, ROCKSMASH_EVENT,
                     GYM8_UNLOCK_EVENT, GYM8_EVENT]
FLAG_EVENT_LIST = [pokedex_event, flash_event, cut_event, tea_event, fly_event, strength_event, silph_scope_event,
                   poke_flute_event, silphco_card_key_event, giovanni_silphco_event, rocksmash_event, bike_event,
                   surf_event, mansion_event, gym8_unlock_event, gym8_event]

no_event_allowed = []
map_chain_breaks = []

# Event Based Warps and Warp Connections
# If map not specified, assume that all warps are accessible
map_warp_accessibility = {
    'MAP_MT_MOON_B1F': {
        0: [WT(3, 0)],
        1: [WT(4, 0)],
        2: [WT(5, 0)],
        3: [WT(0, 0)],
        4: [WT(1, 0)],
        5: [WT(2, 0)],
        6: [WT(7, 0)],
        7: [WT(6, 0)]
    },
    'MAP_MT_MOON_B2F': {
        0: [WT(3, 0)],
        1: [],
        2: [],
        3: [WT(0, 0)]
    },
    'MAP_VICTORY_ROAD_1F': {
        0: [WT(1, 32)],
        1: [WT(0, 32)]
    },
    'MAP_VICTORY_ROAD_2F': {
        0: [WT(2, 32)],
        1: [WT(0, 32), WT(2, 32)],
        2: [],
        3: [WT(5, 0), WT(6, 0), WT(7, 0)],
        5: [WT(3, 0), WT(6, 0), WT(7, 0)],
        6: [WT(5, 0), WT(3, 0), WT(7, 0)],
        7: [WT(5, 0), WT(6, 0), WT(3, 0)],
        8: [WT(2, 0)]
    },
    'MAP_VICTORY_ROAD_3F': {
        0: [WT(1, 0), WT(4, 32)],
        1: [WT(0, 0), WT(4, 32)],
        2: [WT(3, 0), WT(0, 32), WT(1, 32), WT(4, 32)],
        3: [WT(2, 0), WT(0, 32), WT(1, 32), WT(4, 32)],
        4: [WT(0, 32), WT(1, 32)]
    },
    'MAP_ROCKET_HIDEOUT_B1F': {
        0: [WT(1, 0), WT(3, 0), WT(4, 0), WT(5, 0)],
        1: [WT(0, 0), WT(3, 0), WT(4, 0), WT(5, 0)],
        2: [],
        3: [WT(0, 0), WT(1, 0), WT(4, 0), WT(5, 0)],
        4: [WT(0, 0), WT(3, 0), WT(1, 0), WT(5, 0)],
        5: [WT(0, 0), WT(3, 0), WT(4, 0), WT(1, 0)]
    },
    'MAP_ROCKET_HIDEOUT_B4F': {
        0: [],
        1: [WT(2, 0)],
        2: [WT(1, 0)]
    },
    'MAP_SILPH_CO_2F': {
        0: [WT(2, 0), WT(3, 0), WT(5, 0), WT(6, 0), WT(1, 256), WT(4, 256)],
        1: [WT(2, 256), WT(3, 256), WT(5, 256), WT(6, 256), WT(0, 256), WT(4, 256)],
        2: [WT(0, 0), WT(3, 0), WT(5, 0), WT(6, 0), WT(1, 256), WT(4, 256)],
        3: [WT(0, 0), WT(2, 0), WT(5, 0), WT(6, 0), WT(1, 256), WT(4, 256)],
        4: [WT(2, 256), WT(3, 256), WT(5, 256), WT(6, 256), WT(0, 256), WT(1, 256)],
        5: [WT(2, 0), WT(3, 0), WT(0, 0), WT(6, 0), WT(1, 256), WT(4, 256)],
        6: [WT(2, 0), WT(3, 0), WT(5, 0), WT(0, 0), WT(1, 256), WT(4, 256)]
    },
    'MAP_SILPH_CO_3F': {
        0: [WT(1, 0), WT(2, 256), WT(3, 0), WT(4, 256), WT(5, 0), WT(6, 0), WT(7, 0), WT(8, 0), WT(9, 0)],
        1: [WT(0, 0), WT(2, 256), WT(3, 0), WT(4, 256), WT(5, 0), WT(6, 0), WT(7, 0), WT(8, 0), WT(9, 0)],
        2: [WT(1, 256), WT(0, 256), WT(3, 256), WT(4, 256), WT(5, 256), WT(6, 256), WT(7, 256), WT(8, 256), WT(9, 256)],
        3: [WT(1, 0), WT(2, 256), WT(0, 0), WT(4, 256), WT(5, 0), WT(6, 0), WT(7, 0), WT(8, 0), WT(9, 0)],
        4: [WT(1, 256), WT(0, 256), WT(3, 256), WT(2, 256), WT(5, 256), WT(6, 256), WT(7, 256), WT(8, 256), WT(9, 256)],
        5: [WT(1, 0), WT(2, 256), WT(3, 0), WT(4, 256), WT(0, 0), WT(6, 0), WT(7, 0), WT(8, 0), WT(9, 0)],
        6: [WT(1, 0), WT(2, 256), WT(3, 0), WT(4, 256), WT(5, 0), WT(0, 0), WT(7, 0), WT(8, 0), WT(9, 0)],
        7: [WT(1, 0), WT(2, 256), WT(3, 0), WT(4, 256), WT(5, 0), WT(6, 0), WT(0, 0), WT(8, 0), WT(9, 0)],
        8: [WT(1, 0), WT(2, 256), WT(3, 0), WT(4, 256), WT(5, 0), WT(6, 0), WT(7, 0), WT(0, 0), WT(9, 0)],
        9: [WT(1, 0), WT(2, 256), WT(3, 0), WT(4, 256), WT(5, 0), WT(6, 0), WT(7, 0), WT(8, 0), WT(0, 0)]
    },
    'MAP_SILPH_CO_4F': {
        0: [WT(1, 256), WT(2, 0), WT(3, 256), WT(4, 0), WT(5, 0), WT(6, 0)],
        1: [WT(0, 256), WT(2, 256), WT(3, 0), WT(4, 256), WT(5, 256), WT(6, 256)],
        2: [WT(1, 256), WT(0, 0), WT(3, 256), WT(4, 0), WT(5, 0), WT(6, 0)],
        3: [WT(0, 256), WT(2, 256), WT(1, 0), WT(4, 256), WT(5, 256), WT(6, 256)],
        4: [WT(1, 256), WT(2, 0), WT(3, 256), WT(0, 0), WT(5, 0), WT(6, 0)],
        5: [WT(1, 256), WT(2, 0), WT(3, 256), WT(4, 0), WT(0, 0), WT(6, 0)],
        6: [WT(1, 256), WT(2, 0), WT(3, 256), WT(4, 0), WT(5, 0), WT(0, 0)]
    },
    'MAP_SILPH_CO_5F': {
        0: [WT(1, 0), WT(2, 0), WT(3, 0), WT(4, 256), WT(5, 0), WT(6, 0)],
        1: [WT(0, 0), WT(2, 0), WT(3, 0), WT(4, 256), WT(5, 0), WT(6, 0)],
        2: [WT(1, 0), WT(0, 0), WT(3, 0), WT(4, 256), WT(5, 0), WT(6, 0)],
        3: [WT(1, 0), WT(2, 0), WT(0, 0), WT(4, 256), WT(5, 0), WT(6, 0)],
        4: [WT(1, 256), WT(2, 256), WT(3, 256), WT(0, 256), WT(5, 256), WT(6, 256)],
        5: [WT(1, 0), WT(2, 0), WT(3, 0), WT(4, 256), WT(0, 0), WT(6, 0)],
        6: [WT(1, 0), WT(2, 0), WT(3, 0), WT(4, 256), WT(5, 0), WT(0, 0)]
    },
    'MAP_SILPH_CO_7F': {
        0: [WT(2, 256), WT(3, 0), WT(5, 0)],
        1: [WT(4, 0)],
        2: [WT(0, 256), WT(3, 256), WT(5, 256)],
        3: [WT(2, 256), WT(0, 0), WT(5, 0)],
        4: [WT(1, 0)],
        5: [WT(2, 256), WT(3, 0), WT(0, 0)],
    },
    'MAP_SILPH_CO_8F': {
        0: [WT(1, 0), WT(2, 0), WT(3, 0), WT(4, 256), WT(5, 0), WT(6, 0)],
        1: [WT(0, 0), WT(2, 0), WT(3, 0), WT(4, 256), WT(5, 0), WT(6, 0)],
        2: [WT(1, 0), WT(0, 0), WT(3, 0), WT(4, 256), WT(5, 0), WT(6, 0)],
        3: [WT(1, 0), WT(2, 0), WT(0, 0), WT(4, 256), WT(5, 0), WT(6, 0)],
        4: [WT(1, 256), WT(2, 256), WT(3, 256), WT(0, 256), WT(5, 256), WT(6, 256)],
        5: [WT(1, 0), WT(2, 0), WT(3, 0), WT(4, 256), WT(0, 0), WT(6, 0)],
        6: [WT(1, 0), WT(2, 0), WT(3, 0), WT(4, 256), WT(5, 0), WT(0, 0)]
    },
    'MAP_SILPH_CO_9F': {
        0: [WT(1, 0), WT(2, 256), WT(3, 0), WT(4, 0)],
        1: [WT(0, 0), WT(2, 256), WT(3, 0), WT(4, 0)],
        2: [WT(1, 256), WT(0, 256), WT(3, 256), WT(4, 256)],
        3: [WT(1, 0), WT(2, 256), WT(0, 0), WT(4, 0)],
        4: [WT(1, 0), WT(2, 256), WT(3, 0), WT(0, 0)]
    },
    'MAP_SILPH_CO_10F': {
        0: [WT(1, 256), WT(2, 0), WT(3, 0), WT(4, 256), WT(5, 0)],
        1: [WT(0, 256), WT(2, 256), WT(3, 256), WT(4, 0), WT(5, 256)],
        2: [WT(1, 256), WT(0, 0), WT(3, 0), WT(4, 256), WT(5, 0)],
        3: [WT(1, 256), WT(2, 0), WT(0, 0), WT(4, 256), WT(5, 0)],
        4: [WT(0, 256), WT(2, 256), WT(3, 256), WT(1, 0), WT(5, 256)],
        5: [WT(1, 256), WT(2, 0), WT(3, 0), WT(4, 256), WT(0, 0)]
    },
    'MAP_SILPH_CO_11F': {
        0: [WT(2, 0)],
        1: [],
        2: [WT(0, 0)]
    },
    'MAP_POKEMON_MANSION_1F': {
        0: [WT(1, 0), WT(2, 0), WT(3, 0), WT(9, 0)],
        1: [WT(0, 0), WT(2, 0), WT(3, 0), WT(9, 0)],
        2: [WT(1, 0), WT(0, 0), WT(3, 0), WT(9, 0)],
        3: [WT(1, 0), WT(2, 0), WT(0, 0), WT(9, 0)],
        4: [],
        5: [WT(6, 0)],
        6: [WT(5, 0)],
        7: [WT(4, 0)],
        8: [WT(4, 0)],
        9: [WT(1, 0), WT(2, 0), WT(3, 0), WT(0, 0)]
    },
    'MAP_POKEMON_MANSION_2F': {
        0: [],
        1: [],
        2: [WT(0, 0), WT(1, 0), WT(3, 0)],
        3: [WT(2, 0), WT(1, 0), WT(0, 0)],
        4: []
    },
    'MAP_POKEMON_MANSION_3F': {
        0: [WT(1, 0), WT(3, 0), WT(4, 0), WT(5, 0), WT(6, 0), WT(7, 0)],
        1: [WT(3, 0), WT(4, 0), WT(5, 0), WT(6, 0), WT(7, 0)],
        2: [],
        3: [WT(1, 0), WT(4, 0), WT(5, 0), WT(6, 0), WT(7, 0)],
        4: [WT(3, 0), WT(1, 0), WT(5, 0), WT(6, 0), WT(7, 0)],
        5: [WT(3, 0), WT(4, 0), WT(1, 0), WT(6, 0), WT(7, 0)],
        6: [WT(3, 0), WT(4, 0), WT(5, 0), WT(1, 0), WT(7, 0)],
        7: [WT(3, 0), WT(4, 0), WT(5, 0), WT(6, 0), WT(1, 0)],
    },
    'MAP_CERULEAN_CAVE_1F': {
        0: [WT(1, 4096), WT(3, 4096), WT(4, 4096), WT(5, 4096), WT(6, 4096)],
        1: [WT(0, 4096), WT(3, 4096), WT(4, 4096), WT(5, 4096), WT(6, 4096)],
        2: [WT(7, 0)],
        3: [WT(1, 4096), WT(0, 4096), WT(4, 0), WT(5, 0), WT(6, 0)],
        4: [WT(1, 4096), WT(0, 4096), WT(3, 0), WT(5, 0), WT(6, 0)],
        5: [WT(1, 4096), WT(0, 4096), WT(4, 0), WT(3, 0), WT(6, 0)],
        6: [WT(1, 4096), WT(0, 4096), WT(4, 0), WT(5, 0), WT(3, 0)],
        7: [WT(2, 0)]
    },
    'MAP_POKEMON_LEAGUE_LORELEIS_ROOM': {
        0: [WT(1, 0)],
        1: []
    },
    'MAP_POKEMON_LEAGUE_BRUNOS_ROOM': {
        0: [WT(1, 0)],
        1: []
    },
    'MAP_POKEMON_LEAGUE_AGATHAS_ROOM': {
        0: [WT(1, 0)],
        1: []
    },
    'MAP_POKEMON_LEAGUE_LANCES_ROOM': {
        0: [WT(1, 0)],
        1: []
    },
    'MAP_ROCK_TUNNEL_1F': {
        0: [WT(1, 0)],
        1: [WT(0, 0)],
        2: [WT(3, 0)],
        3: [WT(2, 0)],
        4: [WT(5, 0)],
        5: [WT(4, 0)]
    },
    'MAP_ROCK_TUNNEL_B1F': {
        0: [WT(1, 0)],
        1: [WT(0, 0)],
        2: [WT(3, 0)],
        3: [WT(2, 0)]
    },
    'MAP_SEAFOAM_ISLANDS_1F': {
        0: [WT(1, 0), WT(3, 0), WT(5, 0), WT(6, 0)],
        1: [WT(0, 0), WT(3, 0), WT(5, 0), WT(6, 0)],
        2: [WT(4, 0)],
        3: [WT(1, 0), WT(0, 0), WT(5, 0), WT(6, 0)],
        4: [WT(2, 0)],
        5: [WT(1, 0), WT(3, 0), WT(0, 0), WT(6, 0)],
        6: [WT(1, 0), WT(3, 0), WT(5, 0), WT(0, 0)]
    },
    'MAP_SEAFOAM_ISLANDS_B1F': {
        0: [WT(3, 0), WT(4, 0), WT(7, 0)],
        1: [WT(8, 0)],
        2: [WT(6, 0)],
        3: [WT(0, 0), WT(4, 0), WT(7, 0)],
        4: [WT(3, 0), WT(0, 0), WT(7, 0)],
        5: [],
        6: [WT(2, 0)],
        7: [WT(3, 0), WT(4, 0), WT(0, 0)],
        8: [WT(1, 0)],
        9: [WT(0, 0), WT(3, 0), WT(4, 0), WT(7, 0)],
        10: [WT(8, 0), WT(1, 0)]
    },
    'MAP_SEAFOAM_ISLANDS_B2F': {
        0: [WT(4, 0), WT(5, 0)],
        1: [WT(10, 0)],
        2: [WT(6, 0)],
        3: [WT(9, 0)],
        4: [WT(0, 0), WT(5, 0)],
        5: [WT(4, 0), WT(0, 0)],
        6: [WT(2, 0)],
        7: [WT(3, 0), WT(9, 0)],
        8: [WT(1, 0), WT(10, 0)],
        9: [WT(3, 0)],
        10: [WT(1, 0)]
    },
    'MAP_SEAFOAM_ISLANDS_B3F': {
        0: [WT(3, 0), WT(7, 0), WT(8, 0)],
        1: [WT(4, 0)],
        2: [],
        3: [WT(0, 0), WT(7, 0), WT(8, 0)],
        4: [WT(1, 0)],
        7: [WT(3, 0), WT(0, 0), WT(8, 0)],
        8: [WT(3, 0), WT(7, 0), WT(0, 0)]
    },
    'MAP_SEAFOAM_ISLANDS_B4F': {
        0: [WT(1, 0)],
        1: [WT(0, 0)]
    },
    'MAP_VIRIDIAN_CITY': {
        0: [WT(1, 0), WT(2, 16385), WT(3, 0), WT(4, 0)],
        1: [WT(0, 0), WT(2, 16385), WT(3, 0), WT(4, 0)],
        2: [WT(1, 0), WT(0, 0), WT(3, 0), WT(4, 0)],
        3: [WT(1, 0), WT(2, 16385), WT(0, 0), WT(4, 0)],
        4: [WT(1, 0), WT(2, 16385), WT(3, 0), WT(0, 0)]
    },
    'MAP_ROUTE23': {
        0: [WT(2, 49152), WT(3, 49152)],
        1: [],
        2: [WT(0, 49152), WT(3, 0)],
        3: [WT(2, 0), WT(0, 49152)],
    },
    'MAP_ROUTE2': {
        0: [WT(1, 0), WT(3, 4), WT(4, 4), WT(6, 4), WT(7, 4)],
        1: [WT(0, 0), WT(3, 4), WT(4, 4), WT(6, 4), WT(7, 4)],
        2: [WT(9, 0), WT(5, 4), WT(8, 4)],
        3: [WT(1, 4), WT(0, 4), WT(4, 0), WT(6, 4), WT(7, 4)],
        4: [WT(1, 4), WT(0, 4), WT(3, 0), WT(6, 4), WT(7, 4)],
        5: [WT(9, 4), WT(2, 4), WT(8, 0)],
        6: [WT(1, 4), WT(3, 4), WT(4, 4), WT(0, 4), WT(7, 0)],
        7: [WT(1, 4), WT(3, 4), WT(4, 4), WT(0, 4), WT(6, 0)],
        8: [WT(9, 4), WT(2, 4), WT(5, 0)],
        9: [WT(2, 0), WT(5, 4), WT(8, 4)]
    },
    'MAP_PEWTER_CITY': {
        0: [WT(1, 4), WT(2, 0), WT(3, 0), WT(4, 0), WT(5, 0), WT(6, 0)],
        1: [WT(0, 0), WT(2, 0), WT(3, 0), WT(4, 0), WT(5, 0), WT(6, 0)],
        2: [WT(1, 4), WT(0, 0), WT(3, 0), WT(4, 0), WT(5, 0), WT(6, 0)],
        3: [WT(1, 4), WT(2, 0), WT(0, 0), WT(4, 0), WT(5, 0), WT(6, 0)],
        4: [WT(1, 4), WT(2, 0), WT(3, 0), WT(0, 0), WT(5, 0), WT(6, 0)],
        5: [WT(1, 4), WT(2, 0), WT(3, 0), WT(4, 0), WT(0, 0), WT(6, 0)],
        6: [WT(1, 4), WT(2, 0), WT(3, 0), WT(4, 0), WT(5, 0), WT(0, 0)]
    },
    'MAP_PEWTER_CITY_MUSEUM_1F': {
        0: [WT(1, 0), WT(2, 0), WT(5, 0)],
        1: [WT(0, 0), WT(2, 0), WT(5, 0)],
        2: [WT(1, 0), WT(0, 0), WT(5, 0)],
        3: [WT(4, 0)],
        4: [WT(3, 0)],
        5: [WT(1, 0), WT(2, 0), WT(0, 0)]
    },
    'MAP_ROUTE4': {
        0: [WT(2, 0)],
        1: [],
        2: [WT(0, 0)]
    },
    'MAP_CERULEAN_CITY': {
        0: [WT(1, 0), WT(2, 0), WT(3, 0), WT(4, 0), WT(5, 0), WT(6, 0), WT(9, 4), WT(10, 4), WT(11, 0), WT(12, 0),
            WT(13, 0)],
        1: [WT(0, 0), WT(2, 0), WT(3, 0), WT(4, 0), WT(5, 0), WT(6, 0), WT(9, 4), WT(10, 4), WT(11, 0), WT(12, 0),
            WT(13, 0)],
        2: [WT(1, 0), WT(0, 0), WT(3, 0), WT(4, 0), WT(5, 0), WT(6, 0), WT(9, 4), WT(10, 4), WT(11, 0), WT(12, 0),
            WT(13, 0)],
        3: [WT(1, 0), WT(2, 0), WT(0, 0), WT(4, 0), WT(5, 0), WT(6, 0), WT(9, 4), WT(10, 4), WT(11, 0), WT(12, 0),
            WT(13, 0)],
        4: [WT(1, 0), WT(2, 0), WT(3, 0), WT(0, 0), WT(5, 0), WT(6, 0), WT(9, 4), WT(10, 4), WT(11, 0), WT(12, 0),
            WT(13, 0)],
        5: [WT(1, 0), WT(2, 0), WT(3, 0), WT(4, 0), WT(0, 0), WT(6, 0), WT(9, 4), WT(10, 4), WT(11, 0), WT(12, 0),
            WT(13, 0)],
        6: [WT(1, 0), WT(2, 0), WT(3, 0), WT(4, 0), WT(5, 0), WT(0, 0), WT(9, 4), WT(10, 4), WT(11, 0), WT(12, 0),
            WT(13, 0)],
        8: [],
        9: [WT(1, 0), WT(2, 0), WT(3, 0), WT(4, 0), WT(5, 0), WT(6, 0), WT(0, 0), WT(10, 0), WT(11, 0), WT(12, 0),
            WT(13, 0)],
        10: [WT(1, 0), WT(2, 0), WT(3, 0), WT(4, 0), WT(5, 0), WT(0, 0), WT(9, 0), WT(0, 0), WT(11, 0), WT(12, 0),
             WT(13, 0)],
        11: [WT(1, 0), WT(2, 0), WT(3, 0), WT(4, 0), WT(5, 0), WT(6, 0), WT(9, 4), WT(10, 4), WT(0, 0), WT(12, 0),
             WT(13, 0)],
        12: [WT(1, 0), WT(2, 0), WT(3, 0), WT(4, 0), WT(5, 0), WT(6, 0), WT(9, 4), WT(10, 4), WT(11, 0), WT(0, 0),
             WT(13, 0)],
        13: [WT(1, 0), WT(2, 0), WT(3, 0), WT(4, 0), WT(5, 0), WT(6, 0), WT(9, 4), WT(10, 4), WT(11, 0), WT(12, 0),
             WT(0, 0)]
    },
    'MAP_ROUTE10': {
        0: [WT(2, 4096), WT(3, 0)],
        1: [],
        2: [WT(0, 4096), WT(3, 4096)],
        3: [WT(2, 4096), WT(0, 0)],
        4: [WT(0, 4096), WT(2, 0), WT(3, 4096)]
    },
    'MAP_ROUTE6_NORTH_ENTRANCE': {
        0: [WT(1, 0), WT(2, 0), WT(3, 0)],
        1: [WT(0, 0), WT(2, 0), WT(3, 0)],
        2: [WT(1, 8), WT(0, 8), WT(3, 0)],
        3: [WT(1, 8), WT(2, 0), WT(0, 8)]
    },
    'MAP_ROUTE5_SOUTH_ENTRANCE': {
        0: [WT(1, 0), WT(2, 0), WT(3, 0)],
        1: [WT(0, 8), WT(2, 8), WT(3, 0)],
        2: [WT(1, 0), WT(0, 0), WT(3, 0)],
        3: [WT(1, 0), WT(2, 8), WT(0, 8)]
    },
    'MAP_ROUTE7_EAST_ENTRANCE': {
        0: [WT(1, 0), WT(2, 8), WT(3, 8)],
        1: [WT(0, 0), WT(2, 8), WT(3, 8)],
        2: [WT(1, 0), WT(0, 0), WT(3, 0)],
        3: [WT(1, 0), WT(2, 0), WT(0, 0)]
    },
    'MAP_ROUTE8_WEST_ENTRANCE': {
        0: [WT(1, 0), WT(2, 0), WT(3, 0)],
        1: [WT(0, 0), WT(2, 0), WT(3, 0)],
        2: [WT(1, 8), WT(0, 8), WT(3, 0)],
        3: [WT(1, 8), WT(2, 0), WT(0, 8)]
    },
    'MAP_VERMILION_CITY': {
        3: [WT(4, 0), WT(5, 0), WT(6, 0), WT(7, 0), WT(8, 0), WT(9, 4)],
        4: [WT(3, 0), WT(5, 0), WT(6, 0), WT(7, 0), WT(8, 0), WT(9, 4)],
        5: [WT(4, 0), WT(3, 0), WT(6, 0), WT(7, 0), WT(8, 0), WT(9, 4)],
        6: [WT(4, 0), WT(5, 0), WT(3, 0), WT(7, 0), WT(8, 0), WT(9, 4)],
        7: [WT(4, 0), WT(5, 0), WT(6, 0), WT(3, 0), WT(8, 0), WT(9, 4)],
        8: [WT(4, 0), WT(5, 0), WT(6, 0), WT(7, 0), WT(3, 0), WT(9, 4)],
        9: [WT(4, 4), WT(5, 4), WT(6, 4), WT(7, 4), WT(8, 4), WT(3, 4)]
    },
    'MAP_ROUTE11': {
        0: [WT(1, 0)],
        1: [WT(0, 0)],
        2: []
    },
    'MAP_ROUTE12': {
        0: [WT(3, 128)],
        1: [WT(2, 0)],
        2: [WT(1, 0)],
        3: [WT(0, 128)]
    },
    'MAP_CELADON_CITY': {
        0: [WT(1, 0), WT(2, 0), WT(3, 0), WT(4, 0), WT(5, 0), WT(6, 4), WT(7, 0), WT(8, 0), WT(9, 0), WT(10, 0),
            WT(11, 0), WT(12, 0)],
        1: [WT(0, 0), WT(2, 0), WT(3, 0), WT(4, 0), WT(5, 0), WT(6, 4), WT(7, 0), WT(8, 0), WT(9, 0), WT(10, 0),
            WT(11, 0), WT(12, 0)],
        2: [WT(1, 0), WT(0, 0), WT(3, 0), WT(4, 0), WT(5, 0), WT(6, 4), WT(7, 0), WT(8, 0), WT(9, 0), WT(10, 0),
            WT(11, 0), WT(12, 0)],
        3: [WT(1, 0), WT(2, 0), WT(0, 0), WT(4, 0), WT(5, 0), WT(6, 4), WT(7, 0), WT(8, 0), WT(9, 0), WT(10, 0),
            WT(11, 0), WT(12, 0)],
        4: [WT(1, 0), WT(2, 0), WT(3, 0), WT(0, 0), WT(5, 0), WT(6, 4), WT(7, 0), WT(8, 0), WT(9, 0), WT(10, 0),
            WT(11, 0), WT(12, 0)],
        5: [WT(1, 0), WT(2, 0), WT(3, 0), WT(4, 0), WT(0, 0), WT(6, 4), WT(7, 0), WT(8, 0), WT(9, 0), WT(10, 0),
            WT(11, 0), WT(12, 0)],
        6: [WT(1, 4), WT(2, 4), WT(3, 4), WT(4, 4), WT(5, 4), WT(0, 4), WT(7, 4), WT(8, 4), WT(9, 4), WT(10, 4),
            WT(11, 4), WT(12, 4)],
        7: [WT(1, 0), WT(2, 0), WT(3, 0), WT(4, 0), WT(5, 0), WT(6, 4), WT(0, 0), WT(8, 0), WT(9, 0), WT(10, 0),
            WT(11, 0), WT(12, 0)],
        8: [WT(1, 0), WT(2, 0), WT(3, 0), WT(4, 0), WT(5, 0), WT(6, 4), WT(7, 0), WT(0, 0), WT(9, 0), WT(10, 0),
            WT(11, 0), WT(12, 0)],
        9: [WT(1, 0), WT(2, 0), WT(3, 0), WT(4, 0), WT(5, 0), WT(6, 4), WT(7, 0), WT(8, 0), WT(0, 0), WT(10, 0),
            WT(11, 0), WT(12, 0)],
        10: [WT(1, 0), WT(2, 0), WT(3, 0), WT(4, 0), WT(5, 0), WT(6, 4), WT(7, 0), WT(8, 0), WT(9, 0), WT(0, 0),
             WT(11, 0), WT(12, 0)],
        11: [WT(1, 0), WT(2, 0), WT(3, 0), WT(4, 0), WT(5, 0), WT(6, 4), WT(7, 0), WT(8, 0), WT(9, 0), WT(10, 0),
             WT(0, 0), WT(12, 0)],
        12: [WT(1, 0), WT(2, 0), WT(3, 0), WT(4, 0), WT(5, 0), WT(6, 4), WT(7, 0), WT(8, 0), WT(9, 0), WT(10, 0),
             WT(11, 0), WT(0, 0)],
    },
    'MAP_CELADON_CITY_CONDOMINIUMS_1F': {
        0: [WT(1, 0), WT(2, 0), WT(4, 0)],
        1: [WT(0, 0), WT(2, 0), WT(4, 0)],
        2: [WT(1, 0), WT(0, 0), WT(4, 0)],
        3: [WT(5, 0)],
        4: [WT(1, 0), WT(2, 0), WT(0, 0)],
        5: [WT(3, 0)]
    },
    'MAP_CELADON_CITY_CONDOMINIUMS_2F': {
        0: [WT(1, 0)],
        1: [WT(0, 0)],
        2: [WT(3, 0)],
        3: [WT(2, 0)]
    },
    'MAP_CELADON_CITY_CONDOMINIUMS_3F': {
        0: [WT(1, 0)],
        1: [WT(0, 0)],
        2: [WT(3, 0)],
        3: [WT(2, 0)]
    },
    'MAP_CELADON_CITY_CONDOMINIUMS_ROOF': {
        0: [WT(2, 0)],
        1: [],
        2: [WT(0, 0)]
    },
    'MAP_POKEMON_TOWER_6F': {
        0: [WT(1, 64)],
        1: [WT(0, 64)]
    },
    'MAP_ROUTE16': {
        0: [WT(1, 0)],
        1: [WT(0, 0)],
        2: [WT(4, 132)],
        3: [],
        4: [WT(2, 132)]
    },
    'MAP_ROUTE16_NORTH_ENTRANCE_1F': {
        0: [WT(1, 0)],
        1: [WT(0, 0)],
        2: [WT(3, 0), WT(4, 0)],
        3: [WT(2, 2048), WT(4, 0)],
        4: [WT(2, 2048), WT(3, 0)]
    },
    'MAP_ROUTE18_EAST_ENTRANCE_1F': {
        0: [WT(1, 0), WT(2, 0)],
        1: [WT(2, 0), WT(0, 2048)],
        2: [WT(1, 0), WT(0, 2048)]
    },
    'MAP_ROUTE18': {
        0: [],
        1: []
    },
    'MAP_ROUTE15': {
        0: [],
        1: []
    },
    'MAP_FUCHSIA_CITY': {
        0: [WT(1, 0), WT(2, 0), WT(3, 0), WT(4, 0), WT(5, 0), WT(6, 0), WT(7, 0), WT(10, 0)],
        1: [WT(0, 0), WT(2, 0), WT(3, 0), WT(4, 0), WT(5, 0), WT(6, 0), WT(7, 0), WT(10, 0)],
        2: [WT(1, 0), WT(0, 0), WT(3, 0), WT(4, 0), WT(5, 0), WT(6, 0), WT(7, 0), WT(10, 0)],
        3: [WT(1, 0), WT(2, 0), WT(0, 0), WT(4, 0), WT(5, 0), WT(6, 0), WT(7, 0), WT(10, 0)],
        4: [WT(1, 0), WT(2, 0), WT(3, 0), WT(0, 0), WT(5, 0), WT(6, 0), WT(7, 0), WT(10, 0)],
        5: [WT(1, 0), WT(2, 0), WT(3, 0), WT(4, 0), WT(0, 0), WT(6, 0), WT(7, 0), WT(10, 0)],
        6: [WT(1, 0), WT(2, 0), WT(3, 0), WT(4, 0), WT(5, 0), WT(0, 0), WT(7, 0), WT(10, 0)],
        7: [WT(1, 0), WT(2, 0), WT(3, 0), WT(4, 0), WT(5, 0), WT(6, 0), WT(0, 0), WT(10, 0)],
        8: [WT(9, 0)],
        9: [WT(8, 0)],
        10: [WT(1, 0), WT(2, 0), WT(3, 0), WT(4, 0), WT(5, 0), WT(6, 0), WT(7, 0), WT(0, 0)],
    },
    'MAP_SAFFRON_CITY': {
        0: [WT(1, 512), WT(2, 0), WT(3, 512), WT(4, 512), WT(5, 0), WT(6, 0), WT(7, 0), WT(8, 0), WT(9, 0), WT(10, 0),
            WT(11, 0), WT(12, 0), WT(13, 0), WT(14, 0)],
        1: [WT(0, 0), WT(2, 0), WT(3, 512), WT(4, 512), WT(5, 0), WT(6, 0), WT(7, 0), WT(8, 0), WT(9, 0), WT(10, 0),
            WT(11, 0), WT(12, 0), WT(13, 0), WT(14, 0)],
        2: [WT(1, 512), WT(0, 0), WT(3, 512), WT(4, 512), WT(5, 0), WT(6, 0), WT(7, 0), WT(8, 0), WT(9, 0), WT(10, 0),
            WT(11, 0), WT(12, 0), WT(13, 0), WT(14, 0)],
        3: [WT(1, 512), WT(2, 0), WT(0, 0), WT(4, 512), WT(5, 0), WT(6, 0), WT(7, 0), WT(8, 0), WT(9, 0), WT(10, 0),
            WT(11, 0), WT(12, 0), WT(13, 0), WT(14, 0)],
        4: [WT(1, 512), WT(2, 0), WT(3, 512), WT(0, 0), WT(5, 0), WT(6, 0), WT(7, 0), WT(8, 0), WT(9, 0), WT(10, 0),
            WT(11, 0), WT(12, 0), WT(13, 0), WT(14, 0)],
        5: [WT(1, 512), WT(2, 0), WT(3, 512), WT(4, 512), WT(0, 0), WT(6, 0), WT(7, 0), WT(8, 0), WT(9, 0), WT(10, 0),
            WT(11, 0), WT(12, 0), WT(13, 0), WT(14, 0)],
        6: [WT(1, 512), WT(2, 0), WT(3, 512), WT(4, 512), WT(5, 0), WT(0, 0), WT(7, 0), WT(8, 0), WT(9, 0), WT(10, 0),
            WT(11, 0), WT(12, 0), WT(13, 0), WT(14, 0)],
        7: [WT(1, 512), WT(2, 0), WT(3, 512), WT(4, 512), WT(5, 0), WT(6, 0), WT(0, 0), WT(8, 0), WT(9, 0), WT(10, 0),
            WT(11, 0), WT(12, 0), WT(13, 0), WT(14, 0)],
        8: [WT(1, 512), WT(2, 0), WT(3, 512), WT(4, 512), WT(5, 0), WT(6, 0), WT(7, 0), WT(0, 0), WT(9, 0), WT(10, 0),
            WT(11, 0), WT(12, 0), WT(13, 0), WT(14, 0)],
        9: [WT(1, 512), WT(2, 0), WT(3, 512), WT(4, 512), WT(5, 0), WT(6, 0), WT(7, 0), WT(8, 0), WT(0, 0), WT(10, 0),
            WT(11, 0), WT(12, 0), WT(13, 0), WT(14, 0)],
        10: [WT(1, 512), WT(2, 0), WT(3, 512), WT(4, 512), WT(5, 0), WT(6, 0), WT(7, 0), WT(8, 0), WT(9, 0), WT(0, 0),
             WT(11, 0), WT(12, 0), WT(13, 0), WT(14, 0)],
        11: [WT(1, 512), WT(2, 0), WT(3, 512), WT(4, 512), WT(5, 0), WT(6, 0), WT(7, 0), WT(8, 0), WT(9, 0), WT(10, 0),
             WT(0, 0), WT(12, 0), WT(13, 0), WT(14, 0)],
        12: [WT(1, 512), WT(2, 0), WT(3, 512), WT(4, 512), WT(5, 0), WT(6, 0), WT(7, 0), WT(8, 0), WT(9, 0), WT(10, 0),
             WT(11, 0), WT(0, 0), WT(13, 0), WT(14, 0)],
        13: [WT(1, 512), WT(2, 0), WT(3, 512), WT(4, 512), WT(5, 0), WT(6, 0), WT(7, 0), WT(8, 0), WT(9, 0), WT(10, 0),
             WT(11, 0), WT(12, 0), WT(0, 0), WT(14, 0)],
        14: [WT(1, 512), WT(2, 0), WT(3, 512), WT(4, 512), WT(5, 0), WT(6, 0), WT(7, 0), WT(8, 0), WT(9, 0), WT(10, 0),
             WT(11, 0), WT(12, 0), WT(13, 0), WT(0, 0)],
    },
    'MAP_ROUTE20': {
        0: [],
        1: []
    },
    'MAP_CINNABAR_ISLAND': {
        0: [WT(1, 8192), WT(2, 0), WT(3, 0), WT(4, 0)],
        1: [WT(0, 0), WT(2, 0), WT(3, 0), WT(4, 0)],
        2: [WT(1, 8192), WT(0, 0), WT(3, 0), WT(4, 0)],
        3: [WT(1, 8192), WT(2, 0), WT(0, 0), WT(4, 0)],
        4: [WT(1, 8192), WT(2, 0), WT(3, 0), WT(0, 0)],
    }
}

# Basically we define the easiest warp to reach from one map to the next map (i.e. connections)
# We only need to define the easiest warp because once we define the easiest we can then know what it takes to get from
# that warp to all other warps based off map_warp_accessibility
# if not defined we can assume warp 0 is the easiest to reach with 0 flag requirements
map_to_map_warp_accessibility = {
    'MAP_ROUTE2': {
        'MAP_VIRIDIAN_CITY': WT(2, 0),
        'MAP_PEWTER_CITY': WT(0, 0)
    },
    'MAP_ROUTE23': {
        'MAP_INDIGO_PLATEAU_EXTERIOR': WT(1, 0)
    },
    'MAP_ROUTE4': {
        'MAP_ROUTE3': WT(0, 0),
        'MAP_CERULEAN_CITY': WT(1, 4096)
    },
    'MAP_CERULEAN_CITY': {
        'MAP_ROUTE9': WT(0, 4)
    },
    'MAP_ROUTE10': {
        'MAP_ROUTE9': WT(0, 0),
        'MAP_LAVENDER_TOWN': WT(1, 0)
    },
    'MAP_VERMILION_CITY': {
        'MAP_ROUTE6': WT(3, 0),
        'MAP_ROUTE11': WT(3, 0)
    },
    'MAP_ROUTE11': {
        'MAP_ROUTE12': WT(2, 0)
    },
    'MAP_ROUTE12': {
        'MAP_LAVENDER_TOWN': WT(1, 0)
    },
    'MAP_ROUTE16': {
        'MAP_CELADON_CITY': WT(2, 4),
        'MAP_ROUTE17': WT(3, 0)
    },
    'MAP_ROUTE18': {
        'MAP_FUCHSIA_CITY': WT(1, 0),
    },
    'MAP_ROUTE15': {
        'MAP_ROUTE14': WT(1, 0),
    },
    'MAP_ROUTE20': {
        'MAP_CINNABAR_ISLAND': WT(1, 4096),
    }
}


cant_go_back_warps = {
    'MAP_POKEMON_MANSION_1F': [7, 8],
    'MAP_POKEMON_MANSION_2F': [4],
    'MAP_POKEMON_LEAGUE_LORELEIS_ROOM': [0],
    'MAP_POKEMON_LEAGUE_BRUNOS_ROOM': [0],
    'MAP_POKEMON_LEAGUE_AGATHAS_ROOM': [0],
    'MAP_POKEMON_LEAGUE_LANCES_ROOM': [0],
    'MAP_SEAFOAM_ISLANDS_B1F': [9, 10],
    'MAP_SEAFOAM_ISLANDS_B2F': [7, 8],
    'MAP_VIRIDIAN_CITY': [2],
    'MAP_ROUTE10': [4],
    'MAP_ROUTE16_NORTH_ENTRANCE_1F': [2],
    'MAP_SAFFRON_CITY': [1, 3, 4],
    'MAP_CINNABAR_ISLAND': [1],
    'MAP_VICTORY_ROAD_2F': [8],
    'MAP_ROUTE6_NORTH_ENTRANCE': [0, 1],
    'MAP_ROUTE5_SOUTH_ENTRANCE': [0, 2],
    'MAP_ROUTE7_EAST_ENTRANCE': [2, 3],
    'MAP_ROUTE8_WEST_ENTRANCE': [0, 1],
    'MAP_ROUTE18_EAST_ENTRANCE_1F': [0]
}

# Handles Connection Requirements
surf_needed = ['MAP_ROUTE21_NORTH', 'MAP_ROUTE21_SOUTH', 'MAP_ROUTE19', 'MAP_ROUTE20', 'MAP_CINNABAR_ISLAND']
pokeflute_needed = ['MAP_ROUTE12']

dont_randomize = ['MAP_ROCKET_HIDEOUT_ELEVATOR', 'MAP_SAFARI_ZONE_WEST_REST_HOUSE', 'MAP_SAFARI_ZONE_WEST',
                  'MAP_SAFARI_ZONE_SECRET_HOUSE', 'MAP_SAFARI_ZONE_NORTH_REST_HOUSE', 'MAP_SAFARI_ZONE_NORTH',
                  'MAP_SAFARI_ZONE_EAST_REST_HOUSE', 'MAP_SAFARI_ZONE_EAST', 'MAP_SAFARI_ZONE_CENTER_REST_HOUSE',
                  'MAP_SAFARI_ZONE_CENTER', 'PALLET_TOWN', 'MAP_POKEMON_LEAGUE_HALL_OF_FAME', 'ELEVATOR']

dont_randomize_warp = {'MAP_SSANNE_1F_CORRIDOR': [4], 'MAP_VICTORY_ROAD_2F': [4], 'MAP_SEAFOAM_ISLANDS_B3F': [5, 6],
                       'MAP_SEAFOAM_ISLANDS_B4F': [2, 3], 'MAP_POWER_PLANT': [4], 'MAP_CERULEAN_CITY': [7],
                       'MAP_VERMILION_CITY': [0, 1, 2]}

not_needed = ['MAP_SSANNE_EXTERIOR', 'MAP_MT_EMBER_EXTERIOR', 'MAP_MT_EMBER_RUBY_PATH_B5F',
              'MAP_MT_EMBER_RUBY_PATH_B4F', 'MAP_VIRIDIAN_CITY_POKEMON_CENTER_2F', 'MAP_VIRIDIAN_CITY_HOUSE1',
              'MAP_VIRIDIAN_CITY_HOUSE2', 'MAP_ROUTE11_EAST_ENTRANCE_2F', 'MAP_SSANNE_DECK', 'MAP_SSANNE_2F_ROOM1',
              'MAP_SSANNE_2F_ROOM2', 'MAP_SSANNE_2F_ROOM3', 'MAP_SSANNE_2F_ROOM4', 'MAP_SSANNE_2F_ROOM5',
              'MAP_SSANNE_2F_ROOM6', 'MAP_SSANNE_KITCHEN', 'MAP_SSANNE_B1F_ROOM1', 'MAP_SSANNE_B1F_ROOM2',
              'MAP_SSANNE_B1F_ROOM3', 'MAP_SSANNE_B1F_ROOM4', 'MAP_SSANNE_B1F_ROOM5', 'MAP_SSANNE_1F_ROOM1',
              'MAP_SSANNE_1F_ROOM2', 'MAP_SSANNE_1F_ROOM3', 'MAP_SSANNE_1F_ROOM4', 'MAP_SSANNE_1F_ROOM5',
              'MAP_SSANNE_1F_ROOM7', 'MAP_SSANNE_1F_ROOM6', 'MAP_VERMILION_CITY_HOUSE1',
              'MAP_VERMILION_CITY_POKEMON_CENTER_2F', 'MAP_VERMILION_CITY_HOUSE2', 'MAP_VERMILION_CITY_MART',
              'MAP_VERMILION_CITY_HOUSE3', 'MAP_ROUTE5_POKEMON_DAY_CARE', 'MAP_SAFFRON_CITY_COPYCATS_HOUSE_2F',
              'MAP_SAFFRON_CITY_HOUSE', 'MAP_SAFFRON_CITY_MART', 'MAP_SAFFRON_CITY_MR_PSYCHICS_HOUSE',
              'MAP_LAVENDER_TOWN_HOUSE1', 'MAP_LAVENDER_TOWN_HOUSE2', 'MAP_LAVENDER_TOWN_MART',
              'MAP_CERULEAN_CITY_HOUSE3', 'MAP_CERULEAN_CITY_MART', 'MAP_CERULEAN_CAVE_2F', 'MAP_CERULEAN_CITY_HOUSE4',
              'MAP_CERULEAN_CITY_HOUSE5', 'MAP_PEWTER_CITY_MUSEUM_2F', 'MAP_PEWTER_CITY_MART', 'MAP_PEWTER_CITY_HOUSE1',
              'MAP_PEWTER_CITY_HOUSE2', 'MAP_ROUTE12_FISHING_HOUSE', 'MAP_ROUTE12_NORTH_ENTRANCE_2F',
              'MAP_ROUTE15_WEST_ENTRANCE_2F', 'MAP_FUCHSIA_CITY_MART', 'MAP_FUCHSIA_CITY_HOUSE1',
              'MAP_FUCHSIA_CITY_HOUSE3', 'MAP_CINNABAR_ISLAND_POKEMON_LAB_LOUNGE',
              'MAP_CINNABAR_ISLAND_POKEMON_LAB_RESEARCH_ROOM', 'MAP_CINNABAR_ISLAND_POKEMON_LAB_EXPERIMENT_ROOM',
              'MAP_CINNABAR_ISLAND_MART', 'MAP_ROUTE18_EAST_ENTRANCE_2F', 'MAP_ROUTE16_NORTH_ENTRANCE_2F',
              'MAP_CELADON_CITY_CONDOMINIUMS_ROOF_ROOM', 'MAP_CELADON_CITY_GAME_CORNER_PRIZE_ROOM',
              'MAP_CELADON_CITY_RESTAURANT', 'MAP_CELADON_CITY_HOUSE1', 'MAP_CELADON_CITY_HOTEL',
              'MAP_SAFFRON_CITY_POKEMON_TRAINER_FAN_CLUB', 'MAP_ROUTE2_HOUSE', 'MAP_MT_EMBER_RUBY_PATH_B5F',
              'MAP_ROUTE22_NORTH_ENTRANCE', 'MAP_INDIGO_PLATEAU_POKEMON_CENTER_2F',
              'MAP_VIRIDIAN_CITY_POKEMON_CENTER_2F', 'MAP_PEWTER_CITY_POKEMON_CENTER_2F',
              'MAP_CERULEAN_CITY_POKEMON_CENTER_2F', 'MAP_ROUTE10_POKEMON_CENTER_2F',
              'MAP_SAFFRON_CITY_POKEMON_CENTER_2F', 'MAP_VERMILION_CITY_POKEMON_CENTER_2F',
              'MAP_LAVENDER_TOWN_POKEMON_CENTER_2F', 'MAP_CELADON_CITY_POKEMON_CENTER_2F',
              'MAP_FUCHSIA_CITY_POKEMON_CENTER_2F', 'MAP_CINNABAR_ISLAND_POKEMON_CENTER_2F',
              'MAP_ROUTE4_POKEMON_CENTER_2F']

non_navigable_connections = [['MAP_ROUTE23', 'MAP_ROUTE22'], ['MAP_ROUTE22', 'MAP_ROUTE23'],
                             ['MAP_ROUTE2', 'MAP_VIRIDIAN_CITY'], ['MAP_ROUTE2', 'MAP_PEWTER_CITY'],
                             ['MAP_ROUTE4', 'MAP_ROUTE3'], ['MAP_ROUTE4', 'MAP_CERULEAN_CITY'],
                             ['MAP_ROUTE10', 'MAP_ROUTE9'], ['MAP_ROUTE10', 'MAP_LAVENDER_TOWN'],
                             ['MAP_ROUTE5', 'MAP_SAFFRON_CITY_CONNECTION'],
                             ['MAP_SAFFRON_CITY_CONNECTION', 'MAP_ROUTE5'],
                             ['MAP_ROUTE6', 'MAP_SAFFRON_CITY_CONNECTION'],
                             ['MAP_SAFFRON_CITY_CONNECTION', 'MAP_ROUTE6'],
                             ['MAP_ROUTE11', 'MAP_ROUTE12'], ['MAP_ROUTE12', 'MAP_LAVENDER_TOWN'],
                             ['MAP_ROUTE8', 'MAP_SAFFRON_CITY_CONNECTION'],
                             ['MAP_SAFFRON_CITY_CONNECTION', 'MAP_ROUTE8'],
                             ['MAP_ROUTE7', 'MAP_SAFFRON_CITY_CONNECTION'],
                             ['MAP_SAFFRON_CITY_CONNECTION', 'MAP_ROUTE7'],
                             ['MAP_ROUTE16', 'MAP_ROUTE17'], ['MAP_ROUTE16', 'MAP_CELADON_CITY'],
                             ['MAP_ROUTE18', 'MAP_ROUTE17'], ['MAP_ROUTE18', 'MAP_FUCHSIA_CITY'],
                             ['MAP_ROUTE15', 'MAP_ROUTE14'], ['MAP_ROUTE15', 'MAP_FUCHSIA_CITY'],
                             ['MAP_SAFFRON_CITY', 'MAP_ROUTE5'], ['MAP_SAFFRON_CITY', 'MAP_ROUTE6'],
                             ['MAP_SAFFRON_CITY', 'MAP_ROUTE7'], ['MAP_SAFFRON_CITY', 'MAP_ROUTE8'],
                             ['MAP_ROUTE20', 'MAP_ROUTE19'], ['MAP_ROUTE20', 'MAP_CINNABAR_ISLAND']]

connection_to_connection_rules = {
    'MAP_PALLET_TOWN': {'MAP_ROUTE21_NORTH': 4096},
    'MAP_VIRIDIAN_CITY': {'MAP_ROUTE2': 1},
    'MAP_PEWTER_CITY': {'MAP_ROUTE3': 2},
    'MAP_CERULEAN_CITY': {'MAP_ROUTE5': 4, 'MAP_ROUTE9': 4},
    'MAP_ROUTE9': {'MAP_CERULEAN_CITY': 4}
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
    if flag == POKEDEX_FLAG:
        return search_for_needed_maps(pokedex_event, accesible_maps)
    elif flag == FLASH_FLAG:
        return search_for_needed_maps(flash_event, accesible_maps)
    elif flag == CUT_FLAG:
        return search_for_needed_maps(cut_event, accesible_maps)
    elif flag == TEA_FLAG:
        return search_for_needed_maps(tea_event, accesible_maps)
    elif flag == FLY_FLAG:
        return search_for_needed_maps(fly_event, accesible_maps)
    elif flag == STRENGTH_EVENT:
        return search_for_needed_maps(strength_event, accesible_maps)
    elif flag == SILPH_SCOPE_EVENT:
        return search_for_needed_maps(silph_scope_event, accesible_maps)
    elif flag == POKEFLUTE_EVENT:
        return search_for_needed_maps(poke_flute_event, accesible_maps)
    elif flag == SILPHCO_CARD_KEY_EVENT:
        return search_for_needed_maps(silphco_card_key_event, accesible_maps)
    elif flag == GIOVANNI_SILPHCO_EVENT:
        return search_for_needed_maps(giovanni_silphco_event, accesible_maps)
    elif flag == ROCKSMASH_EVENT:
        return search_for_needed_maps(rocksmash_event, accesible_maps)
    elif flag == BIKE_EVENT:
        return search_for_needed_maps(bike_event, accesible_maps)
    elif flag == SURF_EVENT:
        return search_for_needed_maps(surf_event, accesible_maps)
    elif flag == MANSION_EVENT:
        return search_for_needed_maps(mansion_event, accesible_maps)
    elif flag == GYM8_UNLOCK_EVENT:
        return search_for_needed_maps(gym8_unlock_event, accesible_maps)
    elif flag == GYM8_EVENT:
        return search_for_needed_maps(gym8_event, accesible_maps)
    else:
        return False


# If warp_id = -1 we check connection, otherwise we check if there is an accessible warp from warp id
def is_map_progressable(map, accesible_maps, warp_id, ignore=False):
    if not check_progession_blockers(SURF_EVENT, accesible_maps) and map in surf_needed:
        return False
    if not check_progession_blockers(POKEFLUTE_EVENT, accesible_maps) and map in pokeflute_needed:
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
        return True # If map doesn't specify warp routing all warps are accessible
    if from_warp_id not in map_warp_accessibility[map]:
        return False # If warp id isnt in map specifications, warp is not meant to be randomized
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
