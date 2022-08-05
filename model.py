from pydantic import BaseModel


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
    id : int
    item : Item

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
