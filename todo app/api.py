from fastapi import FastAPI
from fastapi import APIRouter
from todo import todo_router

router = APIRouter()

app = FastAPI()

# @app.get("/")
# async def welcome() -> dict:
#     return {"message": "Welcome to the API"}


@router.get("/hello")
async def say_hello() -> dict:
    return {"message": "Welcome to the APIRouter app route."}


app.include_router(todo_router)