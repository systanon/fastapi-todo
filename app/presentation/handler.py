from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import SessionLocal
from infrastructure.schema import TodoRead
from presentation.schema import TodoCreate, Todo
from infrastructure import repository as repository

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
def getAll(skip: int = 0, limit: int = 10, db: Session = Depends(getDB)):
  return repository.getAll(db, skip=skip, limit=limit)