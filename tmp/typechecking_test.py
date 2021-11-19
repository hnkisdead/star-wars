# type: ignore
from typing import Optional

import attr
from pydantic import BaseModel


class PlanetPydantic(BaseModel):
    id: Optional[int]
    name: str


def foo_pydantic(planet: PlanetPydantic) -> None:
    # Error in runtime and on typechecking, pycharm doesn't care
    i = planet.id + 10
    print(i)


@attr.s
class PlanetAttrs(object):
    id: Optional[int] = attr.ib()
    name: str = attr.ib()


def foo_atts(planet: PlanetAttrs) -> None:
    # Error in runtime and on typechecking, pycharm doesn't care
    i = planet.id + 10
    print(i)


if __name__ == "__main__":
    foo_pydantic(PlanetPydantic(name="asdf"))
    foo_atts(PlanetAttrs(name="asdf"))
