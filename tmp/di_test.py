import asyncio

from aioredis import Redis
from dependency_injector import containers, providers
from dependency_injector.wiring import Provide, inject

from src.domain.use_case.get_planets import GetPlanets
from src.repository.star_wars_api_planets_repository import StarWarsAPIPlanetsRepository
from src.settings import Settings
from src.storage.redis_cache import RedisCache


class Container(containers.DeclarativeContainer):
    settings = providers.Configuration()
    redis_client = providers.Callable(Redis.from_url, url=settings.redis_url)
    redis_cache = providers.Factory(RedisCache, client=redis_client)
    api_planets_repository = providers.Factory(StarWarsAPIPlanetsRepository, cache=redis_cache)
    get_planets_use_case = providers.Factory(GetPlanets, repository=api_planets_repository)


def main():
    container = Container()

    container.wire(modules=[__name__])

    settings = Settings(_env_file="../.env")

    container.settings.from_pydantic(settings)


@inject
async def get(use_case: GetPlanets = Provide[Container.get_planets_use_case]):
    data = await use_case.handle()
    print(data)


if __name__ == "__main__":
    main()
    asyncio.run(get())
