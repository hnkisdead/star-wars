import asyncio

from aioredis import Redis
from dependency_injector import containers, providers
from dependency_injector.wiring import Provide, inject

from src.settings import Settings
from src.storage.redis_cache import RedisCache


class Container(containers.DeclarativeContainer):
    settings = providers.Configuration()
    redis_client = providers.Callable(
        Redis.from_url,
        url=settings.redis_url
    )
    # redis_cache = providers.Factory(
    #     RedisCache
    # )

async def main():
    container = Container()

    container.wire()

    settings = Settings(_env_file='../.env')

    container.settings.from_pydantic(settings)

    redis_client = container.redis_client()
    result = await redis_client.set('asdf', 'saf')
    print(result)
    result = await redis_client.get('asdf')
    print(result)


if __name__ == '__main__':
    asyncio.run(main())