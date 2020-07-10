[![Contributor Covenant](https://img.shields.io/badge/Contributor%20Covenant-v2.0%20adopted-ff69b4.svg)](CODE_OF_CONDUCT.md)
[![License](https://img.shields.io/github/license/seanchristians/cavalry)](LICENSE)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Build Status](https://travis-ci.org/seanchristians/CAVALRY.svg?branch=master)](https://travis-ci.org/seanchristians/CAVALRY)
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

## Loading Variables

Changing environment variables in the current scope from a file must be done through your shell's `source` function. Therefore, you have to run `source cav load` instead of just `cav load`.

# Contributing

If you would like to contribute to the project, please go check out [Contributing](CONTRIBUTING.md). Issue templates are available.

---

© 2020 Sean Christians
