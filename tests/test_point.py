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

from webmercator import Point


class TestPoint(unittest.TestCase):

    def setUp(self):
        self.longitude, self.latitude = -78.677972, 35.771834
        self.meter_x, self.meter_y = -8758391.779687436, 4269271.329782032
        self.pixel_x_14, self.pixel_y_14 = 1180487.0, 1650324.0
        self.tile_x_14, self.tile_y_14 = 4611, 6446

        self.zoom_level = 14

        self.pt_null = Point()
        self.pt = Point(latitude=self.latitude, longitude=self.longitude)

    # TEST __INIT__

    def test_init_empty(self):
        self.assertIsNone(self.pt_null.latitude)
        self.assertIsNone(self.pt_null.longitude)

    def test_init_kwargs_geo(self):
        self.assertIsNotNone(self.pt.latitude)
        self.assertIsNotNone(self.pt.longitude)
        self.assertEqual(self.pt.latitude, self.latitude)
        self.assertEqual(self.pt.longitude, self.longitude)

    def test_init_kwargs_meter(self):
        pt_meter = Point(meter_x=self.meter_x, meter_y=self.meter_y)
        self.assertIsNotNone(pt_meter.meter_x)
        self.assertIsNotNone(pt_meter.meter_y)

    def test_init_kwargs_zoom_level(self):
        zl = 5
        self.assertNotEqual(self.pt.zoom_level, zl)

        pt_zoom_level = Point(zoom_level=zl)
        self.assertEqual(pt_zoom_level.zoom_level, zl)

    def test_init_kwargs_pixel(self):
        pt_pixel = Point(pixel_x=self.pixel_x_14, pixel_y=self.pixel_y_14)
        self.assertIsNotNone(pt_pixel.pixel_x)
        self.assertIsNotNone(pt_pixel.pixel_y)

    def test_init_kwargs_tile(self):
        pt_tile = Point(pixel_x=self.tile_x_14, pixel_y=self.tile_y_14)
        self.assertIsNotNone(pt_tile.tile_x)
        self.assertIsNotNone(pt_tile.tile_y)

    # TEST @<variable>.setter and @property (getter)

    def test_get_set_latitude(self):
        self.assertIsNone(self.pt_null.latitude)
        self.pt_null.latitude = self.latitude
        self.assertEqual(self.pt_null.latitude, self.latitude)

    def test_get_set_longitude(self):
        self.assertIsNone(self.pt_null.longitude)
        self.pt_null.longitude = self.longitude
        self.assertEqual(self.pt_null.longitude, self.longitude)

    def test_get_set_longitude_out_of_bounds_init(self):
        nl = self.longitude - 360
        pt = Point(latitude=self.latitude, longitude=nl)
        self.assertEqual(pt.longitude, self.longitude)

        nl = self.longitude + 360
        pt = Point(latitude=self.latitude, longitude=nl)
        self.assertEqual(pt.longitude, self.longitude)

    def test_get_set_longitude_out_of_bounds_setter(self):
        self.assertIsNone(self.pt_null.longitude)
        nl = self.longitude - 360
        self.pt_null.longitude = nl
        self.assertEqual(self.pt_null.longitude, self.longitude)

        nl = self.longitude + 360
        self.pt_null.longitude = nl
        self.assertEqual(self.pt_null.longitude, self.longitude)

    def test_get_set_meter_x(self):
        self.assertIsNone(self.pt_null.meter_x)
        self.pt_null.meter_x = self.meter_x
        self.assertEqual(self.pt_null.meter_x, self.meter_x)

    def test_get_set_meter_y(self):
        self.assertIsNone(self.pt_null.meter_y)
        self.pt_null.meter_y = self.meter_y
        self.assertEqual(self.pt_null.meter_y, self.meter_y)

    def test_get_set_zoom_level(self):
        zl = 5
        self.assertIsNotNone(self.pt_null.zoom_level)
        self.pt_null.zoom_level = zl
        self.assertEqual(self.pt_null.zoom_level, zl)

    def test_get_set_zoom_level_out_of_bounds(self):
        zl = -1
        self.assertIsNotNone(self.pt_null.zoom_level)
        self.pt_null.zoom_level = zl
        self.assertNotEqual(self.pt_null.zoom_level, zl)

        zl = 25
        self.pt_null.zoom_level = zl
        self.assertNotEqual(self.pt_null.zoom_level, zl)

    def test_get_set_pixel_x(self):
        self.assertIsNone(self.pt_null.pixel_x)
        self.pt_null.pixel_x = self.pixel_x_14
        self.assertEqual(self.pt_null.pixel_x, self.pixel_x_14)

    def test_get_set_pixel_y(self):
        self.assertIsNone(self.pt_null.pixel_y)
        self.pt_null.pixel_y = self.pixel_y_14
        self.assertEqual(self.pt_null.pixel_y, self.pixel_y_14)

    def test_get_set_tile_x(self):
        self.assertIsNone(self.pt_null.tile_x)
        self.pt_null.tile_x = self.tile_x_14
        self.assertEqual(self.pt_null.tile_x, self.tile_x_14)

    def test_get_set_tile_y(self):
        self.assertIsNone(self.pt_null.tile_y)
        self.pt_null.tile_y = self.tile_y_14
        self.assertEqual(self.pt_null.tile_y, self.tile_y_14)


