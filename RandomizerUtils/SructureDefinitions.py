"""
StructureDefinitions.py

Abstract classes used in the parsing and randomization processes

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
from abc import ABC, abstractmethod


class Warp:
    def __init__(self, x, y, elevation, dest_map, dest_warp_id, warp_id, header_id=-1, dest_header_id=-1, width=1, height=1, no_pair=0):
        if isinstance(x, int) and isinstance(y, int) and isinstance(elevation, int) and isinstance(dest_map, str) \
                and isinstance(dest_warp_id, int) and isinstance(warp_id, int) and isinstance(header_id, int) \
                and isinstance(width, int) and isinstance(height, int) and isinstance(no_pair, int):
            self.x = x
            self.y = y
            self.elevation = elevation
            self.dest_map = dest_map
            self.dest_warp_id = dest_warp_id
            self.warp_id = warp_id
            self.header_id = header_id
            self.dest_header_id = dest_header_id
            self.width = width
            self.height = height
            self.no_pair = (no_pair != 0)
        else:
            raise ValueError("Invalid Warp")

    def __eq__(self, other):
        return isinstance(other, Warp) and self.x == other.x and self.y == other.y and \
               self.elevation == other.elevation and self.dest_map == other.dest_map and \
               self.dest_warp_id == other.dest_warp_id and self.warp_id == other.warp_id \
               and self.header_id == other.header_id


class Connection:
    def __init__(self, direction, offset, map):
        if isinstance(direction, str) and isinstance(offset, int) and isinstance(map, str):
            self.direction = direction
            self.offset = offset
            self.map = map
        else:
            raise ValueError("Invalid Connection")


class MapNode:
    def __init__(self, map):
        self.map = map
        self.connections = []
        self.warps = []
        self.warp_nodes = []
        self.empty_warps = 0
        self.empty_connections = 0

    def add_connection(self, connection):
        self.connections.append(connection)

    def add_warps(self, warp, warp_node):
        self.warps.append(warp)
        self.warp_nodes.append(warp_node)

    def make_empty_warps(self, num_warps):
        for i in range(0, num_warps):
            self.warps.append(None)
            self.warp_nodes.append(None)
        self.empty_warps = num_warps

    def make_empty_connections(self, num_connections):
        for i in range(0, num_connections):
            self.connections.append(None)
        self.empty_connections = num_connections

    def fill_in_warp(self, warp, warp_node, index):
        self.warps[index] = warp
        self.warp_nodes[index] = warp_node
        self.empty_warps = self.empty_warps - 1

    def fill_in_connection(self, connection, index):
        self.connections[index] = connection
        self.empty_connections = self.empty_connections - 1


class GenRandomizerFunctions(ABC):

    # Gen Specific function to load in map data and output a dictionary of following format
    # [unique_map_id] = [List of Warps], [List of Connections]
    @abstractmethod
    def load_map_data(self) -> dict:
        pass

    @abstractmethod
    def define_starting_map_id(self) -> str:
        pass

    @abstractmethod
    def info(self):
        pass

    @abstractmethod
    def determine_unreachable_maps(self, map_nodes: dict, map_warps: dict) -> []:
        pass

    @abstractmethod
    def is_not_needed_map_ok(self, map_name: str) -> bool:
        pass

    @abstractmethod
    def write_rom(self, input_file: str, output_file: str, map_warps: dict):
        pass