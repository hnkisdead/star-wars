from typing import List

import strawberry
from strawberry.fastapi import GraphQLRouter

from src.web.graphql.planets_resolver import planets_resolver


@strawberry.type
class Query(object):
    planets = strawberry.field(resolver=planets_resolver)


schema = strawberry.Schema(Query)

router = GraphQLRouter(schema)
