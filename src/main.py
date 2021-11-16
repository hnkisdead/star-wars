from fastapi import FastAPI

from .container import wire_container
from .http.graphql import app as graphql_app
from .http.html import app as html_app


def create_app():
    new_app = FastAPI()

    new_app.include_router(html_app.router)
    new_app.include_router(graphql_app.router, prefix="/graphql")

    wire_container()

    return new_app


app = create_app()
