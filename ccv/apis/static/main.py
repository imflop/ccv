import typing as t
from pathlib import Path

from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates


router = APIRouter(tags=["Main page"])
APP_DIR = Path(__file__).resolve().parent.parent.parent
print(APP_DIR)
templates = Jinja2Templates(directory=f"{APP_DIR}/templates")


@router.get("/", response_class=HTMLResponse)
async def main(request: Request) -> t.Any:
    context = {"request": request}
    return templates.TemplateResponse("main.html", context)