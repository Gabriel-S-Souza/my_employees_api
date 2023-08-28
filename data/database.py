import databases
import sqlalchemy
from dotenv import dotenv_values

DATABASE_URL = dotenv_values(".env")["DATABASE_URL"]

metadata = sqlalchemy.MetaData()

def init_db() -> databases.Database:
    engine = sqlalchemy.create_engine(DATABASE_URL)
    global metadata
    metadata.create_all(engine)
    database = databases.Database(DATABASE_URL)
    return database

async def clear_table(database: databases.Database, table: sqlalchemy.Table):
    query = table.delete()
    await database.execute(query)


