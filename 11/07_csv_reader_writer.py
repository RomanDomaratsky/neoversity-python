# Тема: Робота з CSV файлами - csv.reader / csv.writer
# ------------------------------------------------------------------------
# CSV (Comma-Separated Values) - текстовий формат для табличних даних:
# кожен рядок файлу = один запис, поля розділені комою (або іншим
# роздільником), перший рядок часто містить заголовки колонок.
#
# newline='' при відкритті файлу - важливо! Без цього параметра csv-модуль
# може некоректно обробити символи кінця рядка на різних ОС (Windows
# \r\n, Linux/macOS \n), що зіпсує структуру даних.

import csv
import os

# --- Запис у CSV через csv.writer ---
rows = [
    ["name", "age", "specialty"],
    ["Василь Гупало", 30, "Математика"],
    ["Марія Петренко", 22, "Фізика"],
    ["Олександр Коваленко", 20, "Інформатика"],
]

with open("data.csv", "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile, delimiter=",")
    writer.writerows(rows)  # запис одразу декількох рядків
    # для одного рядка використовують writer.writerow(row)


# --- Читання з CSV через csv.reader ---
with open("data.csv", newline="", encoding="utf-8") as csvfile:
    reader = csv.reader(csvfile, delimiter=",")
    for row in reader:
        print(", ".join(map(str, row)))
# name, age, specialty
# Василь Гупало, 30, Математика
# Марія Петренко, 22, Фізика
# Олександр Коваленко, 20, Інформатика

try:
    os.remove("data.csv")
except OSError:
    pass

# Практичне застосування: csv.reader/writer використовують для експорту
# звітів (продажі, транзакції) у формат, який відкриється в Excel/Google
# Sheets, або для імпорту масових даних (прайс-листів, каталогів товарів)
# у систему без потреби писати власний парсер тексту.
