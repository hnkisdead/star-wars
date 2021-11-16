import asyncio

import typer
from dependency_injector.wiring import Provide

from src.domain.use_case.get_planets import GetPlanets

from .container import CLIContainer

use_case: GetPlanets = Provide[CLIContainer.get_planets_use_case]


def sync_planets():
    result = asyncio.run(use_case.handle())
    typer.echo(result)
