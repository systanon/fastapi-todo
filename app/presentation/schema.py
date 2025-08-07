from pydantic import BaseModel
from datetime import datetime


class TodoCreate(BaseModel):
  title: str
  description: str



class TodoUpdate(BaseModel):
  title: str | None = None
  description: str | None = None
  completed: bool | None = None

class Todo(BaseModel):
  id: int
  title: str
  description: str
  completed: bool
  created_at: datetime
  updated_at: datetime 