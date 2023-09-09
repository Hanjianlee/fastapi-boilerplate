from fastapi import FastAPI
import uvicorn
from middlewares import initialise_middlewares
from api import create_app_router
from libs.celery_client.celery_utils import create_celery


def create_app() -> FastAPI:
    current_app = FastAPI(
        title="FastAPI Boilerplate",
        description="Sample FastAPI Application to demonstrate Event "
        "driven architecture with Celery and RabbitMQ",
        version="0.0.0",
    )

    current_app.celery_app = create_celery()
    initialise_middlewares(current_app)
    current_app.include_router(create_app_router())
    return current_app


app = create_app()


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
