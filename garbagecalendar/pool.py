from datetime import timedelta, date

from .sapporo import SapporoGarbageCalendar

class Pool:
    __pool = {
        "sapporo": SapporoGarbageCalendar()
    }
    __last_update_date = date.today()
    __term = timedelta(days=21)

    @classmethod
    def calendar(cls, id):
        return cls.__pool[id]

    @classmethod
    def update(cls, id):
        cls.__pool[id] = type(cls.__pool[id])()
        cls.__last_update_date = date.today()

    @classmethod
    def expired(cls):
        return cls.__last_update_date is None or date.today() - cls.__last_update_date > cls.__term
