from typing import List, Type, Union

from src.cli.container import CLIContainer
from src.settings import Settings
from src.web.container import WebContainer

T = Union[CLIContainer, WebContainer]


def wire_container(container_cls: Type[T], packages: List[str]) -> T:
    container = container_cls()
    settings = Settings()
    container.settings.from_pydantic(settings)
    container.wire(packages=packages)

    return container
