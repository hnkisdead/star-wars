from fastapi import FastAPI

from .http.graphql import app as graphql_app
from .http.html import app as html_app

app = FastAPI()

app.include_router(html_app.router)
app.include_router(graphql_app.router, prefix="/graphql")
