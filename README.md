# sqlite-utils-plugin cookiecutter template

A cookiecutter template for creating new [sqlite-utils plugins](https://sqlite-utils.datasette.io/en/stable/plugins.html).
`
## Installation

You'll need to have [cookiecutter](https://cookiecutter.readthedocs.io/) installed. I recommend pipx for this:

    pipx install cookiecutter

Regular `pip` will work OK too.

## Usage

Run `cookiecutter gh:simonw/sqlite-utils-plugin` and then answer the prompts. Here's an example run:

```bash
cookiecutter gh:simonw/sqlite-utils-plugin
```
```
plugin_name []: plugin template demo
description []: Demonstrating https://github.com/simonw/sqlite-utils-plugin
hyphenated [plugin-template-demo]: 
underscored [plugin_template_demo]: 
github_username []: simonw
author_name []: Simon Willison
```
I strongly recommend accepting the suggested value for "hyphenated" and "underscored" by hitting enter on those prompts.

This will create a directory called `sqlite-utils-plugin-template-demo` - the plugin name you enter is converted to lowercase and uses hyphens instead of spaces.

## Developing your plugin

Having created the new plugin structure from the template, here's how to start working on the plugin.

You can install the plugin in "editable" mode like so:

```bash
sqlite-utils install -e .
```
Run this in the `sqlite-utils-plugin-template-demo` directory.

You can also pass the path to that directory like this:

```bash
sqlite-utils install -e path/to/sqlite-utils-plugin-template-demo
```

To confirm it is installed, run:

```bash
sqlite-utils plugins
```

You should see the following:
```json
[
  {
    "name": "sqlite-utils-plugin-template-demo",
    "hooks": [
      "prepare_connection",
      "register_commands"
    ],
    "version": "0.1"
  }
]
```
You can run the tests for your plugin with `pytest` - follow the development environment instructions in the plugin's generated README for details.
