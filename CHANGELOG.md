# 2.2.0

**2020-07-10**

- Pair projects to directories. Calling `cav load` with no arguments will load projects related to your current working directory and parent directories
    - This works by using a dictionary called `"_directories"` in `.secrets.json`
- Move `__init__.py` functions to `cavalry.py`
- Allow `list`-ing multiple projects

---

- Remove `# Script` (output from `cav -h`) from [README.md](README.md)
- Clarify [Loading Variables](README.md#Loading%20Variables) in README
- Provide text output to the shell when interacting with variables via [src/cav](src/cav)
- Switch scripts to bash and require bash in [CONTRIBUTING.md](CONTRIBUTING.md)
- Comment out comment text in [issue templates](.github/ISSUE_TEMPLATE)
- Add license to setup.py
- Change prog in argparse settings
- Move list functionality to `cavalry.Secrets`. This was done mainly to remove the `_directories` hidden table.

**Bug fixes**

- Fix error where tests run with `--silence-[warn|pass]` did not run python tests properly