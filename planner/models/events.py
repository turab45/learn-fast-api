from pydantic import BaseModel
from typing import Optional, List

class Event(BaseModel):
    id : int
    title : str
    image : str
    description : str
    tags : List[str]
    location : str


    class Config:
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