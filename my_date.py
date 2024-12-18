from datetime import datetime
from re import search

def get_date(datetime_original):
    return datetime.strptime(search("\\d{4}:\\d{2}:\\d{2}", datetime_original).group(), "%Y:%m:%d").date()