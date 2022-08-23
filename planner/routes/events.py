from fastapi import APIRouter, HTTPException, status, Body, Depends
from typing import List
from models.events import Event, EventUpdate
from database.connection import get_session

events_router = APIRouter(
    tags=["Events"]
)

@events_router.get("/", response_model=List[Event])
async def get_events(session=Depends(get_session)) -> List[Event]:
    events = session.query(Event).all()
    return events

@events_router.get("/{id}", response_model=Event)
async def get_event(id: int, session=Depends(get_session)) -> Event:
    event = session.get(Event,id)
    if not event:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = "Event with supplied id does not exist."
        )
    return event

@events_router.post("/new")
async def create_event(new_event: Event, session=Depends(get_session)) -> dict:
    session.add(new_event)
    session.commit()
    session.refresh(new_event)
    return {
        "message" : "Event created successfully."
    }

@events_router.put("/{id}", response_model=Event)
async def update_event(id: int, new_event: EventUpdate, session=Depends(get_session)) -> dict:
    event = session.get(Event,id)
    if event:
        event.title = new_event.title
        event.description = new_event.description
        event.image = new_event.image
        event.tags = new_event.tags
        event.location = new_event.location
        
        session.add(event)
        session.commit()
        session.refresh(event)
        return event

    raise HTTPException(
        status_code = status.HTTP_404_NOT_FOUND,
        detail = "Event with supplied ID does not exist."
    )

@events_router.delete("/{id}")
async def delete_event(id: int, session=Depends(get_session)) -> dict:
    event = session.get(Event,id)
    if event:
        session.delete(event)
        session.commit()
        return {
        "message" : "Event deleted successfully."
    }
    
    raise HTTPException(
        status_code = status.HTTP_404_NOT_FOUND,
        detail = "Event with supplied ID does not exist."
    )

@events_router.delete("/")
async def delete_all_events() -> dict:
    events.clear()
    return {
        "message" : "All events deleted successfully."
    }