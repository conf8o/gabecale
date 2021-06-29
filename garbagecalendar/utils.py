from datetime import date

def date_str(d: date) -> str:
    return f"{d.year}-{d.month}-{d.day}"