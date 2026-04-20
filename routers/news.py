# 导入APIRouter
from fastapi import APIRouter, Depends, Query, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from crud.new import get_news_list,create_news
from config.db_config import get_db
from schemas.news import NewsCreate

#创建APIRouter实例 前缀为/api/news 具体在API文档中
router = APIRouter(prefix="/api/news", tags=["news"])
# 路由
@router.get("/") # 获取新闻分类
async def get_news(skip: int = 0, limit: int = 100,db: AsyncSession = Depends(get_db)): # 依赖注入config中的session
    # 获取数据库里面的新闻分类数据，先定义模型类，封装查询数据的方法，再在这里调用
    categories = await get_news_list(db, skip, limit)
    return {
        "code": 200,
        "message": "success",
        "data": categories,
    }

@router.post("/")
async def add_news(
    news: NewsCreate,
    db: AsyncSession = Depends(get_db)
):
    new_news = await create_news(db, news)

    return {
        "code": 200,
        "message": "created",
        "data": {
            "id": new_news.id,
            "title": new_news.title
        }
    }