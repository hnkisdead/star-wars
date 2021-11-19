import abc
from typing import List

import attr

from src.domain.entity.planet import Planet


@attr.s
class IAPIPlanetsRepository(abc.ABC):
    @abc.abstractmethod
    async def list(self) -> List[Planet]:
        raise NotImplemented


@attr.s
class IDBPlanetsRepository(abc.ABC):
    @abc.abstractmethod
    async def save(self, planet: Planet) -> Planet:
        raise NotImplemented


@attr.s
class SyncPlanets(object):
    api_repository: IAPIPlanetsRepository = attr.ib()
    db_repository: IDBPlanetsRepository = attr.ib()

    async def handle(self) -> List[Planet]:
        planets = await self.api_repository.list()

        return planets
