from typing import Optional
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.services.todo_service import TodoService
from app.config import SessionLocal
from pydantic import BaseModel

router = APIRouter()

#Define the structure of request body data (like in POST or PUT requests).
class TodoCreate(BaseModel):
    title: str
    description: str

class TodoPartialUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    is_completed: Optional[bool] = None

class TodoUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    is_completed: Optional[bool] = None


def get_db():
    db = SessionLocal() 
    try:
        yield db ##Inject db session into routes
    finally:
        db.close()

@router.get("/todos")
def get_todos(db: Session = Depends(get_db)):
    return TodoService(db).get_all_todos()

@router.get("/todos/{todo_id}")
def get_todo(todo_id: int, db: Session = Depends(get_db)):
    todo = TodoService(db).get_todo_by_id(todo_id)
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo

@router.post("/todos")
#inject a database session into your FastAPI routes or controller methods.
def create_todo(todo: TodoCreate, db: Session = Depends(get_db)):
    return TodoService(db).create_new_todo(todo.title, todo.description)

@router.patch("/todos/{todo_id}")
def patch_todo(todo_id: int, todo: TodoPartialUpdate, db: Session = Depends(get_db)):
    existing_todo = TodoService(db).get_todo_by_id(todo_id)
    if not existing_todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    if todo.title is not None:
        existing_todo.title = todo.title
    if todo.description is not None:
        existing_todo.description = todo.description
    if todo.is_completed is not None:
        existing_todo.is_completed = todo.is_completed
    return TodoService(db).update_existing_todo(todo_id, existing_todo.title, existing_todo.description, existing_todo.is_completed)

@router.delete("/todos/{todo_id}")
def delete_todo(todo_id: int, db: Session = Depends(get_db)):
    return TodoService(db).delete_todo_by_id(todo_id)

@router.put("/todos/{todo_id}")
def put_todo(todo_id: int, todo: TodoUpdate, db: Session = Depends(get_db)):
    existing_todo = TodoService(db).get_todo_by_id(todo_id)
    if not existing_todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    if todo.title:
        existing_todo.title = todo.title
    if todo.description:
        existing_todo.description = todo.description
    if todo.is_completed:
        existing_todo.is_completed = todo.is_completed
    return TodoService(db).update_existing_todo(todo_id, existing_todo.title, existing_todo.description, existing_todo.is_completed)
