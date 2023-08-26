from fastapi import FastAPI
from enum import Enum
from constants import random_event_names
from pydantic import BaseModel


class EventModel(str, Enum):
    event_url = "sls"
    event_name = "The Serverless in 2023"


class EventDetails(BaseModel):
    name: str
    slug_url: str
    number_of_participants: int | None = None
    number_of_speakers: int | None = None
    venue: str | None = None
    online: bool = False
    is_free: bool = False

app = FastAPI()


@app.get("/event/me")
async def get_user():
    return {"name": "Tahir"}


@app.get("/event/names")
async def get_event_names(limit: int = 10, offset: int = 0):
    return {
        "event_names": random_event_names[offset:limit],
        "count": len(random_event_names),
    }


@app.get("/event/{event_url}")
async def welcome_user(event_url: EventModel, name: bool = False):
    res = {"event_url": EventModel.event_url}
    if name:
        res["event_name"] = EventModel.event_name
    return res


@app.get("/event/needy/{event_url}")
async def read_user_item(event_url: str, needy: str):
    return {"event_url": EventModel.event_url, "needy": needy}


@app.post("/event")
async def create_event(request: EventDetails) -> dict:
    return {"event": request, "message": "Event created"}
