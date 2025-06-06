#!/bin/bash
## TODO: find a better way to reinstall a project you're working on.
## with most recent changes
rm -r *.egg-info
rm -r build
pipx uninstall {{ cookiecutter.hyphenated }}
pipx install .
