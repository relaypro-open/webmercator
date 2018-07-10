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

from __future__ import division
import math

from webmercator.util import EARTH_CIRCUMFERENCE_METERS, EARTH_RADIUS_METERS, MERCATOR_MAX_LATITUDE


class Point(object):

    # nanometer (nm)
    metric_exp = 9

    # qualitative scale that can be identified: specialized surveying (e.g. tectonic plate mapping)
    decimal_degree_exp = 8

    def __init__(self, **kwargs):
        self.__latitude = None
        self.__longitude = None
        if 'latitude' in kwargs and 'longitude' in kwargs:
            self.latitude = kwargs['latitude']
            self.longitude = kwargs['longitude']

        if 'meter_x' in kwargs and 'meter_y' in kwargs:
            self.meter_x = kwargs['meter_x']
            self.meter_y = kwargs['meter_y']

        self.__zoom_level = None
        if 'zoom_level' in kwargs:
            self.zoom_level = kwargs['zoom_level']
        else:
            self.zoom_level = 14

        if 'pixel_x' in kwargs and 'pixel_y' in kwargs:
            self.pixel_x = kwargs['pixel_x']
            self.pixel_y = kwargs['pixel_y']

        if 'tile_x' in kwargs and 'tile_y' in kwargs:
            self.tile_x = kwargs['tile_x']
            self.tile_y = kwargs['tile_y']

    def __repr__(self):
        return '<Point at ({}, {})>'.format(self.longitude, self.latitude)

    @property
    def latitude(self):
        return self.__latitude

    @latitude.setter
    def latitude(self, value):
        """ Set latitude, even given out of bounds value """
        self.__latitude = round(min(max(value, -1 * MERCATOR_MAX_LATITUDE), MERCATOR_MAX_LATITUDE),
                                self.decimal_degree_exp)

    @property
    def longitude(self):
        return self.__longitude

    @longitude.setter
    def longitude(self, value):
        """ Set longitude, even given out of bounds value """
        while value < -180:
            value += 360

        while value > 180:
            value -= 360

        self.__longitude = round(value, self.decimal_degree_exp)

    @property
    def meter_x(self):
        """ Rounds to nearest nm """
        if self.longitude:
            meter_x = (self.longitude / 360) * EARTH_CIRCUMFERENCE_METERS
            return round(meter_x, self.metric_exp)

    @meter_x.setter
    def meter_x(self, value):
        """ Convert longitude, given meter `X` - rounded to specialized survey precision """
        self.longitude = (value * 360) / EARTH_CIRCUMFERENCE_METERS

    @property
    def meter_y(self):
        """ Rounds to nearest nm """
        if self.latitude:
            meter_y = (math.log(math.tan(math.pi / 4 + ((self.latitude * math.pi) / 180) / 2))) * EARTH_RADIUS_METERS
            return round(meter_y, self.metric_exp)

    @meter_y.setter
    def meter_y(self, value):
        """ Convert latitude, given meter `Y` - rounded to specialized survey precision """
        self.latitude = (180 / math.pi) * (2 * math.atan(math.exp(value / EARTH_RADIUS_METERS)) - math.pi / 2)

    @property
    def map_size(self):
        return 256 * 2 ** self.zoom_level

    @property
    def zoom_level(self):
        return self.__zoom_level

    @zoom_level.setter
    def zoom_level(self, value):
        self.__zoom_level = min(max(value, 1), 23)

    @property
    def pixel_x(self):
        if self.longitude:
            return round(((self.longitude + 180) / 360) * 256 * 2 ** self.zoom_level)

    @pixel_x.setter
    def pixel_x(self, value):
        map_size = 256 * 2 ** self.__zoom_level
        self.longitude = 360 * (value / map_size - 0.5)

    @property
    def pixel_y(self):
        if self.latitude:
            sin_lat = math.sin(math.radians(self.latitude))
            return round((0.5 - math.log((1 + sin_lat) / (1 - sin_lat)) / (4 * math.pi)) * self.map_size)

    @pixel_y.setter
    def pixel_y(self, value):
        self.latitude = 90 - 360 * math.atan(math.exp(-1 * (0.5 - value / self.map_size) * 2 * math.pi)) / math.pi

    @property
    def tile_x(self):
        return int(self.pixel_x / 256) if self.pixel_x else None

    @tile_x.setter
    def tile_x(self, value):
        self.pixel_x = value * 256

    @property
    def tile_y(self):
        return int(self.pixel_y / 256) if self.pixel_y else None

    @tile_y.setter
    def tile_y(self, value):
        self.pixel_y = value * 256

    @property
    def meters_per_pixel(self):
        """Return meters per pixel (Web Mercator meters, not real world meters)"""
        return EARTH_CIRCUMFERENCE_METERS / (256 * 2 ** self.zoom_level)

    @property
    def meters_per_tile(self):
        """Return meters per tile (Web Mercator meters, not real world meters)"""
        return self.meters_per_pixel * 256
