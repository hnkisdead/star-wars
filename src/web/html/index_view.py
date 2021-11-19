from starlette.requests import Request
from starlette.responses import Response

from src.web.html.templates import templates


def index_view(request: Request) -> Response:
    return templates.TemplateResponse(name="index.html", context={"request": request})
