import abc
import asyncio
import json
from itertools import chain
from typing import List

import aiohttp
import attr

from src.domain.entity.planet import Planet
from src.domain.use_case.get_planets import IPlanetsRepository


@attr.s
class ICache(abc.ABC):
    client = attr.ib()

    @abc.abstractmethod
    async def set(self, key, value):
        raise NotImplemented

    @abc.abstractmethod
    async def get(self, key):
        raise NotImplemented


@attr.s
class StarWarsAPIPlanetsRepository(IPlanetsRepository):
    cache: ICache = attr.ib()
    skip_cache: bool = attr.ib(default=False)
    planets_url: str = attr.ib(default="https://swapi.dev/api/planets/?page={}")

    async def _get_pages_urls(self, session) -> List[str]:
        page_num = 1

        async with session.get(self.planets_url.format(page_num)) as response:
            data = await response.json()

            pages_count = data["count"] // len(data["results"])

            return [self.planets_url.format(page_num) for page_num in range(1, pages_count + 1)]

    async def _get_page(self, session: aiohttp.ClientSession, page_url: str) -> List[str]:
        if not self.skip_cache:
            cached = await self.cache.get(page_url)

            if cached:
                return json.loads(cached)

        async with session.get(page_url) as response:
            data = await response.json()

            await self.cache.set(page_url, json.dumps(data["results"]))

            return data

    async def _get_planets(self, session: aiohttp.ClientSession, pages_urls: List[str]) -> List[Planet]:
        tasks = [asyncio.create_task(self._get_page(session, pages_url)) for pages_url in pages_urls]

        result = await asyncio.gather(*tasks)

        return [Planet(name=planet["name"], external_url=planet["url"]) for planet in chain(*result)]

    async def list(self) -> List[Planet]:
        async with aiohttp.ClientSession() as session:
            page_urls = await self._get_pages_urls(session)

            planets = await self._get_planets(session, page_urls)

            return planets
