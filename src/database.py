import motor.motor_asyncio
from beanie import init_beanie

from src.settings import (
    DATABASE_HOST,
    DATABASE_PASSWORD,
    DATABASE_PORT,
    DATABASE_USERNAME,
    DOCUMENT_MODELS,
)


async def init_db():
    client = motor.motor_asyncio.AsyncIOMotorClient(
        f"mongodb://{DATABASE_USERNAME}:{DATABASE_PASSWORD}@{DATABASE_HOST}:{DATABASE_PORT}"
    )

    await init_beanie(database=client.db_name, document_models=DOCUMENT_MODELS)
