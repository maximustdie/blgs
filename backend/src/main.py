from fastapi import FastAPI

from db.pg.base_model import Base
from db.pg.base import engine

app = FastAPI()


@app.on_event("startup")
async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


@app.get("/")
def main():
    return {"status": "ok"}