# TEST conversions
class TestPointConversions(unittest.TestCase):

    def setUp(self):
        self.longitude, self.latitude = -78.677972, 35.771834
        self.meter_x, self.meter_y = -8758391.779687436, 4269271.329782032

        self.pt_geo = Point(latitude=self.latitude, longitude=self.longitude)

    def test_geo_geo_conversions(self):
        geo_x, geo_y = self.pt_geo.longitude, self.pt_geo.latitude

        self.assertEqual(geo_x, self.longitude)
        self.assertEqual(geo_y, self.latitude)

    def test_geo_meter_conversions(self):
        meter_x, meter_y = self.pt_geo.meter_x, self.pt_geo.meter_y

        pt_meter = Point(meter_x=meter_x, meter_y=meter_y)

        geo_x, geo_y = pt_meter.longitude, pt_meter.latitude

        self.assertEqual(geo_x, self.longitude)
        self.assertEqual(geo_y, self.latitude)

    def test_geo_pixel_conversions(self):
        pixel_x_14, pixel_y_14 = self.pt_geo.pixel_x, self.pt_geo.pixel_y

        pt_pixel = Point(pixel_x=pixel_x_14, pixel_y=pixel_y_14)

        meter_x, meter_y = pt_pixel.meter_x, pt_pixel.meter_y

        self.assertAlmostEqual(meter_x, self.meter_x, delta=self.pt_geo.meters_per_pixel)
        self.assertAlmostEqual(meter_y, self.meter_y, delta=self.pt_geo.meters_per_pixel)

    def test_geo_pixel_conversions_non_default_zoom(self):
        zl = 10
        self.pt_geo.zoom_level = zl
        pixel_x_14, pixel_y_14 = self.pt_geo.pixel_x, self.pt_geo.pixel_y

        pt_pixel = Point(pixel_x=pixel_x_14, pixel_y=pixel_y_14, zoom_level=zl)

        meter_x, meter_y = pt_pixel.meter_x, pt_pixel.meter_y

        self.assertAlmostEqual(meter_x, self.meter_x, delta=self.pt_geo.meters_per_pixel)
        self.assertAlmostEqual(meter_y, self.meter_y, delta=self.pt_geo.meters_per_pixel)

    def test_geo_tile_conversions(self):
        tile_x_14, tile_y_14 = self.pt_geo.tile_x, self.pt_geo.tile_y

        pt_tile = Point(tile_x=tile_x_14, tile_y=tile_y_14)

        meter_x, meter_y = pt_tile.meter_x, pt_tile.meter_y

        self.assertAlmostEqual(meter_x, self.meter_x, delta=self.pt_geo.meters_per_tile)
        self.assertAlmostEqual(meter_y, self.meter_y, delta=self.pt_geo.meters_per_tile)

    def test_geo_tile_conversions_non_default_zoom(self):
        zl = 5
        self.pt_geo.zoom_level = zl
        tile_x_14, tile_y_14 = self.pt_geo.tile_x, self.pt_geo.tile_y

        pt_tile = Point(tile_x=tile_x_14, tile_y=tile_y_14, zoom_level=zl)

        meter_x, meter_y = pt_tile.meter_x, pt_tile.meter_y

        self.assertAlmostEqual(meter_x, self.meter_x, delta=self.pt_geo.meters_per_tile)
        self.assertAlmostEqual(meter_y, self.meter_y, delta=self.pt_geo.meters_per_tile)


if __name__ == '__main__':
    unittest.main()
