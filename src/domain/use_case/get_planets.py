import abc
from typing import List

import attr

from src.domain.entity.planet import Planet


@attr.s
class IPlanetsRepository(abc.ABC):
    @abc.abstractmethod
    async def list(self) -> List[Planet]:
        raise NotImplemented


@attr.s
class IGetPlanets(abc.ABC):
    repository: IPlanetsRepository = attr.ib()

    @abc.abstractmethod
    async def handle(self) -> List[Planet]:
        raise NotImplemented


@attr.s
class GetPlanets(IGetPlanets):
    async def handle(self) -> List[Planet]:
        return await self.repository.list()
