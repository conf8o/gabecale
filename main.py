from datetime import date
from typing import Optional

from fastapi import FastAPI

from garbagecalendar.pool import Pool


app = FastAPI()
pool = Pool.instance()

@app.get("/{id}/today")
async def today(id: str, location: Optional[str]=None):
    if pool.expired():
        pool.reset(id)

    calendar = pool.calendar(id)
    today_garbage = calendar[date.today()]

    if location is None:
        return today_garbage.row
    else:
        return {"曜日": today_garbage["曜日"],
                location : today_garbage[location]}

