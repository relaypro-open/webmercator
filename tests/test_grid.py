# MIT License
#
# Copyright (c) 2018 Republic Wireless
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import unittest

from webmercator import Grid


class TestGrid(unittest.TestCase):

    def setUp(self):
        self.x, self.y = 100, 100

        self.width = 4
        self.height = 4

    def test_init_(self):
        Grid(vertex=(self.x, self.y), width=self.width, height=self.height)

    def test_init_empty(self):
        with self.assertRaises(AttributeError):
            Grid()

    def test_init_no_vertex(self):
        with self.assertRaises(AttributeError):
            Grid(width=self.width, height=self.height)

    def test_init_no_bounds(self):
        with self.assertRaises(AttributeError):
            Grid(vertex=(self.x, self.y))

    def test_init_no_width(self):
        with self.assertRaises(AttributeError):
            Grid(vertex=(self.x, self.y), height=self.height)

    def test_init_no_height(self):
        with self.assertRaises(AttributeError):
            Grid(vertex=(self.x, self.y), width=self.width)

    def test_iter_size(self):
        g = Grid(vertex=(self.x, self.y), width=self.width, height=self.height)
        grid = [x for x in g]
        self.assertEqual(len(grid), (self.width + 1) * (self.height + 1))


if __name__ == '__main__':
    unittest.main()
