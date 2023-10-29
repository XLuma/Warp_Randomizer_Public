"""
tableLocator.py

Generic class to locate data tables inside NDS ROMS

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
import ndspy.rom
import ndspy.narc
import ndspy.codeCompression
from activejson import FrozenJSON
from nds.buffer import Buffer
from nds.gen4.dev.johtoReadWriteHandler import JohtoReadWriteHandler
from nds.gen4.formats import PlatinumHeader, JohtoHeader
from nds.gen4 import pointers


class TableLocator:

    def __init__(self, rom):
        self.rom = rom
        self.frozen_json = FrozenJSON(pointers.json)
        found = False
        for entry in self.frozen_json.game:
            if entry.code == self.rom.idCode.decode():
                self.game_entry = entry
                found = True
                # print('--' + entry.code + '--')
        if not found:
            sys.exit("Invalid ROM Supplied")

    def locate(self, table_name, arm9):
        global table
        headers = []
        overlays = self.rom.loadArm9Overlays()
        for x in self.game_entry.tables:
            if x.name == table_name:
                table = x

        pointer_offset = int(table.pointerOffset[2:], base=16)
        arm9.seek_global(pointer_offset)
        # this is because the arm9 starts at 0x02000000 in RAM. Subtracting this value will give the physical offset
        table_offset = arm9.read_u32() - 0x02000000
        # print(hex(table_offset))
        arm9.seek_global(table_offset)

    def get_table(self, table_name):
        arm9 = Buffer(bytearray(ndspy.codeCompression.decompress(self.rom.arm9)))
        headers = []
        self.locate(table_name, arm9)
        if self.rom.idCode.decode()[0:3] == "CPU":
            header_count = int(len(
                self.rom.getFileByName('/fielddata/maptable/mapname.bin')) / 0x10)  # 16 bytes per header entry
            for x in range(header_count):
                headers.append(PlatinumHeader(arm9, x))
        elif self.rom.idCode.decode()[0:3] == "IPK" or self.rom.idCode.decode()[0:3] == "IPG":
            header_count = int(len(
                self.rom.getFileByName('/fielddata/maptable/mapname.bin')) / 0x10)  # 16 bytes per header entry
            for x in range(header_count):
                headers.append(JohtoHeader(arm9, x))

        # PlatinumReadWriteHandler().build_lists(self.rom, headers)
        # JohtoReadWriteHandler().build_lists(self.rom, headers)

        return headers

    def replace_table(self, table_name, headers):
        arm9 = Buffer(bytearray(ndspy.codeCompression.decompress(self.rom.arm9)))
        self.locate(table_name, arm9)
        if self.rom.idCode.decode()[0:3] == "CPU":
            arm9.toggle_write(True)
            for header in headers:
                arm9.write_bytes(header.write())
        elif self.rom.idCode.decode()[0:3] == "IPK" or self.rom.idCode.decode()[0:3] == "IPG":
            arm9.toggle_write(True)
            for header in headers:
                arm9.write_bytes(header.write())

        return arm9.data
