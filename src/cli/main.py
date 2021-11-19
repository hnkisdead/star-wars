import typer

from src.cli.clear_cache import clear_cache
from src.cli.container import CLIContainer
from src.cli.sync_planets import sync_planets
from src.utils.container import wire_container


def create_cli() -> typer.Typer:
    new_cli = typer.Typer()
    add_command = new_cli.command()

    add_command(sync_planets)
    add_command(clear_cache)

    wire_container(container_cls=CLIContainer, packages=["src.cli"])

    return new_cli


cli = create_cli()
