from typing import List

import strawberry
from strawberry.fastapi import GraphQLRouter

from src.http.graphql.planets_resolver import planets_resolver, Planet


@strawberry.type
class Query(object):
    planets: List[Planet] = strawberry.field(resolver=planets_resolver)


schema = strawberry.Schema(Query)

router = GraphQLRouter(schema)
