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
import sys

from webmercator import Point
from webmercator import Grid

if (2, 0) >= sys.version_info > (3, 0):
    from builtins import range


class BoundingBox(object):

    def __init__(self, point, **kwargs):
        if not isinstance(point, Point):
            raise TypeError("Did not provide valid point type")

        self.zoom_level = kwargs.get('zoom_level', point.zoom_level)

        self.pt_center = Point(latitude=point.latitude, longitude=point.longitude, zoom_level=self.zoom_level)

        if 'radius' in kwargs:
            self.radius = kwargs['radius']
            self.diameter = self.radius * 2
        elif 'diameter' in kwargs:
            self.diameter = kwargs['diameter']
            self.radius = self.diameter / 2 if self.diameter > 0 else 0
        else:
            raise AttributeError("Missing required kwarg. Either `radius` or `diameter` are required.")

    def __repr__(self):
        return '<BoundingBox center: {}, diameter: {}>'.format(self.pt_center, self.diameter)

    def _bound_vertices(self, num_pts=4):
        """
        Calculate points around a lat/long, given a specific distance and point count

        Using https://www.movable-type.co.uk/scripts/latlong.html#destPoint
            Formula:
                y2 = asin( sin(y1) * cos(d/R) * cos(bearing) )
                x2 = x1 + atan2( sin(bearing) * sin(d/R) * cos(y1), cos(d/R) - sin(y1) * sin(y2) )
                where y is latitude, x in longitude, bearing is clockwise from north, d/R is angular distance

        :param num_pts: Number of vertices around point, defaults to 4. Don't override without clear understanding.
        :return: List of point indices
        """
        radius_earth = 3959.0

        latitude_rad = math.radians(self.pt_center.latitude)
        longitude_rad = math.radians(self.pt_center.longitude)

        # add 45 degrees to orient
        degrees = [(math.degrees(2.0 * math.pi) / num_pts) * (x + 1) for x in range(num_pts)]
        radians = [math.radians(d) for d in degrees]

        bound_vertices = []
        for bearing in radians:
            lat = math.asin(math.sin(latitude_rad) * math.cos(self.radius / radius_earth) +
                            math.cos(latitude_rad) * math.sin(self.radius / radius_earth) * math.cos(bearing))
            lon = longitude_rad + math.atan2(
                math.sin(bearing) * math.sin(self.radius / radius_earth) * math.cos(latitude_rad),
                math.cos(self.radius / radius_earth) - math.sin(latitude_rad) * math.sin(lat))

            lat_degree = math.degrees(lat)
            lon_degree = math.degrees(lon)
            pt = Point(latitude=lat_degree, longitude=lon_degree)
            bound_vertices.append(pt)

        return bound_vertices

    @property
    def box_vertices(self):
        return self._bound_vertices(num_pts=4)

    @property
    def min_longitude(self):
        return min([v.longitude for v in self.box_vertices])

    @property
    def max_longitude(self):
        return max([v.longitude for v in self.box_vertices])

    @property
    def min_latitude(self):
        return min([v.latitude for v in self.box_vertices])

    @property
    def max_latitude(self):
        return max([v.latitude for v in self.box_vertices])

    @property
    def vertex_top_left(self):
        """ TilePoint representing the upper-left vertex of the Bounding Box """
        return Point(latitude=self.max_latitude, longitude=self.min_longitude, zoom_level=self.zoom_level)

    @property
    def vertex_bottom_right(self):
        """ TilePoint representing the lower-right vertex of the Bounding Box """
        return Point(latitude=self.min_latitude, longitude=self.max_longitude, zoom_level=self.zoom_level)

    @property
    def min_pixel_x(self):
        return self.vertex_top_left.pixel_x

    @property
    def max_pixel_x(self):
        return self.vertex_bottom_right.pixel_x

    @property
    def min_pixel_y(self):
        return self.vertex_top_left.pixel_y

    @property
    def max_pixel_y(self):
        return self.vertex_bottom_right.pixel_y

    @property
    def min_tile_x(self):
        return self.vertex_top_left.tile_x

    @property
    def max_tile_x(self):
        return self.vertex_bottom_right.tile_x

    @property
    def min_tile_y(self):
        return self.vertex_top_left.tile_y

    @property
    def max_tile_y(self):
        return self.vertex_bottom_right.tile_y

    @property
    def tile_width(self):
        return self.max_tile_x - self.min_tile_x

    @property
    def tile_height(self):
        return self.max_tile_y - self.min_tile_y

    @property
    def pixel_width(self):
        return max(int(self.vertex_bottom_right.pixel_x - self.vertex_top_left.pixel_x), 1)

    @property
    def pixel_height(self):
        return max(int(self.vertex_bottom_right.pixel_y - self.vertex_top_left.pixel_y), 1)

    @property
    def tile_grid(self):
        """ Returns a Grid iterator. Iterates width, then height. """
        return Grid(vertex=(self.min_tile_x, self.min_tile_y),
                    width=self.tile_width,
                    height=self.tile_height)

    def relative_pixel_x(self, value):
        """ Relative pixel value of left of box """
        return int(value - self.vertex_top_left.pixel_x)

    def relative_pixel_y(self, value):
        """ Relative pixel value of top of box """
        return int(value - self.vertex_top_left.pixel_y)
