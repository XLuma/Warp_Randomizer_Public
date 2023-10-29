"""
Definitions.py

Global definitions for game

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
# Rom Type Flag Definitions
GEN3_EMERALD = 0
GEN4_PLATINUM = 1
GEN4_HEARTGOLD = 2
GEN4_SOULSILVER = 3
GEN3_FIRERED = 4
GEN3_LEAFGREEN = 5
GEN3_RUBY = 6
GEN3_SAPPHIRE = 7
GEN5_WHITE2 = 8
GEN5_BLACK2 = 9

FLAGS = [GEN3_EMERALD, GEN4_PLATINUM, GEN4_HEARTGOLD, GEN4_SOULSILVER, GEN3_FIRERED, GEN3_LEAFGREEN, GEN3_RUBY,
         GEN3_SAPPHIRE, GEN5_WHITE2, GEN5_BLACK2]


def get_definition(value):
    return FLAGS[value]
