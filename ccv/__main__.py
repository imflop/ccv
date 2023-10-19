import uvicorn

from .libs.settings import AppSettings
from .libs.setup_app import setup_app


def main() -> None:
    settings = AppSettings()
    app = setup_app(settings)
    uvicorn.run(app=app, host=settings.host, port=settings.port, http="httptools")


if __name__ == "__main__":
    main()
