from fastapi import FastAPI

from routers import  news
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
# CORS 設定
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 開發階段可用 *，正式環境要限制
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.get("/")
async def root():
    return {"message": "Hello World"}

app.include_router(news.router)