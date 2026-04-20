from pydantic import BaseModel
from datetime import date

class NewsCreate(BaseModel):
    title: str
    content: str
    publish_date: date