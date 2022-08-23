from sqlmodel import SQLModel, JSON, Field, Column
from typing import Optional, List

class Event(SQLModel, table=True):
    id : int = Field(default=None, primary_key=True)
    title : str
    image : str
    description : str
    tags : List[str] = Field(sa_column = Column(JSON))
    location : str


    class Config:
        arbitary_types_are_allowed = True
        schema_extra = {
            "example" : {
                "id" : 1,
                "title" : "Some Event",
                "image" : "https://linktomyimage.com/image.png",
                "description" : "Description of the event.",
                "tags" : ["event", "planner"],
                "location" : "Zoom"
            }
        }

class EventUpdate(SQLModel):
    title : Optional[str]
    image : Optional[str]
    description : Optional[str]
    tags : Optional[List[str]]
    location : Optional[str]

    class Config:
        schema_extra = {
            "example" : {
                "title" : "Some Event",
                "image" : "https://linktomyimage.com/image.png",
                "description" : "Description of the event.",
                "tags" : ["event", "planner"],
                "location" : "Zoom"
            }
        }