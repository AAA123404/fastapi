
from sqlalchemy import select, func, update
from sqlalchemy.ext.asyncio import AsyncSession
from models.news import News

async def get_news_list(db:AsyncSession,skip: int = 0 ,limit: int = 100):# 默认要放到非默认后面
    stmt = select(News).offset(skip).limit(limit)
    result = await db.execute(stmt)
    return result.scalars().all()

from models.news import News
from sqlalchemy.ext.asyncio import AsyncSession

async def create_news(db: AsyncSession, news_data):
    new_news = News(
        title=news_data.title,
        content=news_data.content,
        publish_date=news_data.publish_date
    )
    db.add(new_news)
    await db.commit()
    await db.refresh(new_news)
    return new_news