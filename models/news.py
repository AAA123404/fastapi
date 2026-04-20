from datetime import datetime, date
from sqlalchemy import DateTime, func, Integer, String, Text, Date
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class News(Base):
    __tablename__ = "news_data"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True,
        comment="ID"
    )

    title: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
        comment="標題"
    )

    content: Mapped[str] = mapped_column(
        Text,
        nullable=False,
        comment="內容"
    )

    publish_date: Mapped[date] = mapped_column(
        Date,
        nullable=False,
        comment="發布日期"
    )

    def __repr__(self):
        return f"<News(id={self.id}, title={self.title})>"
    

