from fastapi import APIRouter, Path, HTTPException, status, Request, Depends, Form
from model import Todo, TodoItems
from fastapi.templating import Jinja2Templates

todo_router = APIRouter()

todos_list = []

templates = Jinja2Templates(directory="templates/")

@todo_router.post("/todo")
async def add_todo(request: Request,  todo: Todo = Depends(Todo.as_form)):
    todo.id = len(todos_list) + 1
    todos_list.append(todo)
    return templates.TemplateResponse("todo.html",
    {
        "request": request,
        "todos": todos_list
    })

@todo_router.get("/todo", response_model=TodoItems)
async def get_todos(request: Request):
    return templates.TemplateResponse(
        "todo.html",
     {
        'request': request,
        'todos': todos_list,
     })


@todo_router.get("/todo/{id}", status_code=status.HTTP_200_OK)
async def get_todo(request: Request, id: int = Path(..., title="The id of the todo to retrieve.")):
    for todo in todos_list:
        if todo.id == id:
            return templates.TemplateResponse(
            "todo.html", {
                "request": request,
                "todo": todo
            })
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, 
        detail="Todo with supplied id does not exist.",
        )


@todo_router.put("/todo/{id}", status_code=status.HTTP_200_OK)
async def update_todo(request : Request, todo_data: Todo, id: int = Path(..., title="The id of the todo to update"))-> dict:
    for todo in todos_list:
        if todo.id == id:
            return template.TemplateResponse("todo.html",
                {
                    'request': request,
                    'todo': todo,
                })
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, 
        detail="Todo with supplied id does not exist.",
        )

@todo_router.delete("/todo/{id}", status_code=status.HTTP_200_OK)
async def delete_todo(id: int = Path(..., title="The id of the todo to delete")) -> dict:
    for todo in todos_list:
        if todo.id == id:
            todos_list.remove(todo)
            return {"message": "Todo deleted successfully"}
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, 
        detail="Todo with supplied id does not exist.",
        )