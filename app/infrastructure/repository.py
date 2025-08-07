from sqlalchemy.orm import Session
from infrastructure.model import Todo
from infrastructure.schema import TodoCreate, TodoUpdate, TodoRead


def createTodo(db: Session, todo: TodoCreate) -> Todo:
  db_todo = Todo(**todo.dict())
  db.add(db_todo)
  db.commit()
  db.refresh(db_todo)
  return db_todo

def getAll(db: Session, skip: int = 0, limit: int = 10) -> Todo | None:
  return db.query(Todo).offset(skip).limit(limit).all()

def getOne(db: Session, todo_id: int) -> Todo | None:
    return db.query(Todo).filter(Todo.id == todo_id).first()


def updateTodo(db: Session, todo_id: int, data: TodoUpdate) -> Todo | None:
    db_todo = getOne(db, todo_id)
    if not db_todo:
        return None
    for field, value in data.model_dump(exclude_unset=True).items():
        setattr(db_todo, field, value)
    db.commit()
    db.refresh(db_todo)
    return db_todo


def deleteTodo(db: Session, todo_id: int) -> bool:
    db_todo = getOne(db, todo_id)
    if not db_todo:
        return False
    db.delete(db_todo)
    db.commit()
    return True