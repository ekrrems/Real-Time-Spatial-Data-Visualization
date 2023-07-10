from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime

app = FastAPI()

class LocationRequest(BaseModel):
    name: str
    location: str


@app.get("/")
def index():
    return {"message": "Hello This is Real Time Spatial Data API"}

@app.post("/send-location")
def send_location(location:LocationRequest):
    name = location.name
    loc = location.location
    now = datetime.now()
    date = now.date()
    hour = now.time().hour
    minute = now.time().minute

    return {"message": f"Location Received! ({date}, {hour}:{minute})", 
            "name": str(name),
            "location": str(loc),
            "date": str(date)}
