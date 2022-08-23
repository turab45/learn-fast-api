from fastapi import Form
from pydantic import BaseModel
from typing import List, Optional

class Item(BaseModel):
    item : str
    status : str

    class Config:
        schema_extra = {
            "example": {
                "item": "test",
                "status": "done"
            }
        }

        
class Todo(BaseModel):
    id : Optional[int]
    item : str

    @classmethod
    def as_form(
        cls,
        item: str = Form(...),
    ):
        return cls(item=item)

    class Config:
        schema_extra = {
            "example": {
                "id": 1,
                "item": {
                    "item": "Buy milk",
                    "status": "active"
                }
            }
        }

class TodoItems(BaseModel):
    todos : List[Todo]

    class Config:
        schema_extra = {
            "example": {
                "todos": [
                    {
                        "item": "example schema 1",

                    },
                    {
                        "item": "example schema 2",
                    }
                ]
            }
        }