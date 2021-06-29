from datetime import date

from garbagecalendar.utils import *

def test_date_str():
    expect = "2021-6-29"
    d = date(2021, 6, 29)
    assert expect == date_str(d)