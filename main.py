from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from starlette.responses import FileResponse
import sqlite3 as sql

app = FastAPI()

@app.get("/")
async def index():
#     return JSONResponse(
#         content = {
#             "ok": True,
#             "code": 200,
#             "data": {
#                 "version": "1.0.0"
#             },
#             "message": "Success"
#         }
# )
    return FileResponse('templates/home.html')

# @app.route('/home')
# def home():
#     return render_template('/home.html')

# @app.route('/visualize')
# async def render_visualization():
#     try:
#         con = sql.connect("tweets.db")
#         con.row_factory = sql.Row
#         cur = con.cursor()
#         cur.execute("SELECT * FROM tweets")
#         rows = cur.fetchall()
#     finally:
#         con.close()
    
#     return FileResponse('templates/visualize.html', rows=rows)

# templates = Jinja2Templates(directory="templates")

# @app.get('/visualize')
# async def render_visualization(request: Request):
#     try:
#         con = sql.connect("tweets.db")
#         con.row_factory = sql.Row
#         cur = con.cursor()
#         cur.execute("SELECT * FROM tweets")
#         rows = cur.fetchall()
#     finally:
#         con.close()

#     return templates.TemplateResponse("visualize.html", {"request": request, "rows": rows})

from routers import cleansing
from routers import sentiment
from routers import database

app.include_router(cleansing.router, tags=["Cleansing API"])
app.include_router(sentiment.router, tags=["Sentiment API"])
app.include_router(database.router, tags=["Database API"])


