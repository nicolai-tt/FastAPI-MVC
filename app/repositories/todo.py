from sqlmodel import Session, select
from app.models.todo import Todo


class TodoRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_todos_by_user(self, user_id: int) -> list[Todo]:
        return self.db.exec(select(Todo).where(Todo.user_id == user_id)).all()