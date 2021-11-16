import strawberry
from dependency_injector.wiring import Provide

from src.domain.use_case.get_planets import GetPlanets
from src.web.container import WebContainer

use_case: GetPlanets = Provide[WebContainer.get_planets_use_case]


@strawberry.type
class Planet(object):
    name: str


async def planets_resolver():
    return await use_case.handle()
