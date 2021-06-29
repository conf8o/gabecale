from datetime import date
from typing import Optional

from fastapi import FastAPI

from garbagecalendar.sapporo import SapporoGarbageCalendar, SAPPORO_GARBAGE_TYPE


app = FastAPI()

@app.get("/sapporo/type")
async def sapporo_type():
    return SAPPORO_GARBAGE_TYPE

@app.get("/sapporo/today")
async def sapporo_today(location: Optional[str]=None):
    today = date.today()
    sapporo_garbage_calendar = SapporoGarbageCalendar()
    sapporo_today_garbage: SapporoGarbageCalendar.Row = sapporo_garbage_calendar[date.today()]

    if location is None:
        return sapporo_today_garbage.row
    else:
        return {"date": today,
                "day": sapporo_today_garbage["曜日"],
                "location": location,
                "type": sapporo_today_garbage[location]}

