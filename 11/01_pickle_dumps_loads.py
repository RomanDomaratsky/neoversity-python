# Тема: Серіалізація об'єктів у Python - вступ + pickle.dumps/loads
# ------------------------------------------------------------------------
# Серіалізація - перетворення об'єкта/структури даних у потік байтів для
# зберігання чи передачі. Десеріалізація - зворотний процес відновлення
# об'єкта. pickle - вбудований модуль для серіалізації Python-об'єктів
# (словників, списків, кортежів, рядків, множин і навіть нескладних
# класів) у байтовий формат, специфічний для Python.

# --- Найпростіший (примітивний) варіант "власного" протоколу серіалізації ---
expenses = {"hotel": 150, "breakfast": 30, "taxi": 15, "lunch": 20}

file_name = "expenses.txt"
with open(file_name, "w") as fh:
    for key, value in expenses.items():
        fh.write(f"{key}|{value}\n")

# Десеріалізація назад у словник
expenses_loaded = {}
with open(file_name, "r") as fh:
    raw_expenses = fh.readlines()
    for line in raw_expenses:
        key, value = line.split("|")
        expenses_loaded[key] = int(value)

print(expenses_loaded)  # {'hotel': 150, 'breakfast': 30, 'taxi': 15, 'lunch': 20}

import os
try:
    os.remove(file_name)
except OSError:
    pass


# --- pickle.dumps / pickle.loads: серіалізація у BYTE-рядок і назад ---
import pickle

my_data = {"key": "value", "num": 42}

serialized_data = pickle.dumps(my_data)
print(serialized_data)  # b'\x80\x04...' - байтове представлення об'єкта

deserialized_data = pickle.loads(serialized_data)
print(deserialized_data)  # {'key': 'value', 'num': 42}

# Практичне застосування: dumps/loads використовують, коли потрібно
# КОНТРОЛЮВАТИ байтове представлення напряму - наприклад, відправити його
# мережею (сокет, черга повідомлень типу Redis/RabbitMQ) або зберегти як
# BLOB у базі даних.
