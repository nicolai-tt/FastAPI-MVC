from fastapi import Request
from app.dependencies import SessionDep
from app.dependencies.auth import AuthDep
from . import api_router
from app.services.todo_service import TodoService
from app.repositories.todo import TodoRepository
from app.schemas.todo import TodoResponse


@api_router.get("/todos", response_model=list[TodoResponse])
async def list_todos(request: Request, db: SessionDep, user: AuthDep):
    todo_repo = TodoRepository(db)
    todo_service = TodoService(todo_repo)
    return todo_service.get_user_todos(user.id)