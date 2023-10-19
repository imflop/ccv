from collections import abc
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import ORJSONResponse
from starlette.middleware import Middleware

from ccv import MODULE_NAME, DESCRIPTION, VERSION
from .settings import AppSettings, SETTINGS_KEY
from ..apis.v1.base import router as router_v1
from ..apis.static.base import router as router_static_pages


def setup_app(settings: AppSettings) -> FastAPI:
    @asynccontextmanager
    async def app_lifespan(app: FastAPI) -> abc.AsyncIterator[None]:
        try:
            yield
        finally:
            pass

    middlewares = [
        Middleware(
            CORSMiddleware,
            allow_origins=add_origins(settings.port),
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )
    ]

    app = FastAPI(
        title=MODULE_NAME,
        version=VERSION,
        description=DESCRIPTION,
        middleware=middlewares,
        lifespan=app_lifespan,
        default_response_class=ORJSONResponse,
        **{SETTINGS_KEY: settings}  # type: ignore
    )

    app.include_router(router_v1)
    app.include_router(router_static_pages)

    return app


def add_origins(port: int) -> abc.Sequence[str]:
    return f"http://localhost:{port}", f"http://0.0.0.0:{port}"
