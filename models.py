from sqlalchemy import Column, Integer, String, Text, DateTime
from database import Base
from datetime import datetime,timezone

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    content = Column(Text)
    created_at = Column(DateTime, default=datetime.now(timezone.utc))
    mode = Column(String, default='özet')