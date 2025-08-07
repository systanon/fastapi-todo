from fastapi import FastAPI
from database import engine
from app.infrastructure import model  as todo_model
from app.presentation import handler as todo_handler


todo_model.Base.metadata.create_all(bind=engine)


app = FastAPI()

app.include_router(todo_handler.router)