from os.path import dirname, join

from starlette.templating import Jinja2Templates

current_dir = dirname(__file__)
templates = Jinja2Templates(directory=join(current_dir, "templates"))