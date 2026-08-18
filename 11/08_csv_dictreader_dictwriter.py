# Тема: csv.DictReader та csv.DictWriter - робота з CSV як зі словниками
# ------------------------------------------------------------------------
# DictWriter/DictReader дозволяють звертатися до полів CSV за ІМЕНАМИ
# колонок замість числових індексів - код стає читабельнішим і менш
# крихким до зміни порядку колонок.

import csv
import os

# --- Запис у CSV зі словників ---
with open("students.csv", "w", newline="", encoding="utf-8") as csvfile:
    fieldnames = ["name", "age", "specialty"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()  # записує рядок заголовків
    writer.writerow({"name": "Олег Олегов", "age": 23, "specialty": "Історія"})
    writer.writerow({"name": "Анна Сергіївна", "age": 22, "specialty": "Біологія"})

# --- Читання CSV у словники ---
with open("students.csv", newline="", encoding="utf-8") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row["name"], row["age"], row["specialty"])
# Олег Олегов 23 Історія
# Анна Сергіївна 22 Біологія

try:
    os.remove("students.csv")
except OSError:
    pass


# --- Практичний приклад: колонки визначаються динамічно з ключів даних ---
FILENAME = "users.csv"

users = [
    {"name": "Микола", "age": 22, "gender": "male"},
    {"name": "Марія", "age": 22, "gender": "female"},
    {"name": "Назар", "age": 22, "gender": "male"},
]

with open(FILENAME, "w", encoding="utf-8", newline="") as f:
    columns = users[0].keys()  # імена колонок беремо з ключів першого словника
    writer = csv.DictWriter(f, delimiter=",", fieldnames=columns)
    writer.writeheader()
    for row in users:
        writer.writerow(row)

with open(FILENAME, "r", encoding="utf-8", newline="") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row)
# {'name': 'Микола', 'age': '22', 'gender': 'male'}
# {'name': 'Марія', 'age': '22', 'gender': 'female'}
# {'name': 'Назар', 'age': '22', 'gender': 'male'}
# УВАГА: усі значення при читанні CSV повертаються як РЯДКИ (навіть 'age'),
# CSV не зберігає типи даних - за потреби конвертуйте самостійно (int(...)).

try:
    os.remove(FILENAME)
except OSError:
    pass

# Практичне застосування: DictReader/DictWriter ідеальні для обробки
# табличних вивантажень з довільним/змінним набором колонок - наприклад,
# експорт даних користувачів із CRM, де порядок і склад полів визначається
# динамічно самими даними, а не жорстко заданим списком індексів.
