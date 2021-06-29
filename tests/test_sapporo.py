from datetime import date
import pandas as pd

from garbagecalendar.sapporo import SapporoGarbageCalendar


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
        t = r["豊平区②"]
        print(t)
        assert t is not None

