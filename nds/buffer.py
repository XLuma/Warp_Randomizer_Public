"""
buffer.py

Generic buffer class

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
class Buffer:
    def __init__(self, data, write=False):
        self.data = data
        self.pos = 0
        self.write = write

    def read_u8(self):
        if self.pos <= len(self.data):
            ret = self.data[self.pos] & 0xff
            self.pos += 1
            return ret
        else:
            raise Exception('Past end of bytearray')

    def read_u16(self):
        if self.pos + 2 <= len(self.data):
            u8_1 = self.read_u8()
            u8_2 = self.read_u8() << 8
            ret = u8_2 | u8_1
            # Don't need to increment self.pos because it is handled by read_u8()
            return ret
        else:
            print(self.data[self.pos:])
            raise Exception('Past end of bytearray: position ' + str(self.pos) + ' out of ' + str(len(self.data)) +
                            ' on attempted read of 2')

    def read_u32(self):
        if self.pos + 4 <= len(self.data):
            u16_1 = self.read_u16()
            u16_2 = self.read_u16() << 16
            ret = u16_2 | u16_1
            # Don't need to increment self.pos because it is handled by read_u16()
            return ret
        else:
            print(self.data[self.pos:])
            raise Exception('Past end of bytearray: position ' + str(self.pos) + ' out of ' + str(len(self.data)) +
                            ' on attempted read of 4')

    def read_u64(self):
        if self.pos + 8 <= len(self.data):
            u32_1 = self.read_u32()
            u32_2 = self.read_u32() << 32
            ret = u32_2 | u32_1
            # Don't need to increment self.pos because it is handled by read_u32()
            return ret
        else:
            raise Exception('Past end of bytearray')

    def read_s8(self):
        return self.twos_comp(self.read_u8(), 8)

    def read_s16(self):
        return self.twos_comp(self.read_u16(), 16)

    def read_s32(self):
        return self.twos_comp(self.read_u32(), 32)

    def read_s64(self):
        return self.twos_comp(self.read_u64(), 64)

    def read_bytes(self, read_length):
        if self.pos + read_length <= len(self.data):
            ret = self.data[self.pos:self.pos + read_length]
            self.pos += read_length
            return ret
        else:
            raise Exception('Past end of bytearray')

    def seek_local(self, val):
        if self.pos + val < len(self.data):
            self.pos += val
        else:
            raise Exception('Past end of bytearray')

    def seek_global(self, offset):
        if offset < len(self.data):
            self.pos = offset
        else:
            raise Exception('Past end of bytearray')

    def toggle_write(self, state):
        self.write = state

    def write_u8(self, val):
        if self.pos < len(self.data) and self.write:
            self.data[self.pos] = val & 0xff
            self.pos += 1
        elif self.pos >= len(self.data) and self.write:
            raise Exception('Past end of bytearray')
        else:
            raise Exception('Write not enabled')

    def write_u16(self, val):
        if self.pos + 2 <= len(self.data) and self.write:
            u8_1 = val & 0xff
            u8_2 = (val >> 8) & 0xff
            self.write_u8(u8_1)
            self.write_u8(u8_2)
        elif self.pos >= len(self.data) and self.write:
            raise Exception('Past end of bytearray')
        elif self.pos + 2 >= len(self.data) and self.write:
            raise Exception('Write will go past end of bytearray')
        else:
            raise Exception('Write not enabled')

    def write_u32(self, val):
        if self.pos + 4 <= len(self.data) and self.write:
            u16_1 = val & 0xffff
            u16_2 = (val >> 16) & 0xffff
            self.write_u16(u16_1)
            self.write_u16(u16_2)
        elif self.pos >= len(self.data) and self.write:
            raise Exception('Past end of bytearray')
        elif self.pos + 4 >= len(self.data) and self.write:
            raise Exception('Write will go past end of bytearray')
        else:
            raise Exception('Write not enabled')

    def write_u64(self, val):
        if self.pos + 8 <= len(self.data) and self.write:
            u32_1 = val & 0xffffffff
            u32_2 = (val >> 32) & 0xffffffff
            self.write_u16(u32_1)
            self.write_u16(u32_2)
        elif self.pos >= len(self.data) and self.write:
            raise Exception('Past end of bytearray')
        elif self.pos + 8 >= len(self.data) and self.write:
            raise Exception('Write will go past end of bytearray')
        else:
            raise Exception('Write not enabled')

    def write_bytes(self, arr):
        if self.pos <= len(self.data) and self.pos + len(arr) <= len(self.data):
            for x in arr:
                self.write_u8(x)
        elif self.pos >= len(self.data) and self.write:
            raise Exception('Past end of bytearray')
        elif self.pos + len(arr) >= len(self.data) and self.write:
            raise Exception('Write will go past end of bytearray')
        else:
            raise Exception('Write not enabled')

    def __len__(self):
        return len(self.data)

    def twos_comp(self, val, bits):
        """compute the 2's complement of int value val"""
        if (val & (1 << (bits - 1))) != 0:  # if sign bit is set e.g., 8bit: 128-255
            val = val - (1 << bits)  # compute negative value
        return val  # return positive value as is
