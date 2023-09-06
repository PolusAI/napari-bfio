# napari-bfio

[![License MIT](https://img.shields.io/pypi/l/napari-bfio.svg?color=green)](https://github.com/PolusAI/napari-bfio/raw/main/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/napari-bfio.svg?color=green)](https://pypi.org/project/napari-bfio)
[![Python Version](https://img.shields.io/pypi/pyversions/napari-bfio.svg?color=green)](https://python.org)
[![tests](https://github.com/PolusAI/napari-bfio/workflows/tests/badge.svg)](https://github.com/PolusAI/napari-bfio/actions)
[![codecov](https://codecov.io/gh/PolusAI/napari-bfio/branch/main/graph/badge.svg)](https://codecov.io/gh/PolusAI/napari-bfio)
[![napari hub](https://img.shields.io/endpoint?url=https://api.napari-hub.org/shields/napari-bfio)](https://napari-hub.org/plugins/napari-bfio)

A plugin to read and write images using bfio within napari

----------------------------------

This [napari] plugin was generated with [Cookiecutter] using [@napari]'s [cookiecutter-napari-plugin] template.

<!--
Don't miss the full getting started guide to set up your new package:
https://github.com/napari/cookiecutter-napari-plugin#getting-started

and review the napari docs for plugin developers:
https://napari.org/stable/plugins/index.html
-->

## Installation

You can install `napari-bfio` via [pip]:

    pip install napari-bfio

`napari-bfio` depends on `bfio` package to read/write the data. By default, `bfio` package and the core dependencies (numpy, tifffile, imagecodecs) are installed during the installation process of `napari-bfio`. 

Additionally, `bfio` with other dependencies can be installed:

1. `pip install bfio[bioformats]` - Adds support for BioFormats/Java. See [License](#license) for additional information.
2. `pip install bfio[zarr]` - Adds support for OME Zarr
3. `pip install bfio[all]` - Installs all dependencies.

To install latest development version :

    pip install git+https://github.com/PolusAI/napari-bfio.git


## Contributing

Contributions are very welcome. Tests can be run with [tox], please ensure
the coverage at least stays the same before you submit a pull request.

## License

Distributed under the terms of the [MIT] license,
"napari-bfio" is free and open source software

**NOTE**

Bioformats is licensed under GPL, and as a consequence so is the `bioformats_jar` 
package. These packages and libraries are installed when using the `bfio[bioformats]` option.

## Issues

If you encounter any problems, please [file an issue] along with a detailed description.

[napari]: https://github.com/napari/napari
[Cookiecutter]: https://github.com/audreyr/cookiecutter
[@napari]: https://github.com/napari
[MIT]: http://opensource.org/licenses/MIT
[BSD-3]: http://opensource.org/licenses/BSD-3-Clause
[GNU GPL v3.0]: http://www.gnu.org/licenses/gpl-3.0.txt
[GNU LGPL v3.0]: http://www.gnu.org/licenses/lgpl-3.0.txt
[Apache Software License 2.0]: http://www.apache.org/licenses/LICENSE-2.0
[Mozilla Public License 2.0]: https://www.mozilla.org/media/MPL/2.0/index.txt
[cookiecutter-napari-plugin]: https://github.com/napari/cookiecutter-napari-plugin

[file an issue]: https://github.com/PolusAI/napari-bfio/issues

[napari]: https://github.com/napari/napari
[tox]: https://tox.readthedocs.io/en/latest/
[pip]: https://pypi.org/project/pip/
[PyPI]: https://pypi.org/
