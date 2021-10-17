from os.path import dirname, join
from typing import List

from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from src.domain.entity.planet import Planet
from src.domain.use_case.get_planets import GetPlanets, IGetPlanets, IPlanetsRepository
from src.repositories.star_wars_api_planets_repository import StarWarsAPIPlanetsRepository

router = APIRouter()

current_dir = dirname(__file__)
templates = Jinja2Templates(directory=join(current_dir, "templates"))


@router.get("/", response_class=HTMLResponse)
async def index(request: Request):
    repository: IPlanetsRepository = StarWarsAPIPlanetsRepository()

    use_case: IGetPlanets = GetPlanets(repository=repository)

    planets: List[Planet] = await use_case.handle()

    return templates.TemplateResponse(name="index.html", context={"request": request, "planets": planets})
