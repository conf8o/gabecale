import bs4
from dataclasses import dataclass
from datetime import date
import pandas as pd
import requests
from .utils import date_str


@dataclass
class ResourceUrl:
    garbage_type: str
    last_calendar: str

def search_resource_url() -> ResourceUrl:
    soup = bs4.BeautifulSoup(
        requests.get("https://ckan.pf-sapporo.jp/dataset/garbage_collection_calendar").text,
        "lxml"
    )

    resources = soup.find_all("li", class_="resource-item")

    garbage_type, last_calendar = [
        resource.find("a", class_="resource-url-analytics")["href"]
        for resource
        in [resources[0], resources[-1]]
    ]
    return ResourceUrl(garbage_type, last_calendar)

class SapporoGarbageCalendar:
    class Row:
        def __init__(self, garbage_type: dict[str, str], row: pd.Series) -> None:
            self.garbage_type = garbage_type
            self.row = row

        def __getitem__(self, area: str) -> str:
            item = self.row[area]
            return self.garbage_type.get(item, item)

        def __str__(self) -> str:
            return str(self.row)
    
    def __init__(self) -> None:
        url = search_resource_url()
        self.garbage_type = pd.read_csv(url.garbage_type, dtype=str).set_index("記号").to_dict()["ごみ種"]
        self.calendar = pd.read_csv(url.last_calendar, dtype=str).set_index("日付")

    def __getitem__(self, d: date) -> Row:
        d = date_str(d)
        return SapporoGarbageCalendar.Row(self.garbage_type, self.calendar.loc[d, :])

