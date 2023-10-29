"""
RandomGenerator.py

Pseudo-Random number generator class

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
import time


class Random:

    def __init__(self, seed):
        if isinstance(seed, int):
            self.seed = ((0x41c64e6d * seed + 0x6073) >> 8) & 0xffffffff
        elif isinstance(seed, str):
            self.seed = hash(seed)

        self.created = []

    def random(self):
        result = ((0x41c64e6d * self.seed + 0x6073) >> 16)
        self.seed = result & 0xffffffff
        self.created.append(result)
        return result

    def randint(self) -> int:
        return int(self.random())

    def randrange(self, start=0, end=1) -> int:
        return self.randint() % (end-start) + start

    def choice(self, seq):
        return seq[self.randrange(start=0, end=len(seq))]


def randrange(end):
    t = round(time.time() * 1000)
    r = Random(t)
    return r.randrange(start=0, end=end)


# if __name__ == "__main__":
#     r = Random(500)
#     result = 0
#     for i in range(1000000):
#         result += r.randrange(start=0, end=10000)
#     print(result)
#     r = Random(3627)
#     result = 0
#     for i in range(1000000):
#         result += r.randrange(start=0, end=10000)
#     print(result)



