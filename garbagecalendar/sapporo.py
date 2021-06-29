from datetime import date
import pandas as pd

from .utils import date_str

CSV_URL = "https://ckan.pf-sapporo.jp/dataset/281fc9c2-7ca5-4aed-a728-0b588e509686/resource/3e7862c1-c9df-4b21-b6cf-aca9b89e60c6/download/garvagecollectioncalendar202010.csv"

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
            return SAPPORO_GARBAGE_TYPE[self.row[area]]

        def __str__(self):
            return str(self.row)
    
    def __init__(self):
        self.csv = pd.read_csv(CSV_URL, dtype=str).set_index("日付")

    def __getitem__(self, d: date) -> Row:
        d = date_str(d)
        return SapporoGarbageCalendar.Row(self.csv.loc[d, :])
