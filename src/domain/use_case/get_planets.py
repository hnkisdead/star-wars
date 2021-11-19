from typing import List, Protocol

import attr

from src.domain.entity.planet import Planet


class IPlanetsRepository(Protocol):
    async def list(self) -> List[Planet]:
        ...


@attr.s
class GetPlanets(object):
    repository: IPlanetsRepository = attr.ib()

    async def handle(self) -> List[Planet]:
        return await self.repository.list()
