# Тема: JSON та кирилиця (не-ASCII символи) - ensure_ascii, indent
# ------------------------------------------------------------------------
# За замовчуванням json.dump()/dumps() екранує всі не-ASCII символи у
# вигляді Unicode escape-послідовностей (\uXXXX), навіть якщо файл
# відкрито з encoding="utf-8". Щоб кирилиця (або інші не-ASCII символи)
# записувалась як є, потрібно явно вказати ensure_ascii=False.

import json
import os

data = {"name": "Гупало Василь", "age": 30, "isStudent": True}

# --- Без ensure_ascii: кирилиця перетворюється на \uXXXX escape-послідовності ---
with open("data_escaped.json", "w", encoding="utf-8") as f:
    json.dump(data, f)

with open("data_escaped.json", "r", encoding="utf-8") as f:
    print(f.read())
# {"name": "\u0413\u0443\u043f\u0430\u043b\u043e \u0412\u0430\u0441\u0438\u043b\u044c", "age": 30, "isStudent": true}


# --- З ensure_ascii=False: кирилиця записується як звичайний текст ---
# indent=4 додатково форматує вивід для зручного читання людиною.
with open("data_readable.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

with open("data_readable.json", "r", encoding="utf-8") as f:
    print(f.read())
# {
#     "name": "Гупало Василь",
#     "age": 30,
#     "isStudent": true
# }

# Десеріалізація працює однаково в обох випадках
with open("data_readable.json", "r", encoding="utf-8") as f:
    restored = json.load(f)
    print(restored)  # {'name': 'Гупало Василь', 'age': 30, 'isStudent': True}

for fname in ("data_escaped.json", "data_readable.json"):
    try:
        os.remove(fname)
    except OSError:
        pass

# Практичне застосування: ensure_ascii=False обов'язково використовують,
# коли JSON-файл призначений для перегляду людиною (конфігурації,
# переклади/локалізація інтерфейсу) - без нього кирилиця, емодзі чи інші
# не-ASCII символи будуть нечитабельними escape-кодами.
