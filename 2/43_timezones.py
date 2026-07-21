# Тема: Робота з часовими зонами (timezone)
# --------------------------------------------

from datetime import datetime, timezone, timedelta

# Поточний локальний час vs поточний час у UTC
local_now = datetime.now()
utc_now = datetime.now(timezone.utc)
print(local_now)
print(utc_now)

# Перетворення UTC в інший часовий пояс (наприклад, UTC-5, східний час США)
utc_time = datetime.now(timezone.utc)
eastern_time = utc_time.astimezone(timezone(timedelta(hours=-5)))
print(eastern_time)

# Перетворення локального часу (з відомою часовою зоною) у UTC
local_timezone = timezone(timedelta(hours=2))  # напр. UTC+2 (Київ)
local_time = datetime(year=2023, month=3, day=14, hour=12, minute=30, second=0, tzinfo=local_timezone)
utc_time = local_time.astimezone(timezone.utc)
print(utc_time)  # 2023-03-14 10:30:00+00:00

# ISO 8601 формат разом з часовою зоною
timezone_offset = timezone(timedelta(hours=2))  # UTC+2
timezone_datetime = datetime(year=2023, month=3, day=14, hour=12, minute=30, second=0, tzinfo=timezone_offset)
iso_format_with_timezone = timezone_datetime.isoformat()
print(iso_format_with_timezone)  # 2023-03-14T12:30:00+02:00
