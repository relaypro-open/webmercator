# WebMercator

[![Build Status](https://travis-ci.org/republicwireless-open/webmercator.svg?branch=master)](https://travis-ci.org/republicwireless-open/webmercator)
[![CodeCov](https://codecov.io/gh/republicwireless-open/webmercator/branch/master/graph/badge.svg)](https://codecov.io/gh/republicwireless-open/webmercator)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

WebMercator is a Python (2.7, 3.4, 3.5, 3.6) package to aid in geographic point conversion onto a Mercator projection for tile systems.


## Getting Started

### Prerequisites

To utilize or contribute to Webmercator, all you need is Python!

### Installing

For bleeding edge

```shell
# keeping the repo local
git clone git@github.com:republicwireless-open/webmercator
cd webmercator
python setup.py install

# only install; no need to clone
pip install git+https://github.com/republicwireless-open/webmercator@master
```

Or for PyPi releases

```
pip install webmercator>=0.1.0
```

## Running the tests

Tests can be run in many ways:

```shell
# runs all tests, in all environments
path/to/tox

# runs all tests, only in Python 2.7
path/to/tox -e py27

# runs specific test class, only in Python 3.6
path/to/tox -e py36 tests/point.py

# runs specific test class, only in Python 3.6
path/to/tox -e py36 tests/point.py:TestPoint

# runs specific test class, only in Python 3.6
path/to/tox -e py36 tests/point.py:TestPoint.test_init_empty

# only runs style guide tests
path/to/tox -e flake8
```

## Contributing

Please read [CONTRIBUTING.md](https://github.com/republicwireless-open/webmercator/blob/master/.github/CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/republicwireless-open/webmercator/tags).

## Authors

* [**Dayne Batten**](https://github.com/daynebatten) - [Republic Wireless](https://republicwireless.com)
* [**Dillon Stadther**](https://github.com/dlstadther) - [Republic Wireless](https://republicwireless.com)

See also the list of [contributors](https://github.com/republicwireless-open/webmercator/contributors) who participated in this project.

## License

This project is licensed under the [MIT License](LICENSE)

## Acknowledgments

* [Bing Maps Tile System](https://msdn.microsoft.com/en-us/library/bb259689.aspx) - The Mercator calculations used
* [Decimal Degrees](https://en.wikipedia.org/wiki/Decimal_degrees) - Precision translation
* [Zoom Levels](https://wiki.openstreetmap.org/wiki/Zoom_levels) - Zoom level pixel/tile size
* [Haversine Formula](https://en.wikipedia.org/wiki/Haversine_formula)
* [Geocoordinate Translation (distance)](https://www.movable-type.co.uk/scripts/latlong.html)
