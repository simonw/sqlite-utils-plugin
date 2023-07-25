# sqlite-utils-{{ cookiecutter.hyphenated }}

[![PyPI](https://img.shields.io/pypi/v/sqlite-utils-{{ cookiecutter.hyphenated }}.svg)](https://pypi.org/project/sqlite-utils-{{ cookiecutter.hyphenated }}/){% if cookiecutter.github_username %}
[![Changelog](https://img.shields.io/github/v/release/{{ cookiecutter.github_username }}/sqlite-utils-{{ cookiecutter.hyphenated }}?include_prereleases&label=changelog)](https://github.com/{{ cookiecutter.github_username }}/sqlite-utils-{{ cookiecutter.hyphenated }}/releases)
[![Tests](https://github.com/{{ cookiecutter.github_username }}/sqlite-utils-{{ cookiecutter.hyphenated }}/workflows/Test/badge.svg)](https://github.com/{{ cookiecutter.github_username }}/sqlite-utils-{{ cookiecutter.hyphenated }}/actions?query=workflow%3ATest)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://github.com/{{ cookiecutter.github_username }}/sqlite-utils-{{ cookiecutter.hyphenated }}/blob/main/LICENSE){% endif %}

{{ cookiecutter.description or "" }}

## Installation

Install this plugin in the same environment as sqlite-utils.
```bash
sqlite-utils install sqlite-utils-{{ cookiecutter.hyphenated }}
```
## Usage

Usage instructions go here.

## Development

To set up this plugin locally, first checkout the code. Then create a new virtual environment:
```bash
cd sqlite-utils-{{ cookiecutter.hyphenated }}
python3 -m venv venv
source venv/bin/activate
```
Now install the dependencies and test dependencies:
```bash
pip install -e '.[test]'
```
To run the tests:
```bash
pytest
```
