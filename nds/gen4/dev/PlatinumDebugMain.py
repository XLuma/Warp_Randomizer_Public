"""
PlatinumDebugMain.py


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
from nds.gen4.PlatinumWarpRandomizer import PlatinumRandomizerFunctions
from nds.tableLocator import TableLocator
import ndspy.rom

# rom = ndspy.rom.NintendoDSRom.fromFile('Platinum.nds')
# locator = TableLocator(rom)
# locator.get_table('mapHeaders')
random = PlatinumRandomizerFunctions()
random.load_map_data()




