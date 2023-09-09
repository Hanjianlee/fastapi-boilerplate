from fastapi import FastAPI
import uvicorn
from middlewares import initialise_middlewares
from api import create_app_router

app = FastAPI()

initialise_middlewares(app)

app.include_router(create_app_router())


def start():
    reload = (
        True  # Should default to false after env config is set up
    )
    host = "localhost"
    # if ENV == "development":
    #     reload = True
    #     host = ENV.SERVER_HOST
    uvicorn.run(
        "main:app",
        host=host,
        reload=reload,
        port=8000,
        reload_dirs=["src"],
    )


if __name__ == "__main__":
    start()
