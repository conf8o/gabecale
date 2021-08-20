import bs4
from datetime import date
import pandas as pd
import requests

from .utils import date_str

BASE_SOUP = bs4.BeautifulSoup(
    requests.get("https://ckan.pf-sapporo.jp/dataset/garbage_collection_calendar").text,
    "lxml"
)

RESOURCES = BASE_SOUP.find_all("li", class_="resource-item")

def calendar_url() -> str:
    last_resource: bs4.element.Tag = RESOURCES[-1]
    download_url = last_resource.find("a", class_="resource-url-analytics")["href"]
    
    return download_url

CALENDAR_URL = calendar_url()

def garbase_type_url() -> str:
    first_resource: bs4.element.Tag = RESOURCES[0]
    download_url = first_resource.find("a", class_="resource-url-analytics")["href"]

    return download_url

SAPPORO_GARBAGE_TYPE = pd.read_csv(garbase_type_url(), dtype=str).set_index("記号").to_dict()["ごみ種"]

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
