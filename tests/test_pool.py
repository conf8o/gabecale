from datetime import date, timedelta
from garbagecalendar.sapporo import SapporoGarbageCalendar
from garbagecalendar.pool import Pool

def test_calendar():
    calendar = Pool.calendar("sapporo")
    assert type(calendar) is SapporoGarbageCalendar

def test_update():
    calendar = Pool.calendar("sapporo")
    not_updated = Pool.calendar("sapporo")
    assert not_updated is calendar

    Pool.update("sapporo")
    updated = Pool.calendar("sapporo")
    assert not_updated is not updated

def test_last_update_date():
    assert not Pool.expired()
    
    Pool.last_update_date = date.today() - timedelta(days=21)
    assert Pool.expired()