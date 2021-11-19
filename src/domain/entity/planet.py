from typing import Optional

import attr


@attr.s
class Planet(object):
    id: Optional[int] = attr.ib()
    name: str = attr.ib()
    external_url: str = attr.ib()
    saved: bool = attr.ib(default=False)
