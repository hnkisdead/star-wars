import typer

from src.cli.do_work import do_work
from src.cli.sync_planets import sync_planets


def create_cli():
    new_cli = typer.Typer()
    add_command = new_cli.command()

    add_command(sync_planets)
    add_command(do_work)

    return new_cli


cli = create_cli()
