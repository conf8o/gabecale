import bs4
from datetime import date
import pandas as pd
import requests

from .utils import date_str


def csv_url() -> str:
    soup = bs4.BeautifulSoup(
        requests.get("https://ckan.pf-sapporo.jp/dataset/garbage_collection_calendar").text,
        "lxml"
    )
    last_resource: bs4.element.Tag = soup.find_all("li", class_="resource-item")[-1]
    download_url = last_resource.find("a", class_="resource-url-analytics")["href"]
    
    return download_url

CSV_URL = csv_url()

SAPPORO_GARBAGE_TYPE = {
    "1": "燃やせるゴミ",
    "2": "燃やせないゴミ",
    "8": "びん・缶・ペット",
    "9": "容器プラ",
    "10": "雑がみ",
    "11": "枝・葉・草"
}

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
        self.csv = pd.read_csv(CSV_URL, dtype=str).set_index("日付")

    def __getitem__(self, d: date) -> Row:
        d = date_str(d)
        return SapporoGarbageCalendar.Row(self.csv.loc[d, :])
