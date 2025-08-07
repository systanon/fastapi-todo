from pydantic import BaseModel
from datetime import datetime


class TodoCreate(BaseModel):
  title: str
  description: str



class TodoUodate(BaseModel):
  title: str | None = None
  description: str | None = None
  completed: bool | None = None

class TodoRead(BaseModel):
  id: int
  title: str
  description: str
  completed: bool
  created_at: datetime
  updated_at: datetime

  class Config:
      orm_mode = True  