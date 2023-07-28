from transformers import AutoModelForSequenceClassification
from transformers import AutoTokenizer
from transformers import pipeline
import re,string
from services.cleansing import cleansing
from fastapi import status
from fastapi.responses import PlainTextResponse
from fastapi.responses import Response
import sqlite3

pretrained = "ayameRushia/bert-base-indonesian-1.5G-sentiment-analysis-smsa"
model = AutoModelForSequenceClassification.from_pretrained(pretrained)
tokenizer = AutoTokenizer.from_pretrained(pretrained)
classifier = pipeline("sentiment-analysis", model=model, tokenizer=tokenizer)

async def insert_db(df):
    conn = sqlite3.connect('tweets.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS tweets
                        (Tweet TEXT, Tweets_clean TEXT, Sentiment TEXT)''')
    df.to_sql('tweets', conn, if_exists='append', index=False)
    conn.close()


async def get_sentiment(input):
    try:
        result = await cleansing(input)
        result = result['data']
        sentiment = classifier(result)
        content = {
            "ok": True,
            "code": status.HTTP_200_OK,
            "data": sentiment,
            "message": "Success",
        }
        return content
    except Exception as e:
        return e


async def get_sentiment_file(df):
    try:
        tweets_list = df['Tweet'].tolist()
        tweets_clean_list = []
        sentiment_list = []

        for tweet in tweets_list:
            tweet_clean = await cleansing(tweet)
            tweets_clean_list.append(tweet_clean['data'])
            sentiment = classifier(tweet_clean['data'])
            sentiment_list.append(sentiment[0]['label'])

        df['Tweets_clean'] = tweets_clean_list
        df['Sentiment'] = sentiment_list

        await insert_db(df=df)

        csv_data = df.to_csv(index=False)
        response = Response(content=csv_data, media_type="text/csv")
        response.headers["Content-Disposition"] = "attachment; filename=data.csv"
        return response
    except Exception as e:
        content = {
            "ok": False,
            "code": 400,
            "message": "Failed, data format not allowed !",
        }
        return content