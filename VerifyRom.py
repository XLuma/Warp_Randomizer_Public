"""
VerifyRom.py

Verify the integrity of a supported ROM

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
import hashlib
import json
import os
from RandomizerUtils import Utils

from nds.buffer import Buffer

nintendo_logo_md5 = 'e0434707845307679464ae1c22f0ec2d'

with open(Utils.resource_path(os.path.join('Resources', 'verification.json'))) as f:
    verification_json = json.load(f)

with open(Utils.resource_path(os.path.join('Resources', 'games.json'))) as f:
    game_json = json.load(f)


def validate_rom(filepath_input):
    print()
    with open(filepath_input, 'rb') as f:
        data = bytearray(f.read())
    m = hashlib.md5()
    m.update(data)
    hash_value = m.hexdigest()
    print(hash_value)
    buffer = Buffer(data)

    if hash_value in verification_json['hashes']:
        # print(hash_value + ' -> ' + str(game_json[verification_json[hash_value]]))
        print(game_json[verification_json['hashes'][hash_value][0]])
        game_entry = game_json[verification_json['hashes'][hash_value][0]]
        return verification_json['hashes'][hash_value][0], game_entry['gen'], game_entry['system'], \
               game_entry['def_flag'], verification_json['hashes'][hash_value][1]
    else:
        buffer.seek_global(0x4)
        m = hashlib.md5()
        m.update(buffer.read_bytes(156))
        gba_logo_hash = m.hexdigest()

        buffer.seek_global(0xC0)
        m = hashlib.md5()
        m.update(buffer.read_bytes(156))
        nds_logo_hash = m.hexdigest()

        if gba_logo_hash == nintendo_logo_md5:  # if this is a gba rom
            return validate_unknown_gba(buffer)
        elif nds_logo_hash == nintendo_logo_md5:  # if this is an nds rom
            return validate_unknown_nds(buffer)
    return None


def validate_unknown_gba(buffer):
    return validate_unknown_generic(buffer, 0xA0)


def validate_unknown_nds(buffer):
    return validate_unknown_generic(buffer, 0x00)


def validate_unknown_generic(buffer, offset):
    buffer.seek_global(offset)
    title = buffer.read_bytes(12)
    if 0x00 in title:
        title = title[0:title.index(0x00)]
    title = title.decode()
    code = buffer.read_bytes(4).decode()
    if code in verification_json['game_codes']:
        print(game_json[verification_json['game_codes'][code]])
        game_entry = game_json[verification_json['game_codes'][code]]
        return verification_json['game_codes'][code], game_entry['gen'], game_entry['system'], game_entry['def_flag'], \
               identify_revision(buffer, game_entry['system'])
    elif title in verification_json['titles']:
        print(game_json[verification_json['titles'][title]])
        game_entry = game_json[verification_json['titles'][title]]
        return verification_json['names'][title], game_entry['gen'], game_entry['system'], game_entry['def_flag'], \
               identify_revision(buffer, game_entry['system'])


def identify_revision(buffer, system):
    if system == 'gba':
        buffer.seek_global(0xBC)
        return buffer.read_u8()
    elif system == 'nds':
        buffer.seek_global(0x1E)
        return buffer.read_u8()
