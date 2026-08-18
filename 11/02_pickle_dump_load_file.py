# Тема: pickle.dump / pickle.load - серіалізація безпосередньо у файл
# ------------------------------------------------------------------------
# dump(obj, file)  - записує серіалізований об'єкт напряму у відкритий файл
# load(file)       - читає та відновлює об'єкт з відкритого файлу
# Файл потрібно відкривати у БІНАРНОМУ режимі: "wb" для запису, "rb" для читання.

import pickle
import os

my_data = {"key": "value", "num": 100}

# Серіалізація об'єкта у файл
with open("data.pickle", "wb") as file:
    pickle.dump(my_data, file)

# Десеріалізація об'єкта з файлу (наприклад, в іншому скрипті)
with open('data.pickle', 'rb') as file:
    deserialized_data = pickle.load(file)

print(deserialized_data)  # {'key': 'value', 'num': 100}

try:
    os.remove("data.pickle")
except OSError:
    pass


# --- Практичний приклад: збереження налаштувань програми між запусками ---
settings = {'theme': 'dark', 'language': 'ukrainian'}
with open('settings.pickle', 'wb') as f:
    pickle.dump(settings, f)

# При наступному запуску програми:
with open('settings.pickle', 'rb') as f:
    loaded_settings = pickle.load(f)

print(loaded_settings)  # {'theme': 'dark', 'language': 'ukrainian'}

try:
    os.remove("settings.pickle")
except OSError:
    pass

# Практичне застосування: dump/load у файл - зручний спосіб зберігати
# налаштування програми, кешувати результати довгих обчислень (щоб не
# рахувати повторно при перезапуску), або передавати проміжний стан
# роботи між окремими процесами/скриптами через файлову систему.
