from typing import List

import strawberry
from strawberry.fastapi import GraphQLRouter

from src.domain.use_case.get_planets import GetPlanets, IGetPlanets, IPlanetsRepository
from src.repository.star_wars_api_planets_repository import ICache, StarWarsAPIPlanetsRepository
from src.settings import get_settings
from src.storage.redis_cache import RedisCache


@strawberry.type
class Planet(object):
    name: str


async def planets_resolver():
    settings = get_settings()

    cache: ICache = RedisCache.from_url(url=settings.redis_url)

    repository: IPlanetsRepository = StarWarsAPIPlanetsRepository(cache=cache)

    use_case: IGetPlanets = GetPlanets(repository=repository)

    planets: List[Planet] = await use_case.handle()

    return planets


@strawberry.type
class Query(object):
    planets: List[Planet] = strawberry.field(resolver=planets_resolver)


schema = strawberry.Schema(Query)

router = GraphQLRouter(schema)
