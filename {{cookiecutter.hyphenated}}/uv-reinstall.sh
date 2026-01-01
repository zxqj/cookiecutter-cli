#! /bin/bash

uv tool uninstall {{ cookiecutter.hyphenated }}
rm -r build dist *.egg-info
uv build
uv tool install --no-cache .
