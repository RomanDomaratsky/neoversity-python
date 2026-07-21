# Тема: weekday() та порівняння об'єктів datetime
# ------------------------------------------------------

from datetime import datetime

# weekday() - номер дня тижня: понеділок = 0, неділя = 6
now = datetime.now()
day_of_week = now.weekday()
print(f"Сьогодні: {day_of_week}")

# Порівняння двох об'єктів datetime стандартними операторами
datetime1 = datetime(2023, 3, 14, 12, 0)
datetime2 = datetime(2023, 3, 15, 12, 0)

print(datetime1 == datetime2)  # False, дати не однакові
print(datetime1 != datetime2)  # True, дати різні
print(datetime1 < datetime2)   # True, datetime1 передує datetime2
print(datetime1 > datetime2)   # False, datetime1 не наступає за datetime2
