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

import sys

if (2, 0) >= sys.version_info > (3, 0):
    from builtins import object


class Grid(object):

    def __init__(self, **kwargs):
        self.x, self.y = 0, 0

        if 'vertex' not in kwargs:
            raise AttributeError('vertex kwarg is required')

        self.__start_x, self.__start_y = kwargs['vertex']

        if 'width' not in kwargs or 'height' not in kwargs:
            raise AttributeError('Both width and height kwargs are required')

        self.__width = int(kwargs['width'])
        self.__height = int(kwargs['height'])

    def __iter__(self):
        return self

    def __iterate(self):
        current_x, current_y = self.__start_x + self.x, self.__start_y + self.y

        if self.x > self.__width or self.y > self.__height:
            raise StopIteration
        elif self.x == self.__width:  # end of x, start next row
            self.x = 0
            self.y += 1
        else:
            self.x += 1

        return current_x, current_y

    def __next__(self):
        """ Python3 iterative """
        return self.__iterate()

    def next(self):
        """ Python2 iterative """
        return self.__iterate()
