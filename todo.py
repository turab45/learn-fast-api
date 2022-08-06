from fastapi import APIRouter, Path, HTTPException, status
from model import Todo, TodoItems

app = APIRouter()

todos_list = []

@app.post("/todo", status_code=status.HTTP_201_CREATED)
async def add_todo(todo: Todo) -> dict:
    todos_list.append(todo)
    return {"message": "Todo created successfully"}

@app.get("/todo", response_model=TodoItems, status_code=status.HTTP_200_OK)
async def get_todos() -> dict:
    return {"todos": todos_list}


@app.get("/todo/{id}", status_code=status.HTTP_200_OK)
async def get_todo(id: int = Path(..., title="The id of the todo to retrieve.")) -> dict:
    for todo in todos_list:
        if todo.id == id:
            return {"todo": todo}
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, 
        detail="Todo with supplied id does not exist.",
        )


@app.put("/todo/{id}", status_code=status.HTTP_200_OK)
async def update_todo(todo_data: Todo, id: int = Path(..., title="The id of the todo to update"))-> dict:
    for todo in todos_list:
        if todo.id == id:
            todo.item.item = todo_data.item.item
            todo.item.status = todo_data.item.status
            return {"message": "Todo updated successfully"}
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, 
        detail="Todo with supplied id does not exist.",
        )

@app.delete("/todo/{id}", status_code=status.HTTP_200_OK)
async def delete_todo(id: int = Path(..., title="The id of the todo to delete")) -> dict:
    for todo in todos_list:
        if todo.id == id:
            todos_list.remove(todo)
            return {"message": "Todo deleted successfully"}
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, 
        detail="Todo with supplied id does not exist.",
        )