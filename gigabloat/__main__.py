import click

from .gatherer import commands as gatherCommands


@click.group()
def cli():
    pass


cli.add_command(gatherCommands.scan)

if __name__ == "__main__":
    cli()
