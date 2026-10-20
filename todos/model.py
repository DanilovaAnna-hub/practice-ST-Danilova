from typing import List, Optional
from pydantic import BaseModel, ConfigDict
from fastapi import Form

class Todo(BaseModel):
    id: Optional[int] = None
    item: str

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "id": 1,
                "item": "Example schema!"
            }
        }
    )

    @classmethod
    def as_form(cls, item: str = Form(...)):
        return cls(item=item)

class TodoItem(BaseModel):
    item: str

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "item": "Прочитать следующую главу книги"
            }
        }
    )

class TodoItems(BaseModel):
    todos: List[TodoItem]

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "todos": [
                    {"item": "Первая задача"},
                    {"item": "Вторая задача"}
                ]
            }
        }
    )
