from datetime import date
from typing import Optional

from fastapi import FastAPI

from garbagecalendar.sapporo import SapporoGarbageCalendar


app = FastAPI()

@app.get("/sapporo")
async def sapporo(location: Optional[str]=None):
    sapporo_garbage_calendar = SapporoGarbageCalendar()
    sapporo_today_garbage: SapporoGarbageCalendar.Row = sapporo_garbage_calendar[date.today()]
    return {"location": location,
            "type": sapporo_today_garbage[location]}

