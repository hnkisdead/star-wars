from fastapi import FastAPI

from .container import Container
from .http.graphql import app as graphql_app
from .http.html import app as html_app
from .settings import Settings


def create_app():
    new_app = FastAPI()

    new_app.include_router(html_app.router)
    new_app.include_router(graphql_app.router, prefix="/graphql")

    container = Container()
    container.wire(modules=[__name__])
    settings = Settings()
    container.settings.from_pydantic(settings)

    return new_app


app = create_app()
