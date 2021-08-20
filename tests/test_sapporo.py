from datetime import date
import pandas as pd

from garbagecalendar.sapporo import SapporoGarbageCalendar, search_resource_url


def test_search_resouce_urls():
    url = search_resource_url()
    assert url.garbage_type is not None
    assert url.last_calendar is not None

def test_init():
    calendar = SapporoGarbageCalendar()
    assert 365 == len(calendar.calendar)

def test_index():
    calendar = SapporoGarbageCalendar()
    d = date.today()
    r = calendar[d]

    if pd.isna(r):
        print("NaN test")
    else:
        t = r["中央区②"]
        print(t)
        assert t is not None

