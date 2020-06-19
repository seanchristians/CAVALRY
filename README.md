[![Contributor Covenant](https://img.shields.io/badge/Contributor%20Covenant-v2.0%20adopted-ff69b4.svg)](CODE_OF_CONDUCT.md)

# CAVALRY

Quickly load secrets as environment variables

# Getting Started

```sh
pip3 install cavalry
```

# Usage

Run `cav -h` to see options. Note: the script is not POSIX compatible and requires `/bin/bash`.

## Loading variables

The `load` command will run an eval on the variables exported from the function. To get these into your current scope, the file must be run with `source ...`. Shorthand in most terminals is to simply prepend a dot: `. cav load ...`. **TL/DR**: to load variables, run `. cav load ...`

```sh
usage: cav [-h] [-s FILE] {store,delete,load} ...

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
