from fastapi import APIRouter
from fastapi import Query
from services.database import ambil_data, ambil_sentiment
from enum import Enum

router = APIRouter()

@router.get("/data")
async def get_data():
    data = await ambil_data()
    content  = {
    "ok" : True,
    "code" : 200,
    "data" : data,
    "messege" : "Success"
    }
    return content


class Sentiment(str, Enum):
    Positive = "Positive"
    Negative = "Negative"
    Neutral = "Neutral"

@router.get("/get_sentiment/{sentiment}")
async def get_data_by_sentiment(sentiment: Sentiment):
    data = await ambil_sentiment(sentiment)
    
    content  = {
    "ok" : True,
    "code" : 200,
    "data" : data,
    "messege" : "Success"
    }
    return content
