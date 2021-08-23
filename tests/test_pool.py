from datetime import date, timedelta
from garbagecalendar.sapporo import SapporoGarbageCalendar
from garbagecalendar.pool import Pool

pool = Pool.instance()

def test_calendar():
    calendar = pool.calendar("sapporo")
    assert type(calendar) is SapporoGarbageCalendar

def test_update():
    calendar = pool.calendar("sapporo")
    not_updated = pool.calendar("sapporo")
    assert not_updated is calendar

    pool.reset("sapporo")
    updated = pool.calendar("sapporo")
    assert not_updated is not updated

def test_last_reset_date():
    assert not pool.expired("sapporo")
    
    pool.last_reset_date["sapporo"] = date.today() - timedelta(days=21)
    assert pool.expired("sapporo")