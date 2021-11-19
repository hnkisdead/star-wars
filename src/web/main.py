from fastapi import FastAPI

from src.utils.container import wire_container
from src.web.container import WebContainer
from src.web.graphql import app as graphql_app
from src.web.html import app as html_app


def create_app() -> FastAPI:
    new_app = FastAPI()

    new_app.include_router(html_app.router)
    new_app.include_router(graphql_app.router, prefix="/graphql")

    wire_container(container_cls=WebContainer, packages=["src.web"])

    return new_app


app = create_app()
