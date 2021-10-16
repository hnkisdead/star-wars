import asyncio
from itertools import chain
from typing import List

import aiohttp
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory="templates")

PLANETS_URL = "https://swapi.dev/api/planets/?page={}"


async def get_pages_urls(session) -> List[str]:
    page_num = 1

    async with session.get(PLANETS_URL.format(page_num)) as response:
        data = await response.json()

        pages_count = data["count"] // len(data["results"])

        return [PLANETS_URL.format(page_num) for page_num in range(1, pages_count + 1)]


async def get_page(session: aiohttp.ClientSession, page_url: str) -> List[str]:
    async with session.get(page_url) as response:
        data = await response.json()
        return [result["name"] for result in data["results"]]


async def get_planets(
    session: aiohttp.ClientSession, pages_urls: List[str]
) -> List[str]:
    tasks = [
        asyncio.create_task(get_page(session, pages_url)) for pages_url in pages_urls
    ]

    result = await asyncio.gather(*tasks)

    result = chain(*result)

    return list(result)


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    async with aiohttp.ClientSession() as session:
        page_urls = await get_pages_urls(session)

        planets = await get_planets(session, page_urls)

    return templates.TemplateResponse(
        name="index.html", context={"request": request, "planets": planets}
    )
