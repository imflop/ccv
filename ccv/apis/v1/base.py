from fastapi import APIRouter

from . import common, short


API_BASE_URL_PREFIX = "/api/v1"


router = APIRouter(prefix=API_BASE_URL_PREFIX)
router.include_router(common.router)
router.include_router(short.router)
