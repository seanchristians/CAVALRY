[![Contributor Covenant](https://img.shields.io/badge/Contributor%20Covenant-v2.0%20adopted-ff69b4.svg)](CODE_OF_CONDUCT.md)

# CAVALRY

Quickly load secrets as environment variables

# Getting Started

```sh
pip3 install cavalry
```

# Usage

Run `cav -h` to see options. Note: the script is not POSIX compatible and requires `/bin/bash`.

```sh
usage: cli.py [-h] [-s FILE] {store,delete,load} ...

Utility to load environment variables. To persist the variables into your
scope, run 'source cav [options]' or '. cav [options]'

positional arguments:
  {store,delete,load}
    store               store variables
    delete              delete variables
    load                load variables

optional arguments:
  -h, --help            show this help message and exit
  -s FILE, --secrets FILE
                        specify an alternate secrets file
```

---

© 2020 Sean Christians
