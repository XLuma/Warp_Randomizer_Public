"""
White2WarpMapInfo.py

Pokemon White 2 randomizer rules definitions

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
CUT_FLAG = 0
STRENGTH_FLAG = 1
SURF_FLAG = 2
WATERFALL_FLAG = 3
VICTORY_ROAD_GATE = 4
COLRESS_MCHN_EVENT = 5
GYM4_UNLOCK_EVENT = 6
GYM5_UNLOCK_EVENT = 7
GYM8_UNLOCK_EVENT = 8
FLY_FLAG = 9
UNLOCK_FLIGHT_MISTRALTON = 10
#PLASMA_FRIGATE_BARRIER1_UNLOCK = 11 b2 exclsuive
UNLOCK_ALDER_HOUSE = 11
LEGENDARIES = 12
ROUTE4_UNLOCK = 13

END_FLAG = ROUTE4_UNLOCK

cut_event = ['Map_Virbank_City', 'Map_Virbank_City_Interior_h455',
             'Map_Pokestar_Studios_h566']  # 'Map_Pokestar_Studios_h566' issues with that or whatevr
# strength_event = ['Map_Castelia_City_h40', 'Map_Castelia_City_h28', 'Map_Castelia_Sewers_h495']  # in case the other one doesnt work
strength_event = ['Map_Castelia_City_h40',
                  'Map_Castelia_Sewers_h495']  # incomplete, need to check h495 or add more castelia maps
surf_event = ['Map_Driftveil_City_Gym00', 'Map_PWT', 'Map_PWT_Interior_h192',
              'Map_Driftveil_City']  # Map_Route_6 is connected to driftveil no gate, tho might have to add Map_Route_6_Interior_h332 (season research lab)
waterfall_event = ['Map_Victory_Road_h573']
victory_road_gate_event = ['Map_Aspertia_City_Gym00', 'Map_Virbank_City_Interior_h455', 'Map_Castelia_City_Gym00',
                           'Map_Nimbasa_City_Gym00', 'Map_Driftveil_City_Gym00', 'Map_Mistralton_City_Gym00',
                           'Map_Opelucid_City_Gym00', 'Map_Humilau_City_Gym00', 'Map_Victory_Road_h573']
colress_mchn_event = ['Map_Humilau_City_Gym00', 'Map_Route_22', 'Map_Seaside_Cave_h515']
gym4_unlock_event = ['Map_Nimbasa_City_Interior_h585']
gym5_unlock_event = ['Map_Driftveil_City',
                     'Map_Driftveil_City_Interior_h104']  # might not randomise h104 cause we get brought in automaticly
gym8_unlock_event = [
    'Map_Humilau_City']  # trigger next to house spawns gym leader. dude blocks you INSIDE of the gym not outside
fly_event = ['Map_Route_5']
mistralton_flight_event = ['Map_Mistralton_City', 'Map_Mistralton_City_Gym00', 'Map_Celestial_Tower_h338']
#plasma_frigate_barrier1 = ['Map_Plasma_Frigate_h577', 'Map_Plasma_Frigate_h575', 'Map_Plasma_Frigate_h559',
 #                          'Map_Plasma_Frigate_h578', 'Map_Plasma_Frigate_h553']  # unlocks blocked top warp in h553, BBLACK 2 EXCLUSIVE

unlock_alder_house = ['Map_Floccesy_Town', 'Map_Floccesy_Ranch_Interior_h445'] #alder blocks the house until you rescue the herdier
legendaries = ['Map_Route_11', 'Map_Route_13', 'Map_Route_22', 'Map_Marvelous_Bridge_h263', 'Map_Dragonspiral_Tower_Interior_h213', 'Map_Ns_Castle_h273',
                    'Map_Dreamyard_h152', 'Map_Giant_Chasm_Interior_h604', 'Map_Cave_of_Being_h517', 'Map_Celestial_Tower_h342', 'Map_Route_23', 'Map_Nacrene_City',
                       'Map_Reversal_Mountain_Interior_h540']
route4_unlock = ['Map_Castelia_City_Gym00', 'Map_Castelia_City_h30', 'Map_Route_4_h551']

FORCED_FLAG_ORDER = [CUT_FLAG, STRENGTH_FLAG, SURF_FLAG, FLY_FLAG, WATERFALL_FLAG]
FLAG_EVENT_LIST = [cut_event, strength_event, surf_event, waterfall_event, victory_road_gate_event, colress_mchn_event,
                   gym4_unlock_event, gym5_unlock_event, gym8_unlock_event, fly_event, mistralton_flight_event,
                    unlock_alder_house, legendaries, route4_unlock]  # incomplete

no_event_allowed = []  # incomplete
map_chain_breaks = []  # incomplete

# Event Based Warps and Warp Connections
# If map not specified, assume that all warps are accessible
map_warp_accessibility = {
    'Map_Seaside_Cave_h515': {  # header 515 TODO make check for Plasma chased out of Opelucid - what is the flag?
        0: [WT(1, 0)],
        1: [WT(0, 0)],
        2: [WT(0, 4), WT(1, 4), WT(3, 0), WT(4, 0)],
        3: [WT(0, 4), WT(1, 4), WT(4, 0)],
        4: [WT(0, 4), WT(1, 4), WT(3, 0)]
    },
    'Map_Seaside_Cave_h516': {  # header 516
        0: [WT(1, 2)],
        1: []
    },
    'Map_Dreamyard_h152': {  # header 152
        0: [WT(2, 0)],
        1: [WT(0, 2), WT(2, 2), WT(3, 0)],
        2: [WT(0, 0)],
        3: [WT(0, 2), WT(1, 0), WT(2, 2)]
    },
    'Map_Relic_Castle_h160': {  # header 160
        0: [WT(2, 0)],
        1: [WT(0, 0), WT(1, 0)],
        2: [WT(0, 0)]
    },
    'Map_Relic_Castle_h161': { # header 161
        0: [],
        1: []
    },
    'Map_Route_5_h304': {  # header 304 TODO figure out why there is a second route 5 version here
        0: [WT(1, 0)],
        1: []
    },
    'Map_Victory_Road_h573': {  # header 573
        0: [], # this warp is a black exclusive, making it unreachable for our purposes
        1: [WT(0, 0), WT(3, 0)],
        2: [WT(0, 16), WT(1, 16), WT(3, 16)],
        3: [WT(0, 0), WT(1, 0)]
    },
    'Map_Route_20': {  # header 446
        0: [WT(1, 12)],
        1: [WT(0, 12)]
    },
    # TODO come back and add Virbank City - header 448 - guy blocking way to Pokestar (unless he got removed)
    'Map_Chargestone_Cave_Interior_h195': {  # header 195 TODO see if story flags are involved here - bianca? bianca stays until you beat plasma in pwt
        0: [WT(1, 0), WT(2, 0), WT(4, 0)],
        1: [WT(0, 0), WT(2, 0), WT(4, 0)],
        2: [WT(0, 0), WT(1, 0), WT(4, 0)],
        3: [WT(0, 0), WT(1, 0), WT(2, 0), WT(3, 0)],
        4: [WT(0, 0), WT(1, 0), WT(2, 0)]
    },
    'Map_Chargestone_Cave_Interior_h196': {  # header 196
        0: [WT(1, 0), WT(2, 0), WT(3, 0)],
        1: [WT(0, 0), WT(2, 0), WT(3, 0)],
        2: [WT(0, 0), WT(1, 0), WT(3, 0)],
        3: [WT(0, 0), WT(1, 0), WT(2, 0)]
    },
    'Map_Wellspring_Cave_h324': {  # header 324
        0: [WT(1, 4)],
        1: [WT(0, 4)]
    },
    'Map_Twist_Mountain_Interior_h199': {  # header 199
        0: [WT(1, 0)],
        1: [WT(0, 0)],
        2: [],
        3: [WT(4, 0)],
        4: [WT(3, 0)],
        5: [WT(6, 0)],
        6: [WT(5, 0)],
        7: [WT(8, 0), WT(13, 0)],
        8: [WT(7, 0), WT(13, 0)],
        9: [WT(10, 0), WT(11, 0), WT(16, 0)],
        10: [WT(9, 0), WT(11, 0), WT(16, 0)],
        11: [WT(9, 0), WT(10, 0), WT(16, 0)],
        12: [WT(9, 0), WT(10, 0), WT(11, 0), WT(16, 0)],
        13: [WT(7, 0), WT(8, 0)],
        14: [],
        15: [],
        16: [WT(9, 0), WT(10, 0), WT(11, 0)]
    },
    'Map_Twist_Mountain_Interior_h201': {  # header 201
        0: [WT(5, 0)],
        1: [WT(2, 0)],
        2: [WT(1, 0)],
        3: [WT(4, 0), WT(8, 0)],
        4: [WT(3, 0), WT(8, 0)],
        5: [WT(0, 0)],
        6: [WT(7, 0), WT(8, 0), WT(9, 0)],
        7: [WT(9, 0)],
        8: [],
        9: [WT(7, 0)]
    },
    'Map_Route_5': {  # header 329
        0: [WT(1, 0), WT(2, 0)],
        1: [],
        2: [WT(0, 0), WT(1, 0)]
    },
    'Map_Route_6': {  # header 331
        0: [WT(1, 4), WT(2, 0)],
        1: [WT(0, 4), WT(2, 4)],
        2: [WT(0, 0), WT(1, 4)],
    },
    'Map_Mistralton_Cave_h333': {  # header 333 TODO check what NPC next to warp 2 does - does he block progression?
        0: [WT(1, 2), WT(2, 2)],
        1: [WT(0, 2), WT(2, 0)],
        2: [WT(0, 2), WT(1, 0)]
    },
    'Map_Mistralton_Cave_h334': {  # header 334
        0: [WT(1, 2)],
        1: [WT(0, 2)]
    },
    'Map_Dragonspiral_Tower_Interior_h208': {  # header 208
        0: [WT(1, 2)],
        1: []
    },
    'Map_Route_21': {  # header 463
        0: [],
        1: [WT(2, 0)],
        2: [WT(1, 0)]
    },
    'Map_Victory_Road_h587': {  # header 587
        0: [WT(3, 2)],
        1: [WT(0, 2), WT(3, 2)],
        2: [WT(0, 4), WT(3, 6)],
        3: [WT(0, 0)]
    },
    'Map_Victory_Road_h589': {  # header 589
        0: [WT(3, 4)],
        1: [WT(5, 12)],
        2: [WT(4, 0)],
        3: [WT(0, 4)],
        4: [WT(2, 0)],
        5: [WT(1, 12)]
    },
    'Map_Victory_Road_h590': {  # header 590
        0: [],
        1: [WT(0, 2), WT(2, 2), WT(3, 2), WT(4, 2), WT(5, 2), WT(6, 2), WT(7, 2), WT(8, 2)],
        2: [WT(0, 2), WT(1, 2), WT(3, 2), WT(4, 2), WT(5, 2), WT(6, 2), WT(7, 2), WT(8, 2)],
        3: [WT(0, 2), WT(1, 2), WT(2, 2), WT(4, 0), WT(5, 0), WT(6, 0), WT(7, 0), WT(8, 0)],
        4: [WT(0, 2), WT(1, 2), WT(2, 2), WT(3, 0), WT(5, 0), WT(6, 0), WT(7, 0), WT(8, 0)],
        5: [WT(0, 2), WT(1, 2), WT(2, 2), WT(3, 0), WT(4, 0), WT(6, 0), WT(7, 0), WT(8, 0)],
        6: [WT(0, 2), WT(1, 2), WT(2, 2), WT(3, 0), WT(4, 0), WT(5, 0), WT(7, 0), WT(8, 0)],
        7: [WT(0, 2), WT(1, 2), WT(2, 2), WT(3, 0), WT(4, 0), WT(5, 0), WT(6, 0), WT(8, 0)],
        8: [WT(0, 2), WT(1, 2), WT(2, 2), WT(3, 0), WT(4, 0), WT(5, 0), WT(6, 0), WT(7, 0)]
    },
    'Map_Victory_Road_h594': {  # header 594
        0: [WT(3, 2)],
        1: [WT(0, 2), WT(3, 2)],
        2: [WT(0, 4), WT(3, 6)],
        3: [WT(0, 2)]
    },
    'Map_Route_23': {  # header 475
        0: [WT(1, 0), WT(2, 0), WT(3, 4)],
        1: [WT(0, 0), WT(2, 0), WT(3, 4)],
        2: [WT(0, 0), WT(1, 0), WT(3, 4)],
        3: [WT(0, 4), WT(1, 4), WT(2, 4)]
    },
    'Map_Victory_Road_h595': {  # header 595
        0: [WT(3, 0)],
        1: [WT(5, 4)],
        2: [WT(4, 12)],
        3: [WT(0, 0)],
        4: [WT(2, 12)],
        5: [WT(1, 4)]
    },
    'Map_Driftveil_City': {  # header 96
        0: [WT(1, 0), WT(2, 0), WT(3, 0), WT(4, 0), WT(5, 0), WT(6, 0), WT(7, 0), WT(8, 0), WT(9, 128), WT(10, 0),
            WT(11, 0), WT(12, 0), WT(13, 0)],
        1: [WT(0, 0), WT(2, 0), WT(3, 0), WT(4, 0), WT(5, 0), WT(6, 0), WT(7, 0), WT(8, 0), WT(9, 128), WT(10, 0),
            WT(11, 0), WT(12, 0), WT(13, 0)],
        2: [WT(0, 0), WT(1, 0), WT(3, 0), WT(4, 0), WT(5, 0), WT(6, 0), WT(7, 0), WT(8, 0), WT(9, 128), WT(10, 0),
            WT(11, 0), WT(12, 0), WT(13, 0)],
        3: [WT(0, 0), WT(1, 0), WT(2, 0), WT(4, 0), WT(5, 0), WT(6, 0), WT(7, 0), WT(8, 0), WT(9, 128), WT(10, 0),
            WT(11, 0), WT(12, 0), WT(13, 0)],
        4: [WT(0, 0), WT(1, 0), WT(2, 0), WT(3, 0), WT(5, 0), WT(6, 0), WT(7, 0), WT(8, 0), WT(9, 128), WT(10, 0),
            WT(11, 0), WT(12, 0), WT(13, 0)],
        5: [WT(0, 0), WT(1, 0), WT(2, 0), WT(3, 0), WT(4, 0), WT(6, 0), WT(7, 0), WT(8, 0), WT(9, 128), WT(10, 0),
            WT(11, 0), WT(12, 0), WT(13, 0)],
        6: [WT(0, 0), WT(1, 0), WT(2, 0), WT(3, 0), WT(4, 0), WT(5, 0), WT(7, 0), WT(8, 0), WT(9, 128), WT(10, 0),
            WT(11, 0), WT(12, 0), WT(13, 0)],
        7: [WT(0, 0), WT(1, 0), WT(2, 0), WT(3, 0), WT(4, 0), WT(5, 0), WT(6, 0), WT(8, 0), WT(9, 128), WT(10, 0),
            WT(11, 0), WT(12, 0), WT(13, 0)],
        8: [WT(0, 0), WT(1, 0), WT(2, 0), WT(3, 0), WT(4, 0), WT(5, 0), WT(6, 0), WT(7, 0), WT(9, 128), WT(10, 0),
            WT(11, 0), WT(12, 0), WT(13, 0)],
        9: [WT(0, 0), WT(1, 0), WT(2, 0), WT(3, 0), WT(4, 0), WT(5, 0), WT(6, 0), WT(7, 0), WT(8, 0), WT(10, 0),
            WT(11, 0), WT(12, 0), WT(13, 0)],
        10: [WT(0, 0), WT(1, 0), WT(2, 0), WT(3, 0), WT(4, 0), WT(5, 0), WT(6, 0), WT(7, 0), WT(8, 0), WT(9, 128),
             WT(11, 0), WT(12, 0), WT(13, 0)],
        11: [WT(0, 0), WT(1, 0), WT(2, 0), WT(3, 0), WT(4, 0), WT(5, 0), WT(6, 0), WT(7, 0), WT(8, 0), WT(9, 128),
             WT(10, 0), WT(12, 0), WT(13, 0)],
        12: [WT(0, 0), WT(1, 0), WT(2, 0), WT(3, 0), WT(4, 0), WT(5, 0), WT(6, 0), WT(7, 0), WT(8, 0), WT(9, 128),
             WT(10, 0), WT(11, 0), WT(13, 0)],
        13: [WT(0, 0), WT(1, 0), WT(2, 0), WT(3, 0), WT(4, 0), WT(5, 0), WT(6, 0), WT(7, 0), WT(8, 0), WT(9, 128),
             WT(10, 0), WT(11, 0), WT(12, 0)]
    },
    #'Map_Giant_Chasm_Interior_h231': {
    #    # header 231 TODO luma either make an event for beating plasma frigate and add it to this accessibility or move the grunts and delete this entire entry
    #    0: [WT(1, 0), WT(2, 0), WT(3, 0)],
    #    1: [WT(0, 0), WT(2, 0), WT(3, 0)],
    #    2: [WT(0, 0), WT(1, 0), WT(3, 0)],
    #    3: [],
    #    4: []
    #}, keeping just in case
    'Map_Giant_Chasm_Interior_h233': {
        0: [WT(2, 0)],
        1: [WT(3, 0)],
        2: [WT(0, 0)],
        3: [WT(1, 0)]
    },
    'Map_Relic_Passage_h504': {
        0: [],
        1: [WT(2, 0), WT(3, 2)],
        2: [WT(1, 0), WT(3, 2)],
        3: []
    },
    # 'Map_Village_Bridge_h255':{
    #    This map has surf tiles, but you dont need surf. A dude in the middle wont let you pass if you cant defeat him tho, but doesnt matter
    # }
    'Map_Clay_Tunnel_h508': {  # header 508
        0: [WT(4, 0)],
        1: [],
        2: [],
        3: [WT(0, 2), WT(4, 2)],
        4: [WT(0, 0)]
    },
    # Map_Clay_Tunnel_h507 is accessible fully
    # Map_Route_15 header 378 is accessible fully
    # Map_Relic_Passage_h505 is accessible fully
    # Map_Abundant_Shrine_h376 is accessible fully

    'Map_Relic_Passage_h503': {  # header 503
        0: [WT(1, 0), WT(1, 2)],
        1: [],
        2: []
    },
    'Map_Route_14': {  # header 374
        0: [WT(1, 4)],
        1: [WT(0, 12)]
    },
    # header 506 is accessible fully
    # header 370 is accessible fully
    'Map_Icirrus_City': {  # header 113
        0: [WT(1, 0), WT(2, 0), WT(3, 0), WT(4, 0), WT(5, 0)],
        1: [WT(0, 0), WT(2, 0), WT(3, 0), WT(4, 0), WT(5, 0)],
        2: [WT(1, 0), WT(0, 0), WT(3, 0), WT(4, 0), WT(5, 0)],
        3: [WT(1, 0), WT(2, 0), WT(0, 0), WT(4, 0), WT(5, 0)],
        4: [WT(1, 0), WT(2, 0), WT(3, 0), WT(0, 0), WT(5, 0)],
        5: [WT(1, 0), WT(2, 0), WT(3, 0), WT(4, 0), WT(0, 0)],
        6: [WT(1, 0), WT(2, 0), WT(3, 0), WT(4, 0), WT(5, 0), WT(0, 0)],  # only warp blocked by a ledge down
    },
    # header 495 is accessible fully
    # header 238 is fully acessible

    'Map_Royal_Unova_h52': {  # header 52
        0: [WT(1, 0), WT(2, 0), WT(3, 0), WT(4, 0), WT(5, 0), WT(6, 0), WT(7, 0), WT(8, 0), WT(9, 0), WT(10, 0), WT(11, 0), WT(12, 0), WT(13, 0), WT(28, 0)],
        1: [WT(0, 0), WT(2, 0), WT(3, 0), WT(4, 0), WT(5, 0), WT(6, 0), WT(7, 0), WT(8, 0), WT(9, 0), WT(10, 0), WT(11, 0), WT(12, 0), WT(13, 0), WT(28, 0)],
        2: [WT(0, 0), WT(1, 0), WT(3, 0), WT(4, 0), WT(5, 0), WT(6, 0), WT(7, 0), WT(8, 0), WT(9, 0), WT(10, 0), WT(11, 0), WT(12, 0), WT(13, 0), WT(28, 0)],
        3: [WT(0, 0), WT(1, 0), WT(2, 0), WT(4, 0), WT(5, 0), WT(6, 0), WT(7, 0), WT(8, 0), WT(9, 0), WT(10, 0), WT(11, 0), WT(12, 0), WT(13, 0), WT(28, 0)],
        4: [WT(0, 0), WT(1, 0), WT(2, 0), WT(3, 0), WT(5, 0), WT(6, 0), WT(7, 0), WT(8, 0), WT(9, 0), WT(10, 0), WT(11, 0), WT(12, 0), WT(13, 0), WT(28, 0)],
        5: [WT(0, 0), WT(1, 0), WT(2, 0), WT(3, 0), WT(4, 0), WT(6, 0), WT(7, 0), WT(8, 0), WT(9, 0), WT(10, 0), WT(11, 0), WT(12, 0), WT(13, 0), WT(28, 0)],
        6: [WT(0, 0), WT(1, 0), WT(2, 0), WT(3, 0), WT(4, 0), WT(5, 0), WT(7, 0), WT(8, 0), WT(9, 0), WT(10, 0), WT(11, 0), WT(12, 0), WT(13, 0), WT(28, 0)],
        7: [WT(0, 0), WT(1, 0), WT(2, 0), WT(3, 0), WT(4, 0), WT(5, 0), WT(6, 0), WT(8, 0), WT(9, 0), WT(10, 0), WT(11, 0), WT(12, 0), WT(13, 0), WT(28, 0)],
        8: [WT(0, 0), WT(1, 0), WT(2, 0), WT(3, 0), WT(4, 0), WT(5, 0), WT(6, 0), WT(7, 0), WT(9, 0), WT(10, 0), WT(11, 0), WT(12, 0), WT(13, 0), WT(28, 0)],
        9: [WT(0, 0), WT(1, 0), WT(2, 0), WT(3, 0), WT(4, 0), WT(5, 0), WT(6, 0), WT(7, 0), WT(8, 0), WT(10, 0), WT(11, 0), WT(12, 0), WT(13, 0), WT(28, 0)],
        10: [WT(0, 0), WT(1, 0), WT(2, 0), WT(3, 0), WT(4, 0), WT(5, 0), WT(6, 0), WT(7, 0), WT(8, 0), WT(9, 0), WT(11, 0), WT(12, 0), WT(13, 0), WT(28, 0)],
        11: [WT(0, 0), WT(1, 0), WT(2, 0), WT(3, 0), WT(4, 0), WT(5, 0), WT(6, 0), WT(7, 0), WT(8, 0), WT(9, 0), WT(10, 0), WT(12, 0), WT(13, 0), WT(28, 0)],
        12: [WT(0, 0), WT(1, 0), WT(2, 0), WT(3, 0), WT(4, 0), WT(5, 0), WT(6, 0), WT(7, 0), WT(8, 0), WT(9, 0), WT(10, 0), WT(11, 0), WT(13, 0), WT(28, 0)],
        13: [WT(0, 0), WT(1, 0), WT(2, 0), WT(3, 0), WT(4, 0), WT(5, 0), WT(6, 0), WT(7, 0), WT(8, 0), WT(9, 0), WT(10, 0), WT(11, 0), WT(12, 0), WT(28, 0)],
        14: [],
        15: [],
        16: [],
        17: [],
        18: [],
        19: [],
        20: [],
        21: [],
        22: [],
        23: [],
        24: [],
        25: [],
        26: [],
        27: [],
        28: [WT(0, 0), WT(1, 0), WT(2, 0), WT(3, 0), WT(4, 0), WT(5, 0), WT(6, 0), WT(7, 0), WT(8, 0), WT(9, 0), WT(10, 0), WT(11, 0), WT(12, 0), WT(13, 0)],
        29: []
    },
    'Map_Dreamyard_h153': { # header 153
        0: [WT(1, 0)],
        1: [WT(0, 0)],
        2: []
    },
    'Map_Reversal_Mountain': { # header 461
        0: [],
        1: [WT(6, 0)],
        2: [],
        3: [],
        4: [],
        5: [],
        6: [WT(1, 0)]
    }

}

# TODO Fill Out Later
map_to_map_warp_accessibility = {

}

cant_go_back_warps = {
    'Map_Pokemon_League_h137': [0],
    # league lobby, all elite 4 rooms you can co back unless you go too far and trigger their intro animations
}

# Handles Connection Requirements
cut_needed = [  # TODO make work
    # cut isnt needed to get anywhere except postgame content
    'Map_Dreamyard_h152'
]
surf_needed = [  # TODO make work
    'Map_Route_21', 'Map_Seaside_Cave_h515'
]
strength_needed = [  # TODO make work
    'Map_Route_36', 'Map_Seaside_Cave_h516', 'Map_Victory_Road_h594', 'Map_Victory_Road_h590',
    'Map_Clay_Tunnel_h506', 'Map_Clay_Tunnel_h507', 'Map_Clay_Tunnel_h508'
]

# TODO finish work
dont_randomize = [
    'Map_Aspertia_City_Interior_h428', 'Map_Virbank_City_Gym00',  #
    # 'Map_Aspertia_City_Center00', #protection for bianca sequence, instead of the whole city
    'Map_Driftveil_City_Interior_h104',
    'Map_Route_6_Interior_h332', 'Map_Black_City_h0', 'Map_White_Treehollow_h478', 'Map_Unity_Tower_Interior_h148',
    'Map_Unity_Tower', 'Map_Victory_Road_h589',
    'Map_Route_4_Interior_h328', 'Map_Route_4_Interior_h327', 'Map_Route_4_Interior_h520', 'Map_Route_4_Interior_h522',
    'Map_Route_4_Interior_h524', 'Map_Route_4_Interior_h519', 'Map_Route_4_Interior_h521', 'Map_Route_4_Interior_h523',
    'Map_Route_4_Interior_h525', 'Map_Black_City_Center00', 'Map_Black_City_h294',
    'Map_Black_City_h2', 'Map_Black_City_h5', 'Map_Black_Tower_h479',
    'Map_Pokemon_League_h145', 'Map_PWT_Interior_h193', 'Map_Pokestar_Studios_h568', 'Map_Pokestar_Studios_h574',
    'Map_Ns_Castle_h277', 
    'Map_Pokestar_Studios_h567', 'Map_Reversal_Mountain_Interior_h531', 'Map_Reversal_Mountain_Interior_h535',
    'Map_Reversal_Mountain_Interior_h533', 'Map_Reversal_Mountain_Interior_h532', 'Map_Reversal_Mountain_Interior_h534',
    'Map_Reversal_Mountain_Interior_h536', 'Map_Icirrus_City_Interior_h118', 'Map_Ns_Castle_h274',
    'Map_Giant_Chasm_Interior_h233', #we arent supposed to EVER access this map
    'Map_Route_4_h326', #black 2 exclusive,
    #'Map_Plasma_Frigate_h562', #we are never reaching this map
    'Map_Victory_Road_h587', # black exclusive
    #CAVE OF BEING NOT INITIALIZED
]

dont_randomize_warp = {  # TODO finish work
    # 'Map_Aspertia_City': [1], #player house
    # 'Map_Driftveil_City': [10], #old plasma event, unlocks gym5 entry
    # 'Map_Route_6': [0], #season research center, cheren brings you in and gives you surf inside
    'Map_Nimbasa_Interior_h84': [2],  # stoopid warp
    'Map_Nimbasa_Interior_h79': [1],  # stadium interior warp pad
    'Map_Royal_Unova_h52':      [14, 17, 18, 19, 20, 23, 25, 27, 15, 16, 29, 21, 22, 24, 26], #useless rooms
    'Map_PWT': [3], #warp that dissapears to plasma frigate
    'Map_Route_21': [2], #warp that dissapears to plasma frigate
    'Map_Plasma_Frigate_h552': [7, 6, 4],
    'Map_Nimbasa_City': [7], # to gear station
    #'Map_Gear_Station_h66': [8], # to nimbasa but its dummied out so we just wanna make sure yk
}

not_needed = [
    # TODO finish work, this likely is partially incorrect thanks to ends containing some maps which it shouldn't/missing some that it should
    #'Map_Castelia_City_h36', if we can touch liberty island
    #'Map_Castelia_City_h39', map with unova royal could also be very funny
    'Map_Plasma_Frigate_h553', #black 2 frigate exclusive
    'Map_Plasma_Frigate_h552', #Main frigate deck
    'Map_Plasma_Frigate_h562', #second iteration they are here so h558 isnt fucked over
    'Map_Plasma_Frigate_h563', #some map
    'Map_Pokemon_League_h138', 'Map_Accumula_Town_Interior_h402', 'Map_Pokestar_Studios_h586',
    'Map_Opelucid_City_Interior_h126', 'Map_Nimbasa_City_Interior_h93', 'Map_Aspertia_City_Interior_h429',
    'Map_Bridge_Gate_h366', 'Map_Lacunosa_Town_Interior_h410', 'Map_Striaton_City_Interior_h9',
    'Map_Driftveil_City_Interior_h101', 'Map_Twist_Mountain_Interior_h204', 'Map_Poke_Transfer_Lab_h381', 'Map_Route_13_Interior_h371', 'Map_Route_Gate_h318', 'Map_Route_Gate_h159',
    'Map_Nimbasa_Gate_h91', 'Map_Opelucid_City_Interior_h134', 'Map_Nacrene_City_Interior_h26', 'Map_Nimbasa_Gate_h92',
    'Map_Shopping_Mall_Interior_h351', 'Map_Village_Bridge_h256',
    'Map_Lentimas_Town_Interior_h608', 'Map_Strange_House_h513', 'Map_Guidance_Chamber_h335',
    'Map_Dragonspiral_Tower_Interior_h212', 'Map_Mistralton_City_Interior_h112',
    'Map_Route_23_Interior_h476', 'Map_Route_6_Interior_h332', 'Map_Route_15_Interior_h382',
    'Map_Giant_Chasm_Interior_h232', 'Map_Floccesy_Town_Interior_h442', 'Map_Anville_Town_h420',
    'Map_White_Treehollow_h478', 'Map_Abundant_Shrine_h377',
    'Map_Lacunosa_Town_Interior_h408', 'Map_Icirrus_City_Interior_h116', 'Map_Plasma_Frigate_h556', #h556 needs to stay here
    'Map_Gear_Station_Interior_h69', 'Map_Village_Bridge_h258', 'Map_Nimbasa_City_Interior_h83',
    'Map_Floccesy_Town_Interior_h440', 'Map_Nimbasa_City_Interior_h81', 'Map_Castelia_Sewers_h499',
    'Map_Striaton_City_Interior_h14', 'Map_Castelia_City_h44', 'Map_Striaton_City_Interior_h10',
    'Map_Accumula_Town_Interior_h400', 'Map_Nimbasa_City_Interior_h95', 'Map_Rumination_Field_Interior_h156',
    'Map_Castelia_City_h501', 'Map_Floccesy_Town_Interior_h441', 'Map_Nimbasa_City_Interior_h85',
    'Map_Humilau_City_Interior_h470', 'Map_Gear_Station_Interior_h72', 'Map_Opelucid_City_Interior_h125',
    'Map_Opelucid_City_Interior_h123', 'Map_Relic_Castle_h175', 'Map_Musical_Theater_Interior_h77',
    'Map_Castelia_City_h43', 'Map_Accumula_Town_Interior_h399', 
    'Map_Reversal_Mountain_Interior_h534', 'Map_Pledge_Grove_Interior_h614', 'Map_Lostlorn_Forest_h385',
    'Map_Opelucid_City_Interior_h128', 'Map_Route_4_Interior_h528', 'Map_Nacrene_City_Interior_h17',
    'Map_Castelia_City_h53', 'Map_Castelia_City_h58', 'Map_Route_13_Interior_h373', 'Map_Castelia_City_h56',
    'Map_Undella_Town_Interior_h415', 'Map_Strange_House_h570', 'Map_Driftveil_City_Interior_h102',
    'Map_Aspertia_City_Interior_h430', 'Map_Opelucid_City_Interior_h127', 'Map_Driftveil_City_Interior_h103',
    'Map_Village_Bridge_h259', 'Map_Village_Bridge_h605', 'Map_Driftveil_City_Interior_h100',
    'Map_Virbank_City_Interior_h451', 'Map_Aspertia_City_Interior_h432', 'Map_Chargestone_Cave_Interior_h197',
    'Map_Nimbasa_City_Interior_h87', 'Map_Dragonspiral_Tower_Interior_h210', 'Map_Gear_Station_Interior_h73',
    'Map_Accumula_Gate', 'Map_Opelucid_City_Interior_h124', 'Map_Striaton_City_Interior_h13',
    'Map_Gear_Station_Interior_h74', 'Map_Nuvema_Town_Interior_h396', 'Map_Humilau_City_Interior_h467',
    'Map_Nimbasa_City_Interior_h82', 'Map_Lacunosa_Town_Interior_h411', 'Map_Aspertia_City_Interior_h433',
    'Map_Join_Avenue_h491', 'Map_Opelucid_City_Interior_h129', 'Map_Castelia_City_h49', 'Map_Nuvema_Town_Interior_h395',
    'Map_Strange_House_h572', 'Map_Nimbasa_City_Interior_h94',
    'Map_Castelia_City_h47', 'Map_Icirrus_City_Interior_h114', 'Map_Nimbasa_City_Interior_h88',
    'Map_Opelucid_City_Interior_h135', 'Map_Virbank_Complex_Interior_h457', 'Map_Aspertia_City_Interior_h431',
    'Map_Nimbasa_City_Interior_h80', 'Map_Nimbasa_City_Interior_h89', 'Map_Castelia_Sewers_h497',
    'Map_Route_7_Interior_h343', 'Map_Route_11_Interior_h367', 'Map_Humilau_City_Interior_h469',
    'Map_Nuvema_Town_Interior_h391', 'Map_Twist_Mountain_Interior_h509', 'Map_Nacrene_City_Interior_h21',
    'Map_Route_18_Interior_h388', 'Map_Virbank_City_Interior_h449', 'Map_Virbank_Gate_h447', 'Map_Virbank_Gate_h453',
    'Map_Plasma_Frigate_h582', 'Map_Anville_Town_h419', 'Map_Gear_Station_Interior_h68',
    'Map_Striaton_City_Interior_h12', 'Map_Humilau_City_Interior_h468', 'Map_Plasma_Frigate_h583',
    'Map_Relic_Passage_h505', 'Map_Accumula_Town_Interior_h405', 'Map_Route_4_Interior_h526', 'Map_Relic_Castle_h178',
    'Map_Bridge_Gate_h369', 'Map_Strange_House_h569', 'Map_Accumula_Town_Interior_h404', 'Map_Plasma_Frigate_h554',
    'Map_Lentimas_Town_Interior_h459', 'Map_Ns_Castle_h278',
    'Map_Striaton_City_Interior_h11', 'Map_Plasma_Frigate_h581',
    'Map_Anville_Town_h421', 'Map_Route_5_Interior_h330', 'Map_Humilau_City_Interior_h466', 'Map_Plasma_Frigate_h580',
    'Map_Nuvema_Town_Interior_h392', 'Map_Route_23_Interior_h477',
    'Map_Opelucid_City_Interior_h130', 'Map_Lacunosa_Town_Interior_h409', 'Map_White_Forest_h426',
    'Map_Reversal_Mountain_Interior_h538', 'Map_Castelia_City_h54', 'Map_Virbank_City_Interior_h450',
    'Map_Plasma_Frigate_h579', 'Map_Striaton_City_Interior_h15', 'Map_Nacrene_City_Interior_h25',
    'Map_Nacrene_City_Interior_h19', 'Map_Nuvema_Town_Interior_h394', 'Map_Route_4_Interior_h530',
    'Map_Plasma_Frigate_h557', 'Map_Route_4_Interior_h529', 'Map_Aspertia_City_Interior_h428',
    'Map_Nacrene_Gate', 'Map_Castelia_City_h500', 'Map_Village_Bridge_h260', 'Map_Moor_of_Icirrus_h346',
    'Map_Gear_Station_Interior_h71', 'Map_P2_Laboratory_Interior_h239', 'Map_Accumula_Town_Interior_h403',
    'Map_Castelia_City_h60', 'Map_Castelia_Sewers_h498', 'Map_Aspertia_City_Interior_h434',
    'Map_Reversal_Mountain_Interior_h532', 'Map_Village_Bridge_h257', 'Map_Accumula_Town_Interior_h401',
    'Map_Relic_Castle_h182', 'Map_Underground_Ruins_h565', 'Map_Castelia_Sewers_h496', 'Map_Wellspring_Cave_h325',
    'Map_Route_6_Interior_h336', 'Map_Castelia_City_h42', 'Map_Route_4_Interior_h527',
    'Map_Village_Bridge_h261', 'Map_Abundant_Shrine_h376', 'Map_Relic_Castle_h176', 'Map_Strange_House_h571',
    'Map_Striaton_City_Interior_h7', 'Map_Opelucid_Gate_h133', 'Map_Opelucid_Gate_h131',
    'Map_Skyarrow_Bridge_h249', 'Map_Nuvema_Town_Interior_h393', 'Map_Gear_Station_Interior_h67',
    'Map_Icirrus_City_Interior_h119', 'Map_Route_7_Interior_h344',
    'Map_Gear_Station_Interior_h70', 'Map_Nimbasa_City_Interior_h86', 'Map_Strange_House_h462', 'Map_Strange_House_h510',
    'Map_Strange_House_h511', 'Map_Strange_House_h512', 'Map_Strange_House_h514', 'Map_Victory_Road_h214', 'Map_Black_Gate_h379', 'Map_Black_Gate_h375'
]

non_navigable_connections = [  # TODO finish work

]

connection_to_connection_rules = {}

grouped_warps = {

}

other_overwrites = {
    "Aspertia City": {
        'resource_folder': 'aspertia_city_h427',
        'event_overwrite': 163,
    },
    "Bridge Gate 252": {
        'resource_folder': 'bridge_gate_h252',
        'event_overwrite': 398,
    },
    "Bridge Gate 349": {
        'resource_folder': 'bridge_gate_h349',
        'event_overwrite': 518,
    },
    "Bridge Gate 384": {
        'resource_folder': 'bridge_gate_h384',
        'event_overwrite': 553,
        'script_overwrite': 768
    },
    "Bridge Gate 414": {
        'resource_folder': 'bridge_gate_h414',
        'event_overwrite': 591,
    },
    "Driftveil City": {
        'resource_folder': 'driftveil_city_h96',
        'event_overwrite': 101,
    },
    "Nimbasa City": {
        'resource_folder': 'nimbasa_city_h62',
        'event_overwrite': 66,
        'script_overwrite': 124,
    },
    "Twist Mountain 198": {
        'resource_folder': 'twist_mountain_h198',
        'event_overwrite': 247,
    },
    "Virbank City 452": {
        'resource_folder': 'virbank_city_h452',
        'event_overwrite': 181,
    },
    "Seaside Cave 515": {
        'resource_folder': 'seaside_cave_h515',
        'script_overwrite': 1030,
    },
    "Giant Chasm 604": {
        'resource_folder': 'giant_chasm_h604',
        'script_overwrite': 1208,
    },
    "Aspertia City Center00": {
        'resource_folder': 'aspertia_city_center00',
        'script_overwrite': 870,
    },
    "Virbank City": {
        'resource_folder': 'virbank_city',
        'event_overwrite': 174,
    },
    "Mistralton City":{
        'resource_folder': 'mistralton_city',
        'script_overwrite': 214,
        'event_overwrite': 120,
    },
    "Mistralton Gym": {
        'resource_folder': 'mistralton_gym',
        'script_overwrite': 216,
    },
    "Giant Chasm 281": {
        'resource_folder': 'giant_chasm_231',
        'event_overwrite': 281,
    },
    "Cynthia House": {
        'resource_folder': 'undella_cynthia_h416',
        'script_overwrite' : 832, #hehe
    },
    "Player House": {
        'resource_folder': 'aspertia_city_h428',
        'script_overwrite': 856,
    },
    "PWT Interior": {
        'resource_folder': 'pwt_h192',
        'script_overwrite': 384,
    },
    'Plasma frigate 552': {
        'resource_folder': 'plasma_frigate_h552',
        'event_overwrite': 344,
    },
    "Opelucid Gym": {
        'resource_folder': 'opelucid_gym',
        'script_overwrite': 242,
    },
    'Route 21': {
        'resource_folder': 'route_21',
        'script_overwrite': 926,
    },
    'Anville town': {
        'resource_folder': 'anville_town_h418',
        'script_overwrite': 836,
    },
    "Castelia City 40": {
        'resource_folder': 'castelia_city_h40',
        'script_overwrite': 80,
    },
    "Castelia City 39": { # header 39
        'resource_folder': 'castelia_city_h39',
        'script_overwrite': 78,
    },
    "Victory road 592": { # header 592
        'resource_folder': 'victory_road_h592',
        'script_overwrite': 1184,
    },
    "Pokemon league 136": { # header 136
        'resource_folder': 'pokemon_league_h136',
        'script_overwrite': 272,
    },
    "Aspertia Gym 1": { # header 489
        'resource_folder': 'aspertia_city_gym',
        'script_overwrite': 978,
    },
    "Driftveil Gym": { # header 97
        'resource_folder': 'driftveil_city_gym',
        'script_overwrite': 194,
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
    # if not check_progession_blockers(ROCKSMASH_FLAG, accesible_maps) and map in rocksmash_needed:
    #   return False
    if not check_progession_blockers(CUT_FLAG, accesible_maps) and map in cut_needed:
        return False
    # if not check_progession_blockers(BIKE_FLAG, accesible_maps) and map in bike_needed:
    #   return False
    if not check_progession_blockers(STRENGTH_FLAG, accesible_maps) and map in strength_needed:
        return False
    # if not check_progession_blockers(WHIRLPOOL_FLAG, accesible_maps) and map in whirlpool_needed:
    #   return False
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
