===========
WebMercator
===========

.. image:: https://travis-ci.org/republicwireless-open/webmercator.svg?branch=master
    :target: https://travis-ci.org/republicwireless-open/webmercator

.. image:: https://codecov.io/gh/republicwireless-open/webmercator/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/republicwireless-open/webmercator

.. image:: https://img.shields.io/pypi/v/webmercator.svg?style=flat
    :target: https://pypi.python.org/pypi/webmercator

.. image:: https://img.shields.io/badge/License-MIT-yellow.svg
    :target: https://opensource.org/licenses/MIT

WebMercator is a Python (2.7, 3.4, 3.5, 3.6) package to aid in geographic point conversion onto a Mercator projection for tile systems.


Getting Started
---------------

Prerequisites
^^^^^^^^^^^^^

To utilize or contribute to Webmercator, all you need is Python!

Installing
^^^^^^^^^^

For bleeding edge

.. code-block:: bash

    # keeping the repo local
    $ git clone git@github.com:republicwireless-open/webmercator
    $ cd webmercator
    $ python setup.py install

    # only install; no need to clone
    $ pip install git+https://github.com/republicwireless-open/webmercator@master

Or for PyPi releases

.. code-block:: bash

    $ pip install webmercator>=0.1.0


Running the tests
-----------------

Tests can be run in many ways:

.. code-block:: bash

    # runs all tests, in all environments
    $ path/to/tox

    # runs all tests, only in Python 2.7
    $ path/to/tox -e py27

    # runs specific test class, only in Python 3.6
    $ path/to/tox -e py36 tests/point.py

    # runs specific test class, only in Python 3.6
    $ path/to/tox -e py36 tests/point.py:TestPoint

    # runs specific test class, only in Python 3.6
    $ path/to/tox -e py36 tests/point.py:TestPoint.test_init_empty

    # only runs style guide tests
    $ path/to/tox -e flake8

Contributing
------------

Please read `CONTRIBUTING.md <https://github.com/republicwireless-open/webmercator/blob/master/.github/CONTRIBUTING.md>`_ for details on our code of conduct, and the process for submitting pull requests to us.

Versioning
----------

We use `SemVer <http://semver.org/>`_ for versioning. For the versions available, see the `tags on this repository <https://github.com/republicwireless-open/webmercator/tags>`_.

Authors
-------

* `Dayne Batten <https://github.com/daynebatten>`_
* `Dillon Stadther <https://github.com/dlstadther>`_

See also the list of `contributors <https://github.com/republicwireless-open/webmercator/contributors>`_ who participated in this project.

License
-------

This project is licensed under the `MIT License <https://github.com/republicwireless-open/webmercator/blob/master/LICENSE>`_

Acknowledgments
---------------

* `Bing Maps Tile System <https://msdn.microsoft.com/en-us/library/bb259689.aspx>`_ - The Mercator calculations used
* `Decimal Degrees <https://en.wikipedia.org/wiki/Decimal_degrees>`_ - Precision translation
* `Zoom Levels <https://wiki.openstreetmap.org/wiki/Zoom_levels>`_ - Zoom level pixel/tile size
* `Haversine Formula <https://en.wikipedia.org/wiki/Haversine_formula>`_
* `Geocoordinate Translation (distance) <https://www.movable-type.co.uk/scripts/latlong.html>`_
