from starlette.requests import Request

from src.web.html.templates import templates


def index_view(request: Request):
    return templates.TemplateResponse(name="index.html", context={"request": request})
