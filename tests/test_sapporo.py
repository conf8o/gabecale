from datetime import date
import pandas as pd

from garbagecalendar.sapporo import SAPPORO_GARBAGE_TYPE, SapporoGarbageCalendar


def test_init():
    calendar = SapporoGarbageCalendar()
    assert 365 == len(calendar.csv)

def test_index():
    calendar = SapporoGarbageCalendar()
    d = date.today()
    t = calendar[d].row["豊平区②"]

    if pd.isna(t):
        print("NaN test")
    else:
        print(t)
        print(SAPPORO_GARBAGE_TYPE[t])
        assert SAPPORO_GARBAGE_TYPE[t]

