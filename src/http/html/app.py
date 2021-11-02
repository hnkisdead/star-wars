from os.path import dirname, join
from typing import List

from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from src.domain.entity.planet import Planet
from src.domain.use_case.get_planets import GetPlanets, IGetPlanets, IPlanetsRepository
from src.repository.star_wars_api_planets_repository import ICache, StarWarsAPIPlanetsRepository
from src.settings import get_settings
from src.storage.redis_cache import RedisCache

current_dir = dirname(__file__)

router = APIRouter()

templates = Jinja2Templates(directory=join(current_dir, "templates"))


@router.get("/", response_class=HTMLResponse)
async def index(request: Request):
    settings = get_settings()

    cache: ICache = RedisCache.from_url(url=settings.redis_url)

    repository: IPlanetsRepository = StarWarsAPIPlanetsRepository(cache=cache)

    use_case: IGetPlanets = GetPlanets(repository=repository)

    planets: List[Planet] = await use_case.handle()

    return templates.TemplateResponse(name="index.html", context={"request": request, "planets": planets})
