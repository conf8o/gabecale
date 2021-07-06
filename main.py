from datetime import date
from typing import Optional

from fastapi import FastAPI

from garbagecalendar.pool import Pool


app = FastAPI()

@app.get("/{id}/today")
async def sapporo_today(id: str, location: Optional[str]=None):
    if Pool.expired:
        Pool.update(id)

    calendar = Pool.calendar(id)
    today_garbage = calendar[date.today()]

    if location is None:
        return today_garbage.row
    else:
        return {"曜日": today_garbage["曜日"],
                location : today_garbage[location]}

