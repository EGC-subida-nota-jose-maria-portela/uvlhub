import click

from rosemary.commands.clear_cache import clear_cache
from rosemary.commands.db_console import db_console
from rosemary.commands.db_migrate import db_migrate
from rosemary.commands.db_reset import db_reset
from rosemary.commands.clear_log import clear_log
from rosemary.commands.clear_uploads import clear_uploads
from rosemary.commands.coverage import coverage
from rosemary.commands.linter import linter
from rosemary.commands.update import update
from rosemary.commands.info import info
from rosemary.commands.make_module import make_module
from rosemary.commands.env import env
from rosemary.commands.test import test


class RosemaryCLI(click.Group):
    def get_command(self, ctx, cmd_name):
        rv = super().get_command(ctx, cmd_name)
        if rv is not None:
            return rv
        click.echo(f"No such command '{cmd_name}'.")
        click.echo("Try 'rosemary --help' for a list of available commands.")
        return None


@click.group(cls=RosemaryCLI)
def cli():
    """A CLI tool to help with project development."""
    pass


cli.add_command(update)
cli.add_command(info)
cli.add_command(make_module)
cli.add_command(env)
cli.add_command(test)
cli.add_command(linter)
cli.add_command(coverage)
cli.add_command(clear_uploads)
cli.add_command(clear_log)
cli.add_command(clear_cache)
cli.add_command(db_reset)
cli.add_command(db_migrate)
cli.add_command(db_console)

if __name__ == '__main__':
    cli()