from fastapi import FastAPI
from src.config import settings
from src.routers.post_routers import post_router
import uvicorn

app = FastAPI()

app.include_router(post_router, prefix="/api")


@app.get("/")
def root():
    return {
        "DB_URL": settings.db_url,
        "DEBUG": settings.debug,
    }


def start():
    uvicorn.run("src.main:app", host="0.0.0.0", port=8000, reload=True)


if __name__ == "__main__":
    start()
