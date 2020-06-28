[![Contributor Covenant](https://img.shields.io/badge/Contributor%20Covenant-v2.0%20adopted-ff69b4.svg)](CODE_OF_CONDUCT.md)
[![License](https://img.shields.io/github/license/seanchristians/cavalry)](LICENSE)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
![Build status](https://img.shields.io/travis/seanchristians/cavalry)
[![Commit history](https://img.shields.io/github/last-commit/seanchristians/cavalry)](https://github.com/seanchristians/cavalry/commits)

[![Python wheels](https://img.shields.io/pypi/wheel/cavalry)](https://pypi.org/project/cavalry)
[![PyPI version](https://img.shields.io/pypi/v/cavalry?color=purple)](https://pypi.org/project/cavalry)
[![Code size](https://img.shields.io/github/languages/code-size/seanchristians/cavalry)](https://github.com/seanchristians/cavalry)

[![Python version](https://img.shields.io/pypi/pyversions/cavalry?color=red)](https://pypi.org/project/cavalry)
[![Top language](https://img.shields.io/github/languages/top/seanchristians/cavalry?color=red)](https://github.com/seanchristians/cavalry)

# CAVALRY

Quickly load secrets as environment variables

# Getting Started

```sh
pip3 install cavalry
```

# Usage

Run `cav -h` to see options. Note: the script is not POSIX compatible and requires `/bin/bash`.

## Loading variables

The `load` command will run an eval on the variables exported from the function. To get these into your current scope, the file must be run with `source ...`. Shorthand in most terminals is to simply prepend a dot: `. cav load ...`. **TL;DR**: to load variables, run `. cav load ...`

## Script

```sh
usage: cav [-h] [-s FILE] {store,delete,load,list,clear} ...

Utility to load environment variables. To persist the variables into your
scope, run 'source cav {load,clear} [options]' or '. cav {load,clear} [options]'

positional arguments:
  {store,delete,load,list,clear}
    store               store variables
    delete              delete variables
    load                load variables
    list                list stored data
    clear               clear variables from environment

optional arguments:
  -h, --help            show this help message and exit
  -s FILE, --secrets FILE
                        specify an alternate secrets file
```

---

© 2020 Sean Christians
