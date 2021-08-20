from datetime import date
import pandas as pd

from garbagecalendar.sapporo import SapporoGarbageCalendar, resource_urls


def test_resouce_urls():
    urls = resource_urls()
    assert 2 == len(urls)
    assert all(type(url) == str for url in urls)

def test_init():
    calendar = SapporoGarbageCalendar()
    assert 365 == len(calendar.csv)

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

