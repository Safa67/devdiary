from sqlalchemy import Column, Integer, String, Text, DateTime
from database import Base
from datetime import datetime,timezone

class Note(Base):
    __tablename__ = "notes"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    content = Column(String)
    mode = Column(String, default="ozet")

    analysis = Column(String, nullable=True)
