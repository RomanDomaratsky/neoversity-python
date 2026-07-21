# Тема: Форматування дат (strftime) та парсинг дат із рядка (strptime)
# ------------------------------------------------------------------------
# %Y рік (4 цифри)   %y рік (2 цифри)   %m місяць   %d день
# %H година (24г)    %I година (12г)    %M хвилини  %S секунди
# %A повна назва дня %a скорочена назва дня
# %B повна назва місяця  %b/%h скорочена назва місяця
# %p AM/PM (12-годинний формат)

from datetime import datetime

now = datetime.now()

# Форматування дати й часу
formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")
print(formatted_date)

# Форматування лише дати (повна назва дня та місяця)
formatted_date_only = now.strftime("%A, %d %B %Y")
print(formatted_date_only)

# Форматування лише часу (12-годинний формат з AM/PM)
formatted_time_only = now.strftime("%I:%M %p")
print(formatted_time_only)

# Форматування дати у форматі дд.мм.рррр
formatted_date_only = now.strftime("%d.%m.%Y")
print(formatted_date_only)


# strptime - перетворення рядка в об'єкт datetime (протилежність strftime)
date_string = "2023.03.14"
datetime_object = datetime.strptime(date_string, "%Y.%m.%d")
print(datetime_object)  # 2023-03-14 00:00:00
