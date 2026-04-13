from app.repositories.todo import TodoRepository


class TodoService:
    def __init__(self, todo_repo: TodoRepository):
        self.todo_repo = todo_repo

    def get_user_todos(self, user_id: int):
        return self.todo_repo.get_todos_by_user(user_id)