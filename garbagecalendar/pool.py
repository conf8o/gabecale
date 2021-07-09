from datetime import timedelta, date

from .sapporo import SapporoGarbageCalendar

class Pool:
    pool = {
        "sapporo": SapporoGarbageCalendar()
    }
    last_update_date = date.today()
    term = timedelta(days=21)

    @classmethod
    def calendar(cls, id) -> SapporoGarbageCalendar:
        return cls.pool[id]

    @classmethod
    def update(cls, id) -> None:
        cls.pool[id] = type(cls.pool[id])()
        cls.last_update_date = date.today()

    @classmethod
    def expired(cls) -> bool:
        return date.today() - cls.last_update_date >= cls.term
