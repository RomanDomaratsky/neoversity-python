# Тема: Робота з timestamp (часова мітка)
# --------------------------------------------
# timestamp - кількість секунд з 1 січня 1970 року (UTC), epoch time.

from datetime import datetime

# Конвертація datetime у timestamp
now = datetime.now()
timestamp = datetime.timestamp(now)
print(timestamp)  # наприклад, 1702854066.56633

# Конвертація timestamp назад у datetime
timestamp = 1617183600
dt_object = datetime.fromtimestamp(timestamp)
print(dt_object)  # 2021-03-31 12:40:00 (залежить від часової зони)
