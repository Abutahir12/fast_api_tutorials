from fastapi import FastAPI
from enum import Enum
from constants import random_event_names


class EventModel(str, Enum):
    event_url = "sls"
    event_name = "The Serverless in 2023"


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
