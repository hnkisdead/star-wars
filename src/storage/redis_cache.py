import attr
from aioredis import Redis


@attr.s
class RedisCache(object):
    client: Redis = attr.ib()

    @classmethod
    def from_url(cls, url: str) -> "RedisCache":
        return cls(client=Redis.from_url(url))

    async def set(self, key: str, value: str) -> bool:
        return await self.client.set(name=key, value=value)

    async def get(self, key: str) -> str:
        data = await self.client.get(name=key)
        return data.decode() if data else data

    async def flush_db(self) -> bool:
        return await self.client.flushdb()
