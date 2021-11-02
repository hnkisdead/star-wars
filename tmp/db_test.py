import asyncio

import databases
from sqlalchemy import text, Table, create_engine, MetaData, Column, Integer, String

DATABASE_URL = "postgresql://postgres:postgres@localhost:55432/postgres"

metadata = MetaData()

PlanetsTable = Table(
    "planets", metadata, Column("id", Integer, primary_key=True), Column("name", String(length=100), primary_key=True)
)


async def test_databases():
    database = databases.Database(DATABASE_URL)
    await database.connect()

    await database.disconnect()


def test_sqlalchemy():
    engine = create_engine(DATABASE_URL, echo=True, future=True)

    with engine.begin() as connection:
        result = connection.execute(PlanetsTable.select())
        print(result.all())


if __name__ == "__main__":
    asyncio.run(test_databases())

    test_sqlalchemy()
