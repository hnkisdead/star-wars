from fastapi import FastAPI

from .http.html import app as html_app

app = FastAPI()

app.include_router(html_app.router)
