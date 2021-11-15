from fastapi import APIRouter

from src.http.html.index_view import index_view
from src.http.html.planets_view import planets_view

router = APIRouter()

router.add_api_route(path="/", endpoint=index_view)
router.add_api_route(path="/planets", endpoint=planets_view)
