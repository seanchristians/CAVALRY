# Contributing

Thanks for taking an interest in **CAVALRY**!

# Issues

Raising issues with the code is very important. This script is responsible for the safety of user's secret keys. Please provide as much information as possible in a bug report.

# Cross-compatibility

This software runs on standard Unix-like systems: Debian, Ubuntu, MacOS, etc. I have no idea if this works on any version of Windows and I don't care. I have no plans to make this library compatible with Windows. However, I am not opposed to contributions in this domain.

# Development Requirements

-   Bourne Shell
-   [GNU Make](https://www.gnu.org/software/make/)
-   [Python 3.8](https://www.python.org/downloads/release/python-380/)
-   [Python setuptools](https://pypi.org/project/setuptools/). Depending on your environment, this may already be included in your standard library

All scripts are run with the standard Bourne Shell `/bin/sh` which is POSIX compatible and included by default everywhere, unlike bash which is included in some systems, but replaced by fish, zsh, csh, etc. in others.

More complex scripts may require another shell for some specific purpose, in that case, make sure to include that environment in all requirements locations: `.travis.yml`, `setup.py`, `MANIFEST.in`, etc.

Note that pip for python 3.8 is required. Make sure you have pip by running `which pip` and that you have the correct version by running `pip -V`. It should end with something similar to `(python 3.8)`. If you do not have pip or the correct version, run `python3 -m pip install --upgrade pip`

# Makefile

To quickly build and install from source, just running `make` with no arguments (or `make all`) will build a wheel and install it to your local site-packages as defined by pip.

# Encryption

-   Cavalry doesn't encrypt `.secrets.json` nor does the option even exist to do so. Adding support for GPG is next up. Desired execution would decrypt the file into memory and re-encrypt on disk write.
-   Cavalry only supports direct key:value data. It does not deal with key:file interactions. The script requires the key be provided directly to it. This might be bad if users' threat models do not trust the software.

# Storage

-   JSON is a simple way of storing data. It may not be the best option for this situation. Feel free to submit a pull request if you can come up with a better way to store user data.
-   `.secrets.json` is not deleted with `pip3 uninstall cavalry`
-   `.secrets.json` is never backed up. Users relying solely on the script to save their API keys may find themselves in unfortunate situations.

# Testing

More and better testing is always good. Testing for this software is especially important due to the sensitive nature of it's operation. Including secrets in a commit or a distribution would be a big problem.

## Notes on `tests/`

-   Executing `tests/run-tests` is the preferred method of running tests
-   `run-tests` will automatically run any _executables_ in `tests/`
-   Python script tests must be suffixed with `.py` so `run-tests` executes them properly in all environments (standard user/virtualenvs/travis-ci).

* * *

# Credit

<https://testlio.com/blog/the-ideal-bug-report/>
<https://blog.usejournal.com/feature-requests-that-dont-suck-d5b776cef1e2>
