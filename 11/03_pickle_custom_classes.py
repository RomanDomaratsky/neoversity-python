# Тема: pickle та класи користувача - важлива умова десеріалізації
# ------------------------------------------------------------------------
# pickle НЕ зберігає сам код класу - лише дані об'єкта. Тому для успішної
# десеріалізації клас повинен бути ВИЗНАЧЕНИЙ (import або оголошений) у
# скрипті, який виконує pickle.load(), з тією ж структурою та в тому ж
# просторі імен, що й під час серіалізації.

import pickle
import os


class Human:
    def __init__(self, name):
        self.name = name


bob = Human("Bob")
with open("instance.pickle", "wb") as file:
    pickle.dump(bob, file)


# --- Десеріалізація ПРАЦЮЄ, бо клас Human визначений вище в цьому файлі ---
with open("instance.pickle", "rb") as file:
    loaded_instance = pickle.load(file)

print(loaded_instance.name)  # Bob


# --- Демонстрація помилки: якщо клас НЕ визначений, десеріалізація падає ---
# (Симулюємо через exec у окремому namespace без класу Human, щоб показати
# саме ту помилку, яку описує лекція, не ламаючи решту прикладів у файлі.)
import subprocess
import sys

broken_script = """
import pickle
with open("instance.pickle", "rb") as file:
    loaded_instance = pickle.load(file)
print(loaded_instance.name)
"""

result = subprocess.run(
    [sys.executable, "-c", broken_script],
    capture_output=True, text=True, cwd=os.getcwd()
)
print(result.stderr.strip().splitlines()[-1])
# AttributeError: Can't get attribute 'Human' on <module '__main__' (built-in)>
# (текст помилки в різних версіях Python/шляхах може відрізнятись, але суть
# та сама: клас Human не знайдено в просторі імен модуля, що десеріалізує)

try:
    os.remove("instance.pickle")
except OSError:
    pass

# Практичне застосування: цю особливість важливо пам'ятати при передачі
# pickle-даних між сервісами - десеріалізуючий сервіс має мати доступ до
# ТОГО САМОГО визначення класу (наприклад, через спільний пакет моделей),
# інакше отримає AttributeError. Тому pickle рідко використовують для
# міжсервісної комунікації - там частіше обирають JSON.
