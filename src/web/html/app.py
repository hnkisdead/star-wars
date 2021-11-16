from fastapi import APIRouter

from src.web.html.index_view import index_view
from src.web.html.planets_view import planets_view

router = APIRouter()

router.add_api_route(path="/", endpoint=index_view)
router.add_api_route(path="/planets", endpoint=planets_view)
