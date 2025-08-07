from sqlalchemy import Column, Integer, String, Boolean, DateTime
from datetime import datetime, timezone
from database import Base


class Todo(Base):
  __tablename__ = "todos"

  id = Column(Integer, primary_key=True, index=True)
  title = Column(String, index=True)
  description = Column(String, index=True)
  completed = Column(Boolean, index=True, default=False)
  created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
  updated_at = Column(DateTime, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))