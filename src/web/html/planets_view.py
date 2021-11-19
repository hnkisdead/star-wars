from typing import List

from starlette.requests import Request
from starlette.responses import Response

from src.domain.entity.planet import Planet
from src.domain.use_case.get_planets import GetPlanets
from src.repository.star_wars_api_planets_repository import StarWarsAPIPlanetsRepository
from src.settings import get_settings
from src.storage.redis_cache import RedisCache
from src.web.html.templates import templates


async def planets_view(request: Request) -> Response:
    settings = get_settings()

    cache = RedisCache.from_url(url=settings.redis_url)

    repository = StarWarsAPIPlanetsRepository(cache=cache)

    use_case = GetPlanets(repository=repository)

    planets: List[Planet] = await use_case.handle()

    return templates.TemplateResponse(name="planets.html", context={"request": request, "planets": planets})
