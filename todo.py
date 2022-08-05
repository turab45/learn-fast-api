from fastapi import APIRouter, Path
from model import Todo

app = APIRouter()

todos_list = []

@app.post("/todo")
async def add_todo(todo: Todo) -> dict:
    todos_list.append(todo)
    return {"message": "Todo created successfully"}

@app.get("/todo")
async def get_todos() -> dict:
    return {"todos": todos_list}


@app.get("/todo/{id}")
async def get_todo(id: int = Path(..., title="The id of the todo to retrieve.")) -> dict:
    for todo in todos_list:
        if todo.id == id:
            return {"todo": todo}
    return {"message": "Todo with supplied id does not exist."}

@app.put("/todo/{id}")
async def update_todo(todo_data: Todo, id: int = Path(..., title="The id of the todo to update"))-> dict:
    for todo in todos_list:
        if todo.id == id:
            todo.item = todo_data.item
            todo.status = todo_data.status
            return {"message": "Todo updated successfully"}
    return {"message": "Todo with supplied id does not exist."}

