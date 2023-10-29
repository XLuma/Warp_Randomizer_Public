"""
White2DebugMain.py

Debug helper for initial White 2 support

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

from nds.buffer import Buffer
from nds.gen5.FormatsGen5 import *
from White2ReadWriteHandler import *

import ndspy.rom
import ndspy.narc
import ndspy.codeCompression

rom = ndspy.rom.NintendoDSRom.fromFile('../White2.nds')
events_narc = ndspy.narc.NARC(rom.getFileByName('/a/1/2/6'))
events = []
event = 0

for i in range(len(events_narc.files)):
    event = Overworlds(Buffer(events_narc.files[i]))
    events.append(event)

# matrix_narc = ndspy.narc.NARC(rom.getFileByName('/a/0/0/9'))
# matrices = []
#
# for i in range(len(matrix_narc.files)):
#     matrix = Matrix(Buffer(matrix_narc.files[i]))
#     matrices.append(matrix)
#
# maps_narc = ndspy.narc.NARC(rom.getFileByName('/a/0/0/8'))
# maps = []
#
# for i in range(len(maps_narc.files)):
#     map = Map(Buffer(maps_narc.files[i]), i)
#     maps.append(map)

# maps[280].permissions.layers[2].print()
# maps[279].permissions.layers[2].print()

# names = []
headers = []
# with open('w2 locations.txt') as infile:
#     for line in infile.readlines():
#         names.append(line.replace('\n', ''))
headers_narc = ndspy.narc.NARC(rom.getFileByName('/a/0/1/2'))
buffer = Buffer(headers_narc.files[0])
# print('num headers: %i' % (len(buffer.data)/0x30))
# max = 0

# flag_values = [0x1D, 0x3D, 0x3F, 0x40, 0x72, 0x73, 0x74, 0x75]
# collision_values = [0x16, 0x56, 0x13, 0x1]
# matching_headers = set()
for i in range(615):
    header = White2Header(buffer, i)
    headers.append(header)
    # if len(events[header.event_id].warps) >= 2:
    #     for npc in events[header.event_id].npcs:
    #         if npc.script == 10004 or npc.script == 10000:
    #             matching_headers.add(header.id)
    #     matrix = matrices[header.matrix_id]
    #     map_locations = matrix.get_maps_by_header(header.id)
    #     for coord_tuple in map_locations:
    #         map_id = matrix.get_map(coord_tuple[1], coord_tuple[0])
    #         map_obj = Map(Buffer(maps_narc.files[map_id]), map_id)
    #         found = False
    #         if map_obj.magic != 0x474E:
    #             for row in map_obj.permissions.layers[2].table:
    #                 for cell in row:
    #                     if cell in flag_values:
    #                         found = True
    #         if found:
    #             matching_headers.add(header.id)


# print('Located %i matching headers' % len(matching_headers))

#
# # print(max)
handler = White2ReadWriteHandler()
handler.build_lists(rom, headers)
