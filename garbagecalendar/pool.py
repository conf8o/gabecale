from datetime import timedelta, date
from typing import TypeVar, Optional
from .sapporo import SapporoGarbageCalendar

Calendar = TypeVar("Calendar")

class Pool:
    RESET_TERM = timedelta(days=21)
    __instance: Optional['Pool'] = None

    @classmethod
    def instance(cls) -> 'Pool':
        if cls.__instance is None:
            cls.__instance = Pool()
        
        return cls.__instance
    
    def __init__(self) -> None:
        self.pool: dict[str, Calendar] = {
            "sapporo": SapporoGarbageCalendar()
        }
        self.last_reset_date: dict[str, date] = {
            id: date.today()
            for id
            in self.pool.keys()
        }

    def calendar(self, id) -> Calendar:
        return self.pool[id]

    def reset(self, id) -> None:
        self.pool[id] = type(self.pool[id])()
        self.last_reset_date[id] = date.today()

    def expired(self, id) -> bool:
        return date.today() - self.last_reset_date[id] >= Pool.RESET_TERM

