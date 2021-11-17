import asyncio

import typer
from dependency_injector.wiring import Provide

from src.cli.container import CLIContainer
from src.storage.redis_cache import RedisCache

cache: RedisCache = Provide[CLIContainer.redis_cache]


def clear_cache():
    result = asyncio.run(cache.flush_db())
    typer.echo("Cache is cleared - {}".format(result))
