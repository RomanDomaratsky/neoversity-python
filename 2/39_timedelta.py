# Тема: Робота з часовими проміжками timedelta
# ---------------------------------------------------

from datetime import timedelta, datetime

# Створення timedelta з декількох одиниць часу
delta = timedelta(
    days=50,
    seconds=27,
    microseconds=10,
    milliseconds=29000,
    minutes=5,
    hours=8,
    weeks=2
)
print(delta)  # 64 days, 8:05:56.000010

# Різниця між двома datetime дає об'єкт timedelta
seventh_day_2019 = datetime(year=2019, month=1, day=7, hour=14)
seventh_day_2020 = datetime(year=2020, month=1, day=7, hour=14)

difference = seventh_day_2020 - seventh_day_2019
print(difference)                  # 365 days, 0:00:00
print(difference.total_seconds())  # 31536000.0

# Додавання timedelta до поточної дати
now = datetime.now()
future_date = now + timedelta(days=10)
print(future_date)

# Додавання/віднімання timedelta від конкретної дати
seventh_day_2020 = datetime(year=2020, month=1, day=7, hour=14)
four_weeks_interval = timedelta(weeks=4)

print(seventh_day_2020 + four_weeks_interval)  # 2020-02-04 14:00:00
print(seventh_day_2020 - four_weeks_interval)  # 2019-12-10 14:00:00

# toordinal() - порядковий номер дня з 1 січня року 1 н.е.
date = datetime(year=2023, month=12, day=18)
ordinal_number = date.toordinal()
print(f"Порядковий номер дати {date} становить {ordinal_number}")

# Приклад: скільки днів минуло від 14 вересня 1812 року (спалення Москви)
napoleon_burns_moscow = datetime(year=1812, month=9, day=14)
current_date = datetime.now()
days_since = current_date.toordinal() - napoleon_burns_moscow.toordinal()
print(days_since)
