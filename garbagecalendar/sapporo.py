import bs4
from datetime import date
import pandas as pd
import requests

from .utils import date_str


def resource_urls() -> tuple[str, str]:
    soup = bs4.BeautifulSoup(
        requests.get("https://ckan.pf-sapporo.jp/dataset/garbage_collection_calendar").text,
        "lxml"
    )

    resources = soup.find_all("li", class_="resource-item")

    garbase_type = resources[0]
    last_calendar = resources[-1]

    return tuple(resource.find("a", class_="resource-url-analytics")["href"] for resource in [garbase_type, last_calendar])

GARBAGE_TYPE_URL, CALENDAR_URL = resource_urls()

SAPPORO_GARBAGE_TYPE = pd.read_csv(GARBAGE_TYPE_URL, dtype=str).set_index("記号").to_dict()["ごみ種"]

class SapporoGarbageCalendar:
    class Row:
        def __init__(self, row: pd.Series):
            self.row = row

        def __getitem__(self, area: str) -> str:
            item = self.row[area]
            return SAPPORO_GARBAGE_TYPE.get(item, item)

        def __str__(self):
            return str(self.row)
    
    def __init__(self):
        self.csv = pd.read_csv(CALENDAR_URL, dtype=str).set_index("日付")

    def __getitem__(self, d: date) -> Row:
        d = date_str(d)
        return SapporoGarbageCalendar.Row(self.csv.loc[d, :])
