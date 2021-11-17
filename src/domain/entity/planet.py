import attr


@attr.s
class Planet(object):
    external_url: str = attr.ib()
    name: str = attr.ib()
