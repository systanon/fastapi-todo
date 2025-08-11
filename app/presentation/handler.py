from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import Optional

from database import SessionLocal
from infrastructure.schema import TodoRead
from presentation.schema import TodoCreate, TodoUpdate
from infrastructure import repository

router = APIRouter(prefix="/todos", tags=["Todos"])

def getDB():
  db = SessionLocal()
  try:
    yield db
  finally:
    db.close() 

@router.post("/", response_model=TodoRead)
def create(todo: TodoCreate, db: Session = Depends(getDB)):
  return repository.createTodo(db, todo)

@router.get("/", response_model=list[TodoRead])
def getAll(skip: int = 0, limit: int = 10, search: Optional[str] = None,
    completed: Optional[bool] = None, db: Session = Depends(getDB)):
  return repository.getAll(db, skip=skip, limit=limit, search=search, completed=completed)

@router.get("/{todo_id}", response_model=TodoRead)
def read(todo_id: int, db: Session = Depends(getDB)):
    db_todo = repository.getOne(db, todo_id)
    if not db_todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return db_todo

@router.patch("/{todo_id}", response_model=TodoRead)
def update(todo_id: int, todo: TodoUpdate, db: Session = Depends(getDB)):
    db_todo = repository.updateTodo(db, todo_id, todo)
    if not db_todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return db_todo

@router.delete("/{todo_id}", status_code=204)
def delete(todo_id: int, db: Session = Depends(getDB)):
    success = repository.deleteTodo(db, todo_id)
    if not success:
        raise HTTPException(status_code=404, detail="Todo not found")