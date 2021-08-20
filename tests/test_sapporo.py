from datetime import date
import pandas as pd

from garbagecalendar.sapporo import SapporoGarbageCalendar, calendar_url, garbase_type_url


def test_csv_url():
    assert calendar_url() is not None

def test_garbage_type():
    assert garbase_type_url is not None

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

