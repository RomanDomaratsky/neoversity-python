# Тема: Модуль data.py - завантаження та первинне очищення даних
# ------------------------------------------------------------------------
# Розділення "завантаження даних" (data.py) та "аналізу даних" (processing.py)
# - типовий підхід у скриптах обробки даних: якщо джерело даних зміниться
# (наприклад, дані прийдуть з бази даних чи API замість файлу), достатньо
# переписати тільки data.py, а вся логіка аналізу в processing.py залишиться.


def load_data(filename: str) -> list[str]:
    with open(filename, "r") as file:
        return file.readlines()


def clean_data(temperature_data: list[str]) -> list[float]:
    return [float(temp.strip()) for temp in temperature_data if temp.strip()]
