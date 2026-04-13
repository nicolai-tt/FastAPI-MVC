from sqlmodel import SQLModel


class TodoResponse(SQLModel):
    id: int
    title: str
    completed: bool