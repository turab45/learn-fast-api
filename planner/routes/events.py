from fastapi import APIRouter, HTTPException, status, Body
from typing import List
from models.events import Event

events_router = APIRouter(
    tags=["Events"]
)

events = []

@events_router.get("/", response_model=List[Event])
async def get_events() -> List[Event]:
    return events

@events_router.get("/{id}", response_model=Event)
async def get_event(id: int) -> Event:
    event = [event for event in events if event.id == id]
    if not event:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = "Event with supplied id does not exist."
        )
    return event[0]

@events_router.post("/new")
async def create_event(body: Event = Body(...)) -> dict:
    events.append(body)
    return {
        "message" : "Event created successfully."
    }

@events_router.put("/{id}")
async def update_event(id: int, body: Event = Body(...)) -> dict:
    for event in events:
        if event.id == id:
            event = body
            return {
        "message" : "Event updated successfully."
    }

    raise HTTPException(
        status_code = status.HTTP_404_NOT_FOUND,
        detail = "Event with supplied id does not exist."
    )

@events_router.delete("/{id}")
async def delete_event(id: int) -> dict:
    event = [event for event in events if event.id == id]
    if not event:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = "Event with supplied id does not exist."
        )
    events.remove(event[0])
    return {
        "message" : "Event deleted successfully."
    }

@events_router.delete("/")
async def delete_all_events() -> dict:
    events.clear()
    return {
        "message" : "All events deleted successfully."
    }