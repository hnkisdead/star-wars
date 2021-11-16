from dependency_injector import containers, providers

from src.domain.use_case.get_planets import GetPlanets
from src.repository.star_wars_api_planets_repository import ICache, StarWarsAPIPlanetsRepository


class RedisCacheStub(ICache):
    async def set(self, key, value):
        return None

    async def get(self, key):
        return None


class CLIContainer(containers.DeclarativeContainer):
    settings = providers.Configuration()
    redis_client = providers.Factory(lambda: None)
    redis_cache = providers.Factory(RedisCacheStub, client=redis_client)
    api_planets_repository = providers.Factory(StarWarsAPIPlanetsRepository, cache=redis_cache)
    get_planets_use_case = providers.Factory(GetPlanets, repository=api_planets_repository)
