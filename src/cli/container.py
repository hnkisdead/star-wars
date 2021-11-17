from aioredis import Redis
from dependency_injector import containers, providers

from src.domain.use_case.get_planets import GetPlanets
from src.repository.star_wars_api_planets_repository import StarWarsAPIPlanetsRepository
from src.storage.redis_cache import RedisCache


class CLIContainer(containers.DeclarativeContainer):
    settings = providers.Configuration()
    redis_client = providers.Callable(Redis.from_url, url=settings.redis_url)
    redis_cache = providers.Factory(RedisCache, client=redis_client)
    api_planets_repository = providers.Factory(StarWarsAPIPlanetsRepository, cache=redis_cache, skip_cache=True)
    get_planets_use_case = providers.Factory(GetPlanets, repository=api_planets_repository)
