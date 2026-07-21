# Тема: Робота з ISO 8601 форматом дати
# --------------------------------------------
# Формат: "YYYY-MM-DDTHH:MM:SS", де T розділяє дату і час.

from datetime import datetime

# isoformat() - конвертація datetime у рядок ISO 8601
now = datetime.now()
iso_format = now.isoformat()
print(iso_format)  # напр. 2023-12-14T15:43:42.651309

# fromisoformat() - конвертація рядка ISO 8601 у datetime
iso_date_string = "2023-03-14T12:39:29.992996"
date_from_iso = datetime.fromisoformat(iso_date_string)
print(date_from_iso)  # 2023-03-14 12:39:29.992996

# isoweekday() - день тижня за ISO 8601: понеділок = 1, неділя = 7
now = datetime.now()
day_of_week = now.isoweekday()
print(f"Сьогодні: {day_of_week}")

# isocalendar() - кортеж (ISO_рік, ISO_тиждень, ISO_день_тижня)
now = datetime.now()
iso_calendar = now.isocalendar()
print(f"ISO рік: {iso_calendar[0]}, ISO тиждень: {iso_calendar[1]}, ISO день тижня: {iso_calendar[2]}")
