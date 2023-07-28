from fastapi import APIRouter
from fastapi import Query
from services.cleansing import cleansing

router = APIRouter()

@router.get("/cleansing")
async def text_cleansing(
    sentence: str = Query(default = "")
):
    result = await cleansing(sentence)
    return result