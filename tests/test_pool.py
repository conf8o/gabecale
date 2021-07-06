from garbagecalendar.sapporo import SapporoGarbageCalendar
from garbagecalendar.pool import Pool

def test_calendar():
    calendar = Pool.calendar("sapporo")
    assert type(calendar) is SapporoGarbageCalendar
