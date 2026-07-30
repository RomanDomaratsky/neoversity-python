import random
import pathlib

# pathlib.Path(__file__).parent - директорія, де лежить САМ цей файл.
# Завдяки цьому шлях до jokes.txt буде правильним незалежно від того,
# з якої директорії запущено головний скрипт main.py.
current_dir = pathlib.Path(__file__).parent


def get_random_joke():
    try:
        with open(current_dir / "jokes.txt", "r", encoding="utf-8") as file:
            jokes = file.readlines()
            return random.choice(jokes).strip()
    except FileNotFoundError:
        return "Не вдалося знайти файл з анекдотами."
