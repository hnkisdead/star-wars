from src.settings import Settings


def wire_container(container_cls, packages):
    container = container_cls()
    settings = Settings()
    container.settings.from_pydantic(settings)
    container.wire(packages=packages)

    return container
