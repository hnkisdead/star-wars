import attr
from aioredis import Redis


@attr.s
class RedisCache(object):
    client: Redis = attr.ib()

    @classmethod
    def from_url(cls, url):
        return cls(client=Redis.from_url(url))

    async def set(self, key, value):
        return await self.client.set(name=key, value=value)

    async def get(self, key):
        return (await self.client.get(name=key)).decode()
