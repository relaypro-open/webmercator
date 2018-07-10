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

from webmercator import BoundingBox
from webmercator import Point


class TestBoundingBox(unittest.TestCase):

    def setUp(self):
        self.latitude = 35.771834
        self.longitude = -78.677972

        self.radius = 2.5
        self.diameter = 5

        self.pt = Point(latitude=self.latitude, longitude=self.longitude)

        self.bb = BoundingBox(self.pt, diameter=self.diameter)

    def test_init_invalid_pt(self):
        with self.assertRaises(TypeError):
            BoundingBox(1)

    def test_init_no_distance(self):
        with self.assertRaises(AttributeError):
            BoundingBox(self.pt)

    def test_init_radius(self):
        bb = BoundingBox(self.pt, radius=self.radius)
        self.assertEqual(bb.radius, self.radius)
        self.assertEqual(bb.diameter, self.diameter)

    def test_init_diameter(self):
        bb = BoundingBox(self.pt, diameter=self.diameter)
        self.assertEqual(bb.diameter, self.diameter)
        self.assertEqual(bb.radius, self.radius)

    def test_init_radius_priority(self):
        diameter = 50
        bb = BoundingBox(self.pt, diameter=diameter, radius=self.radius)
        self.assertEqual(bb.radius, self.radius)
        self.assertNotEqual(bb.diameter, diameter)

    def test_init_zoom_level_default(self):
        self.assertEqual(self.bb.pt_center.zoom_level, self.pt.zoom_level)

    def test_init_zoom_level_kwarg(self):
        zl = 10
        bb = BoundingBox(self.pt, zoom_level=zl, radius=self.radius)
        self.assertEqual(bb.pt_center.zoom_level, zl)
        self.assertNotEqual(bb.pt_center.zoom_level, self.pt.zoom_level)

    def test_box_vertices_num(self):
        bv = self.bb.box_vertices
        self.assertEqual(len(bv), 4)

    def test_longitude_min_max(self):
        self.assertLessEqual(self.bb.min_longitude, self.bb.max_longitude)

    def test_latitude_min_max(self):
        self.assertLessEqual(self.bb.min_latitude, self.bb.max_latitude)

    def test_pixel_width_positive(self):
        self.assertGreater(self.bb.pixel_width, 0)

    def test_pixel_height_positive(self):
        self.assertGreater(self.bb.pixel_height, 0)

    def test_tile_grid(self):
        grid_tiles = [p for p in self.bb.tile_grid]

        self.assertEqual(len(grid_tiles), (self.bb.tile_width + 1) * (self.bb.tile_height + 1))


if __name__ == '__main__':
    unittest.main()
