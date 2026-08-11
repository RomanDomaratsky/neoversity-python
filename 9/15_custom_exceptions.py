# Тема: Власні винятки (Custom Exceptions)
# ------------------------------------------------------------------------
# Власний виняток - клас, що наслідується від Exception (або одного з
# його підкласів). Дозволяє сигналізувати про специфічні для програми
# помилки та обробляти їх окремо від загальних вбудованих винятків.

# --- Нагадування: стандартний try/except/else/finally ---
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Ділення на нуль!")
except Exception as e:
    print(f"Виникла помилка: {e}")
else:
    print("Все пройшло успішно!")
finally:
    print("Блок finally завжди виконується.")


# --- Найпростіший власний виняток ---
class MyCustomError(Exception):
    """Базовий клас для власних винятків"""
    pass


# --- Практичний приклад 1: перевірка віку ---
class AgeVerificationError(Exception):
    def __init__(self, message="Вік не задовольняє мінімальній вимозі"):
        self.message = message
        super().__init__(self.message)


def verify_age(age: int):
    if age < 18:
        raise AgeVerificationError("Вік особи меньший за 18 років")


if __name__ == "__main__":
    try:
        verify_age(16)
    except AgeVerificationError as e:
        print(f"Виняток: {e}")  # Виняток: Вік особи меньший за 18 років
    else:
        print("Вік перевірено, особа доросла.")


# --- Практичний приклад 2: валідація введеного імені (декілька власних винятків) ---
class NameTooShortError(Exception):
    pass


class NameStartsFromLowError(Exception):
    pass


def validate_name(name: str) -> str:
    if len(name) < 3:
        raise NameTooShortError("Name is too short, need more than 2 symbols")
    if not name[0].isupper():
        raise NameStartsFromLowError("Name should start from capital letter")
    return name


for test_name in ("Bob", "bob", "Bo"):
    try:
        validated = validate_name(test_name)
        print(f"Hello, {validated}")
    except (NameTooShortError, NameStartsFromLowError) as e:
        print(e)
# Hello, Bob
# Name should start from capital letter
# Name is too short, need more than 2 symbols

# Практичне застосування: власні винятки використовують у API/бібліотеках,
# щоб виклична сторона могла точково обробити саме "свою" помилку (напр.
# InsufficientFundsError у платіжній системі, ValidationError у формах),
# не змішуючи бізнес-помилки із загальними винятками Python.
