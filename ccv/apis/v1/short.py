from fastapi import APIRouter


router = APIRouter(tags=["Shorten actions"])


@router.post("/shorten")
async def short():
    return {"short_url": "https://ccv.pm/fGHd23GFsx"}