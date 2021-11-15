from typing import List

from starlette.requests import Request

from src.domain.entity.planet import Planet
from src.domain.use_case.get_planets import IPlanetsRepository, IGetPlanets, GetPlanets
from src.http.html.templates import templates
from src.repository.star_wars_api_planets_repository import ICache, StarWarsAPIPlanetsRepository
from src.settings import get_settings
from src.storage.redis_cache import RedisCache


async def planets_view(request: Request):
    settings = get_settings()

    cache: ICache = RedisCache.from_url(url=settings.redis_url)

    repository: IPlanetsRepository = StarWarsAPIPlanetsRepository(cache=cache)

    use_case: IGetPlanets = GetPlanets(repository=repository)

    planets: List[Planet] = await use_case.handle()

    return templates.TemplateResponse(name="planets.html", context={"request": request, "planets": planets})