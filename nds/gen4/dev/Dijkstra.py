"""
Dijkstra.py

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
from tkinter import ttk, Canvas

from ttkthemes import ThemedTk


class Dijkstra:

    def __init__(self, vertices, graph):
        self.vertices = vertices  # ("A", "B", "C" ...)
        self.graph = graph  # {"A": {"B": 1}, "B": {"A": 3, "C": 5} ...}

    def find_route(self, start, end):
        unvisited = {n: float("inf") for n in self.vertices}
        unvisited[start] = 0  # set start vertex to 0
        visited = {}  # list of all visited nodes
        parents = {}  # predecessors
        while unvisited:
            min_vertex = min(unvisited, key=unvisited.get)  # get smallest distance
            for neighbour, _ in self.graph.get(min_vertex, {}).items():
                if neighbour in visited:
                    continue
                new_distance = unvisited[min_vertex] + self.graph[min_vertex].get(neighbour, float("inf"))
                if new_distance < unvisited[neighbour]:
                    unvisited[neighbour] = new_distance
                    parents[neighbour] = min_vertex
            visited[min_vertex] = unvisited[min_vertex]
            unvisited.pop(min_vertex)
            if min_vertex == end:
                break
        return parents, visited

    @staticmethod
    def generate_path(parents, start, end):
        path = [end]
        while True:
            try:
                key = parents[path[0]]
            except KeyError:
                return None
            path.insert(0, key)
            if key == start:
                break
        return path

#
# input_vertices = ("A", "B", "C", "D", "E", "F", "G")
# input_graph = {
#     "A": {"B": 5, "D": 3, "E": 12, "F": 5, "H": 1},
#     "B": {"A": 5, "D": 1, "G": 2},
#     "C": {"E": 1, "F": 16, "G": 2},
#     "D": {"A": 3, "B": 1, "E": 1, "G": 1},
#     "E": {"A": 12, "C": 1, "D": 1, "F": 2},
#     "F": {"A": 5, "C": 16, "E": 2},
#     "G": {"B": 2, "C": 2, "D": 1},
#     "H": {}
# }
# start_vertex = "B"
# end_vertex = "C"
# dijkstra = Dijkstra(input_vertices, input_graph)
# p, v = dijkstra.find_route(start_vertex, end_vertex)
# print("Distance from %s to %s is: %.2f" % (start_vertex, end_vertex, v[end_vertex]))
# se = dijkstra.generate_path(p, start_vertex, end_vertex)
# print("Path from %s to %s is: %s" % (start_vertex, end_vertex, " -> ".join(se)))
