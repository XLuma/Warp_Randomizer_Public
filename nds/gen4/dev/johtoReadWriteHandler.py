"""
JohtoReadWriteHandler.py

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
import ndspy.rom
import ndspy.narc

from nds.gen4.dev import JohtoFileDataGenerator
from nds.gen4.formats import *
from nds.buffer import Buffer


class JohtoReadWriteHandler:

    def __init__(self):
        # these color names aren't accurate anymore and I'm too lazy to change them
        black = '\u001b[38;5;0m{'
        red = '\u001b[38;5;1m{'
        green = '\u001b[38;5;184m{'
        yellow = '\u001b[38;5;208m{'
        blue = '\u001b[38;5;138m{'
        magenta = '\u001b[38;5;5m{'
        cyan = '\u001b[38;5;6m{'
        white = '\u001b[38;5;7m{'
        self.reset = '}\u001b[0m'

        b_red = '\u001b[38;5;18m{'
        b_green = '\u001b[38;5;144m{'
        b_yellow = '\u001b[38;5;10m{'
        b_blue = '\u001b[38;5;11m{'
        b_magenta = '\u001b[38;5;12m{'
        b_cyan = '\u001b[38;5;13m{'
        b_white = '\u001b[38;5;14m{'

        self.colors = [black, red, green, yellow, blue, magenta, cyan, white, b_red, b_green, b_yellow, b_blue,
                       b_magenta, b_cyan, b_white]

        # headers whose warps shouldn't be randomized
        self.blacklisted_headers = []

    def build_lists(self, rom, headers):
        matrix_narc = ndspy.narc.NARC(rom.getFileByName('/a/0/4/1'))
        events_narc = ndspy.narc.NARC(rom.getFileByName('/a/0/3/2'))

        # # This GUI is a test/ proof of concept for having all of m0's warps displayed at once
        # root = Tk()
        # root.geometry('1920x1920')
        # canvas = Canvas(root, height=1920, width=1920)

        matrix_0 = Matrix(Buffer(matrix_narc.files[0]))
        headers_by_matrix = []
        for x in range(len(matrix_narc.files)):  # one entry for each matrix
            headers_by_matrix.append([])

        for header in headers:  # creates a list of what headers are used on each matrix/ vice versa
            headers_by_matrix[header.matrix_id].append(header.id)

        for x in range(len(headers_by_matrix)):
            print(str(x) + ': ' + str(headers_by_matrix[x]))

        events = []
        for x in range(len(events_narc.files)):
            events.append(Events(Buffer(events_narc.files[x])))

        # for x in headers_by_matrix[0]:
        #     for warp in events[headers[x].event_id].warps:
        #         canvas.create_line(2*warp.global_x_pos,2*warp.global_y_pos, 2*warp.global_x_pos + 1,
        #         2*warp.global_y_pos+1, fill='black')

        # root.wm_attributes("-transparent", True)
        # canvas.pack()
        # root.mainloop()

        headers_by_area_data = []
        for y in range(len(matrix_narc.files)):  # one entry for each matrix
            headers_by_area_data.append([])
            for x in range(106):  # one entry for each area data value
                headers_by_area_data[y].append([])

        for y in range(len(headers_by_area_data)):  # iterates through for each matrix num
            for x in headers_by_matrix[y]:  # creates a structure readable as: headers_by_area_data[matrix id][area data ID] -> list of what headers use that area data ID
                headers_by_area_data[y][headers[x].area_data_id].append(x)

        new_sorted_headers = []

        for x in range(len(headers_by_area_data[0])):
            if len(headers_by_area_data[0][x]) != 0:
                new_sorted_headers.append(headers_by_area_data[x])

        # for row in range(matrix_0.y):
        #     for col in range(matrix_0.x):
        #         print(self.color_txt(matrix_0.get_header(row, col), new_sorted_headers[0]), end=',')
        #     print()

        matrices = []
        for x in range(len(matrix_narc.files)):
            matrices.append(Matrix(Buffer(matrix_narc.files[x])))

        names = []
        name_buffer = Buffer(rom.getFileByName('/fielddata/maptable/mapname.bin'))
        for x in range(int(len(name_buffer.data) / 0x10)):
            name = name_buffer.read_bytes(0x10)
            end = 0x10
            for b in range(len(name)):
                if name[b] == 0x00:
                    end = b
                    break
            names.append(name[0:end].decode())

        # uncomment the line below to reactivate JSON generation (dev only) (DON'T TOUCH!!!)
        # JohtoFileDataGenerator.write_json(headers_by_area_data, headers, matrices, events, names, rom)

        # this is a test to show that warps can be edited properly
        # for x in range(len(events)):
        #     for warp in events[x].warps:
        #         warp.dest_header = 3
        #         warp.dest_warp_id = 0
        #     events_narc.files[x] = events[x].write()
        # rom.setFileByName('/fielddata/eventdata/zone_event.narc', events_narc.save())
        # rom.saveToFile('Platinum_edited.nds')

    def color_txt(self, value, sorted_headers):
        return (self.get_color(value, sorted_headers) + self.reset).format(self.fix_length(value))

    def fix_length(self, value):
        return '0' * (4 - len(str(value)) % 4) + str(value)

    def get_color(self, value, sorted_headers):
        for row in range(len(sorted_headers)):
            for col in range(len(sorted_headers[row])):
                if sorted_headers[row][col] == value:
                    return self.colors[row]
