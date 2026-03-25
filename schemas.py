from pydantic import BaseModel
from datetime import datetime
from typing import Optional

# 1. Temel Şema (Ortak Alanlar)
class NoteBase(BaseModel):
    title: str
    content: str
    mode: str = "ozet"


class NoteCreate(NoteBase):
    pass


class Note(NoteBase):
    id: int

    analysis: Optional[str] = None

    class Config:
        from_attributes = True