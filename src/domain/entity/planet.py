import attr


@attr.s
class Planet(object):
    name: str = attr.ib()
