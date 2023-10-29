"""
FormatsGen5.py

Class definitions for the 5th generation of Pokemon Games

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
from nds.buffer import Buffer
from enum import Enum


class White2Header:
    def __init__(self, buffer, id):
        self.id = id

        self.map_type = buffer.read_u8()
        self.map_change = buffer.read_u8()
        self.texture_container_idx = buffer.read_u16()
        self.matrix_id = buffer.read_u16()
        self.scripts_id = buffer.read_u16()
        self.init_scripts_idx = buffer.read_u16()
        self.text_container_idx = buffer.read_u16()

        self.bgms = buffer.read_bytes(0x8)
        self.wild_poke_container_idx = buffer.read_u16()
        self.event_id = buffer.read_u16()
        self.parent_header_id = buffer.read_u16()
        self.name_idx = buffer.read_u16()

        self.env_flags = buffer.read_u16()
        self.flags_and_background = buffer.read_u16()
        self.remainder = buffer.read_bytes(16)

    def write(self):
        size = 0x30
        buffer = Buffer(bytearray(size), write=True)

        buffer.write_u8(self.map_type)
        buffer.write_u8(self.map_change)
        buffer.write_u16(self.texture_container_idx)
        buffer.write_u16(self.matrix_id)
        buffer.write_u16(self.scripts_id)
        buffer.write_u16(self.init_scripts_idx)
        buffer.write_u16(self.text_container_idx)
        buffer.write_bytes(self.bgms)
        buffer.write_u16(self.wild_poke_container_idx)
        buffer.write_u16(self.event_id)
        buffer.write_u16(self.parent_header_id)
        buffer.write_u16(self.name_idx)
        buffer.write_u16(self.env_flags)
        buffer.write_u16(self.flags_and_background)
        buffer.write_bytes(self.remainder)

        return buffer.data

    def set_teleport_flag(self):
        # I'm sure one of these also will enable teleport
        # self.flags_and_background |= (1 << 11)  # can run
        self.flags_and_background |= (1 << 12)  # can escape rope
        self.flags_and_background |= (1 << 13)  # can fly

    def __str__(self):
        return str(self.id) + ":" + \
               "\nmap type: " + str(self.map_type) + \
               "\nmap change: " + str(self.map_change) + \
               "\ntexture container idx: " + str(self.texture_container_idx) + \
               "\nmatrix id: " + str(self.matrix_id) + \
               "\nscripts id: " + str(self.scripts_id) + \
               "\ninit scripts idx: " + str(self.init_scripts_idx) + \
               "\ntext container idx: " + str(self.text_container_idx) + \
               "\nmusic: " + str(self.bgms) + \
               "\nwild: " + str(self.wild_poke_container_idx) + \
               "\nevents id: " + str(self.event_id) + \
               "\nparent header id: " + str(self.parent_header_id) + \
               "\nname idx: " + str(self.name_idx) + \
               "\nenv flags: " + str(self.env_flags) + \
               "\nother flags: " + str(self.flags_and_background) + \
               "\nremainder: " + str(self.remainder)


class Matrix:
    def __init__(self, buffer):
        self.headers_flag = buffer.read_s32()
        self.x = buffer.read_u16()
        self.y = buffer.read_u16()
        self.maps = []
        self.headers = []

        for row in range(self.y):
            entry = []
            for col in range(self.x):
                entry.append(buffer.read_s32())
            self.maps.append(entry)

        if self.headers_flag == 1:
            for row in range(self.y):
                entry = []
                for col in range(self.x):
                    entry.append(buffer.read_s32())
                self.headers.append(entry)

    def get_map(self, row, col):
        return self.maps[row][col]

    def get_header(self, row, col):
        return self.headers[row][col]

    def get_maps_by_header(self, header_id):
        ret = []
        for row in range(self.y):
            for col in range(self.x):
                if self.headers:
                    if self.headers[row][col] == header_id:
                        ret.append((col, row))
                else:
                    ret.append((col, row))
        return ret

    def write(self):
        size = (self.y * self.x * 4) + 4 + 2 + 2
        if self.headers_flag == 1:
            size += self.y * self.x * 4
        buffer = Buffer(bytearray(size), write=True)

        buffer.write_u32(self.headers_flag)
        buffer.write_u8(self.x)
        buffer.write_u8(self.y)

        for row in range(self.y):
            for col in range(self.x):
                buffer.write_u32(self.maps[row][col])

        if self.headers_flag == 1:
            for row in range(self.y):
                for col in range(self.x):
                    buffer.write_u32(self.headers[row][col])

        return buffer.data

    def get_connected_maps(self, row, col, headers, header_id):
        ret = []
        name_prefix = 'm' + str(headers[header_id].matrix_id) + ':ad' + str(
            headers[header_id].texture_container_idx) + ':h'
        if not self.headers:
            if row - 1 >= 0:
                ret.append(name_prefix + str(header_id) + ':x' + str(col) + ':y' + str(row - 1))
            if col + 1 < self.x:
                ret.append(name_prefix + str(header_id) + ':x' + str(col + 1) + ':y' + str(row))
            if row + 1 < self.y:
                ret.append(name_prefix + str(header_id) + ':x' + str(col) + ':y' + str(row + 1))
            if col - 1 >= 0:
                ret.append(name_prefix + str(header_id) + ':x' + str(col - 1) + ':y' + str(row))
        else:
            if row - 1 >= 0:
                if headers[self.get_header(row - 1, col)].area_data_id == headers[header_id].texture_container_idx:
                    ret.append(
                        name_prefix + str(self.get_header(row - 1, col)) + ':x' + str(col) + ':y' + str(row - 1))
            if col + 1 < self.x:
                if headers[self.get_header(row, col + 1)].area_data_id == headers[header_id].texture_container_idx:
                    ret.append(
                        name_prefix + str(self.get_header(row, col + 1)) + ':x' + str(col + 1) + ':y' + str(row))
            if row + 1 < self.y:
                if headers[self.get_header(row + 1, col)].area_data_id == headers[header_id].texture_container_idx:
                    ret.append(
                        name_prefix + str(self.get_header(row + 1, col)) + ':x' + str(col) + ':y' + str(row + 1))
            if col - 1 >= 0:
                if headers[self.get_header(row, col - 1)].area_data_id == headers[header_id].texture_container_idx:
                    ret.append(
                        name_prefix + str(self.get_header(row, col - 1)) + ':x' + str(col - 1) + ':y' + str(row))

        return ret

    def get_connected_headers(self, row, col, headers, header_id):
        ret = set()

        if row - 1 >= 0:
            if headers[self.get_header(row - 1, col)].texture_container_idx == headers[header_id].texture_container_idx:
                ret.add(self.get_header(row - 1, col))
        if col + 1 < self.x:
            if headers[self.get_header(row, col + 1)].texture_container_idx == headers[header_id].texture_container_idx:
                ret.add(self.get_header(row, col + 1))
        if row + 1 < self.y:
            if headers[self.get_header(row + 1, col)].texture_container_idx == headers[header_id].texture_container_idx:
                ret.add(self.get_header(row + 1, col))
        if col - 1 >= 0:
            if headers[self.get_header(row, col - 1)].texture_container_idx == headers[header_id].texture_container_idx:
                ret.add(self.get_header(row, col - 1))

        return ret


class Overworlds:  # This is equivalent to a gen 4 events file
    def __init__(self, buffer):
        self.file_size = buffer.read_u32()
        self.npcs = []
        self.warps = []
        if self.file_size == 0:
            return
        self.interactable_count = buffer.read_u8()
        self.npc_count = buffer.read_u8()
        self.warp_count = buffer.read_u8()
        self.trigger_count = buffer.read_u8()

        self.interactables = buffer.read_bytes(self.interactable_count * 0x14)  # 20 bytes per interactable

        self.npcs_offset = buffer.pos
        for x in range(self.npc_count):
            self.npcs.append(NPC(buffer, x))

        self.warps_offset = buffer.pos
        for x in range(self.warp_count):
            self.warps.append(Warp(buffer, x))

        self.remainder = buffer.read_bytes(len(buffer.data) - buffer.pos)

    def write(self):
        if self.file_size == 0:
            size = 4
        else:
            size = 8 + len(self.interactables) + (self.warp_count * 0x14) + (self.npc_count * 0x24) + len(
                self.remainder)

        buffer = Buffer(bytearray(size), write=True)

        if self.file_size == 0:
            buffer.write_u32(0)
            return buffer.data

        buffer.write_u32(self.file_size)
        buffer.write_u8(self.interactable_count)
        buffer.write_u8(self.npc_count)
        buffer.write_u8(self.warp_count)
        buffer.write_u8(self.trigger_count)
        buffer.write_bytes(self.interactables)

        for npc in self.npcs:
            buffer.write_bytes(npc.write())

        for warp in self.warps:
            buffer.write_bytes(warp.write())

        buffer.write_bytes(self.remainder)

        return buffer.data

    def __str__(self):
        if len(self.warps) > 0:
            ret = '--------'
            for warp in self.warps:
                ret += '\n(' + str(warp.global_x_pos) + ',' + str(warp.global_y_pos) + ') to h' + str(
                    warp.dest_header) + \
                       ':w' + str(warp.dest_warp_id)
            return ret
        else:
            return ''


class Warp(dict):
    def __init__(self, buffer, warp_id):
        self.dest_header = buffer.read_u16()
        self.dest_warp_id = buffer.read_u16()
        self.contact_direction = buffer.read_u8()
        self.transition_type = buffer.read_u8()
        self.coordinate_type = buffer.read_u16()

        self.global_x_pos = buffer.read_u16()
        self.local_x_pos = int(self.global_x_pos / 16) % 32
        self.map_x_pos = int(int(self.global_x_pos / 16) / 32)

        self.global_z_pos = buffer.read_u16()

        self.global_y_pos = buffer.read_u16()
        self.local_y_pos = int(self.global_y_pos / 16) % 32
        self.map_y_pos = int(int(self.global_y_pos / 16) / 32)

        self.width = buffer.read_u16()
        self.height = buffer.read_u16()
        self.is_rail = buffer.read_u16()

        self.id = warp_id
        super().__init__(x_pos=self.local_x_pos, y_pos=self.local_y_pos, map_x=self.map_x_pos, map_y=self.map_y_pos,
                         global_z=self.global_z_pos, dest_header=self.dest_header, dest_warp_id=self.dest_warp_id,
                         id=self.id)

    def write(self):
        size = 0x14
        buffer = Buffer(bytearray(size), write=True)

        buffer.write_u16(self.dest_header)
        buffer.write_u16(self.dest_warp_id)
        buffer.write_u8(self.contact_direction)
        buffer.write_u8(self.transition_type)
        buffer.write_u16(self.coordinate_type)
        buffer.write_u16(self.global_x_pos)
        buffer.write_u16(self.global_z_pos)
        buffer.write_u16(self.global_y_pos)
        buffer.write_u16(self.width)
        buffer.write_u16(self.height)
        buffer.write_u16(self.is_rail)

        return buffer.data

    def __repr__(self):
        return 'w' + str(self.id) + ':(' + str(self.local_x_pos) + ',' + str(self.local_y_pos) + ')->h' + str(
            self.dest_header) + ':w' + \
               str(self.dest_warp_id)


class NPC:
    def __init__(self, buffer, id):
        self.ow_id = buffer.read_u16()
        self.overlay_table_entry = buffer.read_u16()
        self.movement = buffer.read_u16()
        self.type = buffer.read_u16()
        self.flag = buffer.read_u16()
        self.script = buffer.read_u16()
        self.orientation = buffer.read_u16()
        self.sight_range = buffer.read_u16()
        self.unknown1 = buffer.read_u16()
        self.unknown2 = buffer.read_u16()
        self.x_range = buffer.read_u16()
        self.y_range = buffer.read_u16()

        self.global_x_pos = buffer.read_u16()
        self.local_x_pos = (self.global_x_pos % 32) & 0xffff
        self.map_x_pos = int(self.global_x_pos / 32) & 0xffff

        self.global_y_pos = buffer.read_u16()
        self.local_y_pos = (self.global_y_pos % 32) & 0xffff
        self.map_y_pos = int(self.global_y_pos / 32) & 0xffff

        self.other_x = buffer.read_u16()
        self.other_y = buffer.read_u16()

        self.unknown3 = buffer.read_u16()
        self.z_pos = buffer.read_u16()

        self.id = id

    def write(self):
        size = 36
        buffer = Buffer(bytearray(size), write=True)
        buffer.write_u16(self.ow_id)
        buffer.write_u16(self.overlay_table_entry)
        buffer.write_u16(self.movement)
        buffer.write_u16(self.type)
        buffer.write_u16(self.flag)
        buffer.write_u16(self.script)
        buffer.write_u16(self.orientation)
        buffer.write_u16(self.sight_range)
        buffer.write_u16(self.unknown1)
        buffer.write_u16(self.unknown2)
        buffer.write_u16(self.x_range)
        buffer.write_u16(self.y_range)
        buffer.write_u16(self.global_x_pos)
        buffer.write_u16(self.global_y_pos)
        buffer.write_u16(self.other_x)
        buffer.write_u16(self.other_y)
        buffer.write_u16(self.unknown3)
        buffer.write_u16(self.z_pos)

        return buffer.data


class Map:
    """NG means no grid"""
    """WB means one collision file"""
    """RD also means one collision file, but slightly different structure(?) possibly for hybrid rail/grid maps"""
    """GC means two collision files (Trifindo thinks it is two concatenated WB files)"""

    def __init__(self, buffer, id):
        self.magic = buffer.read_u16()
        self.num_sections = buffer.read_u16()
        self.model_offset = buffer.read_u32()
        self.perms_offset = 0
        self.perms_2_offset = 0
        self.building_pos_offset = 0
        self.file_size = 0

        self.id = id

        if self.magic == 0x474E:  # Ng
            pass
        elif self.magic == 0x4452 or self.magic == 0x4257:  # Rd, Wb
            self.perms_offset = buffer.read_u32()
        elif self.magic == 0x4347:  # Gc
            self.perms_offset = buffer.read_u32()
            self.perms_2_offset = buffer.read_u32()
        else:
            print('ERROR: Invalid magic')

        self.building_pos_offset = buffer.read_u32()
        self.file_size = buffer.read_u32()

        if self.magic == 0x474E:  # Ng
            self.model = buffer.read_bytes(self.building_pos_offset - self.model_offset)
            self.building_positions = buffer.read_bytes(self.file_size - self.building_pos_offset)
        elif self.magic == 0x4452 or self.magic == 0x4257:  # Rd, Wb
            self.model = buffer.read_bytes(self.perms_offset - self.model_offset)
            self.permissions = PermsFile(Buffer(bytearray(buffer.read_bytes(self.building_pos_offset - self.perms_offset))))
            self.building_positions = buffer.read_bytes(self.file_size - self.building_pos_offset)
        elif self.magic == 0x4347:  # Gc
            self.model = buffer.read_bytes(self.perms_offset - self.model_offset)
            self.permissions = PermsFile(Buffer(bytearray(buffer.read_bytes(self.perms_2_offset - self.perms_offset))))
            self.permissions_2 = PermsFile(Buffer(bytearray(buffer.read_bytes(self.building_pos_offset - self.perms_2_offset))))
            self.building_positions = buffer.read_bytes(self.file_size - self.building_pos_offset)
        else:
            print('ERROR: Invalid number of sections')

        self.remainder = buffer.read_bytes(len(buffer.data) - buffer.pos)

    def write(self):
        size = 16 + len(self.remainder)
        if self.magic == 0x474E:  # Ng
            pass
        elif self.magic == 0x4452 or self.magic == 0x4257:  # Rd, Wb
            size += self.permissions.get_size()
        elif self.magic == 0x4347:  # Gc
            size += self.permissions.get_size() + self.permissions_2.get_size()
        else:
            print('ERROR: Invalid magic')

        buffer = Buffer(bytearray(size), write=True)
        buffer.write_u16(self.magic)
        buffer.write_u16(self.num_sections)
        buffer.write_u32(self.model_offset)

        if self.magic == 0x474E:  # Ng
            pass
        elif self.magic == 0x4452 or self.magic == 0x4257:  # Rd, Wb
            buffer.write_u32(self.perms_offset)
        elif self.magic == 0x4347:  # Gc
            buffer.write_u32(self.perms_offset)
            buffer.write_u32(self.perms_2_offset)
        else:
            print('ERROR: Invalid magic')

        buffer.write_u32(self.building_pos_offset)
        buffer.write_u32(self.file_size)

        if self.magic == 0x474E:  # Ng
            buffer.write_bytes(self.model)
            buffer.write_bytes(self.building_positions)
        elif self.magic == 0x4452 or self.magic == 0x4257:  # Rd, Wb
            buffer.write_bytes(self.model)
            buffer.write_bytes(self.permissions.write())
            buffer.write_bytes(self.building_positions)
        elif self.magic == 0x4347:  # Gc
            buffer.write_bytes(self.model)
            buffer.write_bytes(self.permissions.write())
            buffer.write_bytes(self.permissions_2.write())
            buffer.write_bytes(self.building_positions)
        else:
            print('ERROR: Invalid number of sections')

    def get_name(self):
        buffer = Buffer(bytearray(self.model))
        buffer.seek_local(0x34)
        name = list(buffer.read_bytes(16))
        name = list(filter((0).__ne__, name))

        return bytearray(name).decode('utf-8')


class PermsFile:
    def __init__(self, buffer):
        self.height = buffer.read_u16()
        self.width = buffer.read_u16()
        self.layers = []
        for num in range(5):
            self.layers.append(PermsTable(self.height, self.width, num))

        for row in range(self.height):
            for col in range(self.width):
                self.layers[0].add(buffer.read_u16())
                self.layers[1].add(buffer.read_u16())
                self.layers[2].add(buffer.read_u16())
                self.layers[3].add(buffer.read_u8())
                self.layers[4].add(buffer.read_u8())

        self.remainder = buffer.read_bytes(len(buffer.data)-buffer.pos)

    def get_size(self):  # height + width + 8 * num_rows * num_cols + remainder
        return 4 + 8*self.height*self.width + len(self.remainder)

    def write(self):
        size = self.get_size()
        buffer = Buffer(bytearray(size), write=True)
        buffer.write_u16(self.height)
        buffer.write_u16(self.width)

        for row in range(self.height):
            for col in range(self.width):
                buffer.write_u16(self.layers[0].get(row, col))
                buffer.write_u16(self.layers[1].get(row, col))
                buffer.write_u16(self.layers[2].get(row, col))
                buffer.write_u8(self.layers[3].get(row, col))
                buffer.write_u8(self.layers[4].get(row, col))

        buffer.write_bytes(self.remainder)

        return buffer.data


class PermsTable:
    def __init__(self, height, width, id):
        self.table = []
        self.table.append([])
        self.height = height
        self.width = width
        self.row_num = 0
        self.col_num = 0
        self.id = id

    def add(self, value):
        if self.row_num != self.height:
            if self.col_num == self.width:
                self.table.append([])
                self.row_num += 1
                self.col_num = 0

            self.table[self.row_num].append(value)
            self.col_num += 1
        else:
            print('Error in perms table initialization: attempted to add extraneous value beyond boundary')

    def get(self, row, col):
        return self.table[row][col]

    def print(self):
        for row in self.table:
            for cell in row:
                print(self.format_hex(cell), end=',')
            print()

    def format_hex(self, num):
        val = hex(num)[2:]
        while len(val) != 2:
            val = '0' + val
        if val != '00':
            if self.id == 2:
                if num == 1:
                    val = '\u001b[31m' + val + '\u001b[0m'
                elif num == 3:
                    val = '\u001b[33m' + val + '\u001b[0m'
                elif num == 6:
                    val = '\u001b[32m' + val + '\u001b[0m'
                elif num == 0x3f:
                    val = '\u001b[36m' + val + '\u001b[0m'
            elif self.id == 3:
                if num == 0x81:
                    val = '\u001b[31m' + val + '\u001b[0m'
                elif num == 0x80:
                    val = '\u001b[33m' + val + '\u001b[0m'
                elif num == 0x24:
                    val = '\u001b[32m' + val + '\u001b[0m'
                elif num == 0x16:
                    val = '\u001b[36m' + val + '\u001b[0m'
        return val
