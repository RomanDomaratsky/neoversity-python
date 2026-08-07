# Тема: Декоратори - зміна поведінки функції БЕЗ зміни її коду
# ------------------------------------------------------------------------
# Практичне застосування: декоратори повсюдно використовують у веброзробці
# (Flask/Django/FastAPI) для логування, перевірки прав доступу, кешування
# результатів та валідації аргументів - без дублювання цієї логіки в
# кожній окремій функції-обробнику.

# --- 1. Декоратор "вручну", без синтаксису @ ---
def complicated(x: int, y: int) -> int:
    return x + y


def logger(func):
    def inner(x: int, y: int) -> int:
        print(f"Викликається функція: {func.__name__}: {x}, {y}")
        result = func(x, y)
        print(f"Функція {func.__name__} завершила виконання: {result}")
        return result
    return inner


complicated = logger(complicated)
print(complicated(2, 3))
# Викликається функція: complicated: 2, 3
# Функція complicated завершила виконання: 5
# 5


# --- 2. Той самий результат через синтаксис @ (декоратор) ---
def logger2(func):
    def inner(x: int, y: int) -> int:
        print(f"Викликається функція: {func.__name__}: {x}, {y}")
        result = func(x, y)
        print(f"Функція {func.__name__} завершила виконання: {result}")
        return result
    return inner


@logger2
def complicated2(x: int, y: int) -> int:
    return x + y


print(complicated2(2, 3))


# --- 3. functools.wraps - зберігає метадані оригінальної функції ---
# Без wraps, complicated3.__name__ дав би "inner", а не "complicated3" -
# це заважає, наприклад, автогенерації документації API чи логам.
from functools import wraps


def logger3(func):
    @wraps(func)
    def inner(x: int, y: int) -> int:
        print(f"Викликається функція: {func.__name__}: {x}, {y}")
        result = func(x, y)
        print(f"Функція {func.__name__} завершила виконання: {result}")
        return result
    return inner


@logger3
def complicated3(x: int, y: int) -> int:
    return x + y


print(complicated3(2, 3))
print(complicated3.__name__)  # complicated3 (а не "inner" - завдяки @wraps)
