"""
formats.py

Classes to represent data found in NDS games

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


class PlatinumHeader:
    def __init__(self, buffer, id):
        self.area_data_id = buffer.read_u8()
        self.unknown1 = buffer.read_u8()
        self.matrix_id = buffer.read_u16()
        self.script_id = buffer.read_u16()
        self.level_script_id = buffer.read_u16()
        self.text_id = buffer.read_u16()
        self.music_day_id = buffer.read_u16()
        self.music_night_id = buffer.read_u16()
        self.wild_id = buffer.read_u16()
        self.event_id = buffer.read_u16()
        self.location_name = buffer.read_u8()
        self.area_icon = buffer.read_u8()
        self.weather_id = buffer.read_u8()
        self.camera_id = buffer.read_u8()
        self.map_settings = buffer.read_u16()
        self.id = id

    def write(self):
        size = 0x18
        buffer = Buffer(bytearray(size), write=True)

        buffer.write_u8(self.area_data_id)
        buffer.write_u8(self.unknown1)
        buffer.write_u16(self.matrix_id)
        buffer.write_u16(self.script_id)
        buffer.write_u16(self.level_script_id)
        buffer.write_u16(self.text_id)
        buffer.write_u16(self.music_day_id)
        buffer.write_u16(self.music_night_id)
        buffer.write_u16(self.wild_id)
        buffer.write_u16(self.event_id)
        buffer.write_u8(self.location_name)
        buffer.write_u8(self.area_icon)
        buffer.write_u8(self.weather_id)
        buffer.write_u8(self.camera_id)
        buffer.write_u16(self.map_settings)

        return buffer.data

    def set_teleport_flag(self):
        location_specifier = self.map_settings & 0b1111111
        battle_background = (self.map_settings >> 7) & 0b11111
        flags = (self.map_settings >> 12) & 0b1111
        flags = (flags | 0b1100) << 12  # enables rope/ dig/ tp flag, shifts bits back by 12
        battle_background = (battle_background << 7)
        self.map_settings = flags | battle_background | location_specifier

    def __str__(self):
        return str(self.id) + ":" + \
               "\narea data: " + str(self.area_data_id) + \
               "\nunknown1: " + str(self.unknown1) + \
               "\nmatrix: " + str(self.matrix_id) + \
               "\nscript: " + str(self.script_id) + \
               "\nlevel script: " + str(self.level_script_id) + \
               "\ntext: " + str(self.text_id) + \
               "\nmusic_day: " + str(self.music_day_id) + \
               "\nmusic_night: " + str(self.music_night_id) + \
               "\nwild: " + str(self.wild_id) + \
               "\nevents: " + str(self.event_id) + \
               "\nname: " + str(self.location_name) + \
               "\narea_icon: " + str(self.area_icon) + \
               "\nweather: " + str(self.weather_id) + \
               "\ncamera: " + str(self.camera_id) + \
               "\nsettings: " + bin(self.map_settings)[2:6] + ' ' + bin(self.map_settings)[6:11] + \
               ' ' + bin(self.map_settings)[11:] + "\n"


class JohtoHeader:
    def __init__(self, buffer, id):
        self.wild_id = buffer.read_u8()
        self.area_data_id = buffer.read_u8()
        self.unknown1 = buffer.read_u8()
        self.unknown2 = buffer.read_u8()
        self.matrix_id = buffer.read_u16()
        self.script_id = buffer.read_u16()
        self.level_script_id = buffer.read_u16()
        self.text_id = buffer.read_u16()
        self.music_day_id = buffer.read_u16()
        self.music_night_id = buffer.read_u16()
        self.event_id = buffer.read_u16()
        self.location_name = buffer.read_u8()
        self.area_properties = buffer.read_u8()
        self.map_settings = buffer.read_u32()
        self.id = id

    def write(self):
        size = 0x18
        buffer = Buffer(bytearray(size), write=True)
        buffer.write_u8(self.wild_id)
        buffer.write_u8(self.area_data_id)
        buffer.write_u8(self.unknown1)
        buffer.write_u8(self.unknown2)
        buffer.write_u16(self.matrix_id)
        buffer.write_u16(self.script_id)
        buffer.write_u16(self.level_script_id)
        buffer.write_u16(self.text_id)
        buffer.write_u16(self.music_day_id)
        buffer.write_u16(self.music_night_id)
        buffer.write_u16(self.event_id)
        buffer.write_u8(self.location_name)
        buffer.write_u8(self.area_properties)
        buffer.write_u32(self.map_settings)

        return buffer.data

    def set_teleport_flag(self):
        other = self.map_settings & 0x1000000
        flags = (self.map_settings >> 25) & 0b1111111
        flags = (flags | 0b00011000) << 25  # enables rope/ dig/ tp flag, shifts bits back by 25
        self.map_settings = flags | other

    def __str__(self):
        return str(self.id) + ":" + \
               "\nwild: " + str(self.wild_id) + \
               "\narea data: " + str(self.area_data_id) + \
               "\nunknown1: " + str(self.unknown1) + \
               "\nunknown2: " + str(self.unknown2) + \
               "\nmatrix: " + str(self.matrix_id) + \
               "\nscript: " + str(self.script_id) + \
               "\nlevel script: " + str(self.level_script_id) + \
               "\ntext: " + str(self.text_id) + \
               "\nmusic_day: " + str(self.music_day_id) + \
               "\nmusic_night: " + str(self.music_night_id) + \
               "\nevents: " + str(self.event_id) + \
               "\nname: " + str(self.location_name) + \
               "\narea_properties: " + str(self.area_properties) + \
               "\nsettings: " + bin(self.map_settings)


class Matrix:
    def __init__(self, buffer):
        self.x = buffer.read_u8()
        self.y = buffer.read_u8()
        self.headers_flag = buffer.read_u8() == 1
        self.border_heights_flag = buffer.read_u8() == 1
        self.name_length = buffer.read_u8()
        self.name = buffer.read_bytes(self.name_length)
        self.headers = []
        self.heights = []
        self.maps = []
        if self.headers_flag:
            for row in range(self.y):
                entry = []
                for col in range(self.x):
                    entry.append(buffer.read_u16())
                self.headers.append(entry)

        if self.border_heights_flag:
            for row in range(self.y):
                entry = []
                for col in range(self.x):
                    entry.append(buffer.read_u8())
                self.heights.append(entry)

        for row in range(self.y):
            entry = []
            for col in range(self.x):
                entry.append(buffer.read_u16())
            self.maps.append(entry)

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
        size = 5 + self.name_length + self.y*self.x*2
        if self.headers:
            size += self.y*self.x*2
        if self.heights:
            size += self.y * self.x
        buffer = Buffer(bytearray(size), write=True)

        buffer.write_u8(self.x)
        buffer.write_u8(self.y)
        buffer.write_u8(0x1) if self.headers_flag else buffer.write_u8(0x0)
        buffer.write_u8(0x1) if self.border_heights_flag else buffer.write_u8(0x0)
        buffer.write_u8(self.name_length)
        buffer.write_bytes(self.name)
        if self.headers_flag:
            for row in range(self.y):
                for col in range(self.x):
                    buffer.write_u16(self.headers[row][col])

        if self.border_heights_flag:
            for row in range(self.y):
                for col in range(self.x):
                    buffer.write_u8(self.heights[row][col])

        for row in range(self.y):
            for col in range(self.x):
                buffer.write_u16(self.maps[row][col])

        return buffer.data

    def get_connected_maps(self, row, col, headers, header_id):
        ret = []
        name_prefix = 'm' + str(headers[header_id].matrix_id) + ':ad' + str(headers[header_id].area_data_id) + ':h'
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
                if headers[self.get_header(row - 1, col)].area_data_id == headers[header_id].area_data_id:
                    ret.append(name_prefix + str(self.get_header(row - 1, col)) + ':x' + str(col) + ':y' + str(row - 1))
            if col + 1 < self.x:
                if headers[self.get_header(row, col + 1)].area_data_id == headers[header_id].area_data_id:
                    ret.append(name_prefix + str(self.get_header(row, col + 1)) + ':x' + str(col + 1) + ':y' + str(row))
            if row + 1 < self.y:
                if headers[self.get_header(row + 1, col)].area_data_id == headers[header_id].area_data_id:
                    ret.append(name_prefix + str(self.get_header(row + 1, col)) + ':x' + str(col) + ':y' + str(row + 1))
            if col - 1 >= 0:
                if headers[self.get_header(row, col - 1)].area_data_id == headers[header_id].area_data_id:
                    ret.append(name_prefix + str(self.get_header(row, col - 1)) + ':x' + str(col - 1) + ':y' + str(row))

        return ret

    def get_connected_headers(self, row, col, headers, header_id):
        ret = set()

        if row - 1 >= 0:
            if headers[self.get_header(row - 1, col)].area_data_id == headers[header_id].area_data_id:
                ret.add(self.get_header(row - 1, col))
        if col + 1 < self.x:
            if headers[self.get_header(row, col + 1)].area_data_id == headers[header_id].area_data_id:
                ret.add(self.get_header(row, col + 1))
        if row + 1 < self.y:
            if headers[self.get_header(row + 1, col)].area_data_id == headers[header_id].area_data_id:
                ret.add(self.get_header(row + 1, col))
        if col - 1 >= 0:
            if headers[self.get_header(row, col - 1)].area_data_id == headers[header_id].area_data_id:
                ret.add(self.get_header(row, col - 1))

        return ret


class Events:
    def __init__(self, buffer):
        self.spawnable_count = buffer.read_u32()
        self.spawnables = buffer.read_bytes(self.spawnable_count * 0x14)  # 20 bytes per spawnable

        self.overworld_count = buffer.read_u32()
        self.overworlds_offset = buffer.pos
        self.overworlds = []
        for x in range(self.overworld_count):
            self.overworlds.append(Overworld(buffer, x))

        self.warp_count = buffer.read_u32()
        self.warps_offset = buffer.pos
        self.warps = []
        for x in range(self.warp_count):
            self.warps.append(Warp(buffer, x))

        self.trigger_count = buffer.read_u32()
        self.triggers = buffer.read_bytes(self.trigger_count * 0x10)  # 16 bytes per trigger

    def write(self):
        size = 16 + len(self.spawnables) + self.warp_count * 0xC + self.overworld_count * 0x20 + len(self.triggers)
        buffer = Buffer(bytearray(size), write=True)

        buffer.write_u32(self.spawnable_count)
        buffer.write_bytes(self.spawnables)

        buffer.write_u32(self.overworld_count)
        for overworld in self.overworlds:
            buffer.write_bytes(overworld.write())

        buffer.write_u32(self.warp_count)
        for warp in self.warps:
            buffer.write_bytes(warp.write())

        buffer.write_u32(self.trigger_count)
        buffer.write_bytes(self.triggers)

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
        self.global_x_pos = buffer.read_u16()
        self.local_x_pos = (self.global_x_pos % 32) & 0xffff
        self.map_x_pos = int(self.global_x_pos / 32) & 0xffff

        self.global_y_pos = buffer.read_u16()
        self.local_y_pos = (self.global_y_pos % 32) & 0xffff
        self.map_y_pos = int(self.global_y_pos / 32) & 0xffff

        self.dest_header = buffer.read_u16()
        self.dest_warp_id = buffer.read_u16()
        self.height = buffer.read_u32()

        self.id = warp_id
        super().__init__(x_pos=self.local_x_pos, y_pos=self.local_y_pos, map_x=self.map_x_pos, map_y=self.map_y_pos,
                         dest_header=self.dest_header, dest_warp_id=self.dest_warp_id, id=self.id)

    def write(self):
        size = 0xC
        buffer = Buffer(bytearray(size), write=True)

        buffer.write_u16(self.global_x_pos)
        buffer.write_u16(self.global_y_pos)
        buffer.write_u16(self.dest_header)
        buffer.write_u16(self.dest_warp_id)
        buffer.write_u32(self.height)

        return buffer.data

    def __repr__(self):
        return 'w' + str(self.id) + ':(' + str(self.local_x_pos) + ',' + str(self.local_y_pos) + ')->h' + str(
            self.dest_header) + ':w' + \
               str(self.dest_warp_id)


class Overworld:
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

        self.z_pos = buffer.read_u16()
        self.unknown3 = buffer.read_u16()

        self.id = id

    def write(self):
        size = 0x20
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
        buffer.write_u16(self.z_pos)
        buffer.write_u16(self.unknown3)

        return buffer.data


class Map:
    def __init__(self, buffer, id, name, hgss=False):
        self.hgss = hgss
        self.perms_size = buffer.read_u32()
        self.other_sizes = buffer.read_bytes(0xc)
        if hgss:
            self.signature = buffer.read_u16()
            self.sound_length = buffer.read_u16()
            self.sound_section = buffer.read_bytes(self.sound_length)
        self.permissions = []
        self.collisions = []

        for row in range(32):
            self.permissions.append([])
            self.collisions.append([])
            for col in range(32):
                self.permissions[row].append(buffer.read_u8())
                self.collisions[row].append(buffer.read_u8())

        self.remainder = buffer.read_bytes(len(buffer.data)-buffer.pos)

        self.id = id
        self.name = name
        self.original_size = len(buffer.data)

    def write(self):
        buffer = Buffer(bytearray(self.original_size), write=True)
        buffer.write_u32(self.perms_size)
        buffer.write_bytes(self.other_sizes)
        if self.hgss:
            buffer.write_u16(self.signature)
            buffer.write_u16(self.sound_length)
            buffer.write_bytes(self.sound_section)
        for row in range(32):
            for col in range(32):
                buffer.write_u8(self.permissions[row][col])
                buffer.write_u8(self.collisions[row][col])
        buffer.write_bytes(self.remainder)
        return buffer.data

    def get_permissions(self, row, col):
        return self.permissions[row][col]

    def get_collisions(self, row, col):
        return self.collisions[row][col]

    def __str__(self):
        return "Map_ID_%i" % self.id
