import abc
import asyncio
from itertools import chain
from typing import List

import aiohttp
import attr

from src.domain.entity.planet import Planet
from src.domain.use_case.get_planets import IPlanetsRepository


@attr.s
class ICache(abc.ABC):
    client: attr.ib()

    @abc.abstractmethod
    async def set(self, key, value):
        raise NotImplemented

    @abc.abstractmethod
    async def get(self, key):
        raise NotImplemented


@attr.s
class StarWarsAPIPlanetsRepository(IPlanetsRepository):
    cache: ICache = attr.ib()
    planets_url: str = attr.ib(default="https://swapi.dev/api/planets/?page={}")

    async def get_pages_urls(self, session) -> List[str]:
        page_num = 1

        async with session.get(self.planets_url.format(page_num)) as response:
            data = await response.json()

            pages_count = data["count"] // len(data["results"])

            return [self.planets_url.format(page_num) for page_num in range(1, pages_count + 1)]

    async def get_page(self, session: aiohttp.ClientSession, page_url: str) -> List[str]:
        cached = await self.cache.get(page_url)

        if cached:
            return cached.split(",")

        async with session.get(page_url) as response:
            data = await response.json()

            planet_names = [result["name"] for result in data["results"]]

            await self.cache.set(page_url, ",".join(planet_names))

            return planet_names

    async def get_planets(self, session: aiohttp.ClientSession, pages_urls: List[str]) -> List[Planet]:
        tasks = [asyncio.create_task(self.get_page(session, pages_url)) for pages_url in pages_urls]

        result = await asyncio.gather(*tasks)

        result = chain(*result)

        return [Planet(name=planet_name) for planet_name in result]

    async def list(self) -> List[Planet]:
        async with aiohttp.ClientSession() as session:
            page_urls = await self.get_pages_urls(session)

            planets = await self.get_planets(session, page_urls)

            return planets
