from sqlalchemy.orm import Session
from app.infrastructure.model import Todo
from app.infrastructure.schema import TodoCreate, TodoUodate, TodoRead


def createTodo(db: Session, todo: TodoCreate) -> Todo:
  db_todo = Todo(**todo.dict())
  db.add(db_todo)
  db.commit()
  db.refresh(db_todo)
  return db_todo

def getAll(db: Session, skip: int = 0, limit: int = 10) -> Todo | None:
  return db.query(Todo).offset(skip).limit(limit).all()