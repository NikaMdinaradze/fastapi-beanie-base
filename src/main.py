from fastapi import FastAPI

from src.database import init_db

app = FastAPI()


@app.on_event("startup")
async def start_db():
    await init_db()


@app.get("/", tags=["Root"])
async def read_root() -> dict:
    return {"message": "Welcome to root api !"}
