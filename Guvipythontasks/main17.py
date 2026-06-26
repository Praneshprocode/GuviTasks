#Extract year, month, and day from a datetime object
from datetime import datetime
dt = datetime(2026, 7, 15, 10, 30, 0)
extract_date = lambda d: (d.year, d.month, d.day)
print(extract_date(dt))
