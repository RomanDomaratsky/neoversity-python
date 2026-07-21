# Тема: Основи модуля datetime
# ---------------------------------

import datetime




# Отримання поточної дати й часу
now = datetime.datetime.now()
print(now)  # рік-місяць-день години:хвилини:секунди.мікросекунди

from datetime import datetime
# Об'єкт datetime також можна імпортувати напряму з модуля
current_datetime = datetime.now()

# Атрибути об'єкта datetime
print(current_datetime.year)
print(current_datetime.month)
print(current_datetime.day)
print(current_datetime.hour)
print(current_datetime.minute)
print(current_datetime.second)
print(current_datetime.microsecond)
print(current_datetime.tzinfo)  # None, якщо часова зона не вказана

# Отримання тільки дати або тільки часу
print(current_datetime.date())
print(current_datetime.time())

# datetime.combine - об'єднання окремих date і time в один datetime
import datetime as dt

date_part = dt.date(2023, 12, 14)
time_part = dt.time(12, 30, 15)
combined_datetime = dt.datetime.combine(date_part, time_part)
print(combined_datetime)  # 2023-12-14 12:30:15

# Створення datetime з конкретною датою (час за замовчуванням 00:00:00)
specific_date = dt.datetime(year=2020, month=1, day=7)
print(specific_date)  # 2020-01-07 00:00:00

# Створення datetime з конкретною датою і часом (іменовані параметри)
specific_datetime = dt.datetime(year=2020, month=1, day=7, hour=14, minute=30, second=15)
print(specific_datetime)  # 2020-01-07 14:30:15

# Той самий результат без іменованих параметрів (менш зрозуміло)
specific_datetime = dt.datetime(2020, 1, 7, 14, 30, 15)
print(specific_datetime)  # 2020-01-07 14:30:15
