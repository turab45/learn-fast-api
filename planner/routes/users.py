from fastapi import APIRouter, HTTPException, status
from models.users import User, UserSignIn

user_router = APIRouter(
    tags=["User"]
)

users = {}

@user_router.post("/signup")
async def sign_new_user(data: UserSignIn) -> dict:
    if data.email in users:
        raise HTTPException(
            status = status.HTTP_409_CONFLICT,
            detail= "User with the supplied username already exists."
        )
    users[data.email] = data
    return {
        "message" : "User registered successfully."
    }

@user_router.post("/signin")
async def sign_in_user(user: UserSignIn) -> dict:
    if user.email not in users:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail= "User does not exist."
        )
    if users[user.email].password != user.password:
        raise HTTPException(
            status_code = status.HTTP_403_FORBIDDEN,
            detail = "Invalid credentials."
        )
        
    return {
        "message" : "User signed in successfully."
    }
