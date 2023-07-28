from fastapi import APIRouter
from fastapi import Query
from services.sentiment import get_sentiment, get_sentiment_file
import pandas as pd
from fastapi import FastAPI, File, UploadFile
import io

router = APIRouter()

@router.get("/sentiment")
async def sentiment_analytics(
    sentence: str = Query(default = "")
):
    result = await get_sentiment(sentence)
    return result

@router.post("/sentiment-upload")
async def upload_file(file: UploadFile = File(...)):
    try:
        contents = await file.read()
        df = pd.read_csv(io.BytesIO(contents))
        result = await get_sentiment_file(df)
        return result

    except Exception as e:
        return {"error": str(e)}