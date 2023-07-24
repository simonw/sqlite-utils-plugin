import click
import sqlite_utils


@sqlite_utils.hookimpl
def register_commands(cli):
    return
    # @cli.command()
    # def hello_world():
    #     "Say hello world"
    #     click.echo("Hello world!")


@sqlite_utils.hookimpl
def prepare_connection(conn):
    return
    # conn.create_function(
    #     "hello", 1, lambda name: f"Hello, {name}!"
    # )
