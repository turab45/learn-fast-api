from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from routes.users import user_router
from routes.events import events_router
import uvicorn
from database.connection import conn

app = FastAPI()


# register routes
app.include_router(user_router, prefix="/user")
app.include_router(events_router, prefix="/event")

@app.on_event("startup")
async def startup():
    conn()


@app.get("/")
async def root():
    # redirect to /event
    return RedirectResponse(url="/event/")

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True)

