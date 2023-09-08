from fastapi import FastAPI
import uvicorn
from middlewares import initialise_middlewares
from api import create_app_router

app = FastAPI()

initialise_middlewares(app)

app.include_router(create_app_router())


def start():
    reload = False
    if ENV == "development":
        reload = True
    uvicorn.run(
        "main:app",
        # host="0:0:0:0",
        reload=reload,
        port=8000,
        reload_dirs=["src"],
    )


if __name__ == "__main__":
    start()
