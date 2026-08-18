# Тема: json.dump / json.load - серіалізація JSON безпосередньо у файл
# ------------------------------------------------------------------------
# dump(obj, file) - записує JSON у відкритий файл
# load(file)      - читає та парсить JSON з відкритого файлу
# Файли JSON - текстові, тому відкриваються у звичайному текстовому режимі.

import json
import os

data = {"name": "Gupalo Vasyl", "age": 30, "isStudent": True}

# Серіалізація у файл
with open("data.json", "w", encoding="utf-8") as f:
    json.dump(data, f)

# Перевіримо вміст файлу
with open("data.json", "r", encoding="utf-8") as f:
    print(f.read())
# {"name": "Gupalo Vasyl", "age": 30, "isStudent": true}

# Десеріалізація з файлу
with open("data.json", "r", encoding="utf-8") as f:
    data_from_file = json.load(f)
    print(data_from_file)
# {'name': 'Gupalo Vasyl', 'age': 30, 'isStudent': True}

try:
    os.remove("data.json")
except OSError:
    pass

# Практичне застосування: json.dump/load у файл - стандартний спосіб
# зберігати конфігурацію застосунку (config.json), кеш даних API, або
# експортувати результати роботи скрипта в читабельному текстовому форматі,
# який легко переглянути й відредагувати вручну.
