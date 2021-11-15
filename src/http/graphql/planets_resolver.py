from typing import List

import strawberry
from dependency_injector.wiring import Provide

from src.container import Container
from src.domain.use_case.get_planets import GetPlanets

use_case: GetPlanets = Provide[Container.get_planets_use_case]


@strawberry.type
class Planet(object):
    name: str


async def planets_resolver() -> List[Planet]:
    return await use_case.handle()
