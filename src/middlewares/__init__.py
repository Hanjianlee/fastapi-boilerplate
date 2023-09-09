from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


def initialise_middlewares(app: FastAPI) -> None:
    # app.middleware("http")(authenticate)
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    return
