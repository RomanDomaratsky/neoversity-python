# Тема: Функція як об'єкт першого класу
# ------------------------------------------------------------------------
# Функції можна: присвоювати змінним, передавати як аргументи, повертати
# з інших функцій, зберігати в колекціях (списках, словниках).

# --- 1. Присвоєння функції змінній ---
def my_function():
    print("Hello, world!")


f = my_function
f()  # Hello, world! - викликаємо f, а не my_function напряму


# --- 2. Функція як аргумент іншої функції ---
from typing import Callable


def add(a: int, b: int) -> int:
    return a + b


def multiply(a: int, b: int) -> int:
    return a * b


def apply_operation(a: int, b: int, operation: Callable[[int, int], int]) -> int:
    return operation(a, b)


result_add = apply_operation(5, 3, add)
result_multiply = apply_operation(5, 3, multiply)
print(result_add, result_multiply)  # 8 15


# --- 3. Функція, що повертає іншу функцію ---
def power(exponent: int) -> Callable[[int], int]:
    def inner(base: int) -> int:
        return base ** exponent
    return inner


square = power(2)
cube = power(3)

print(square(4))  # 16
print(cube(4))    # 64


# --- 4. Зберігання функцій у структурах даних (словнику) ---
from typing import Dict

operations: Dict[str, Callable] = {
    'add': add,
    'multiply': multiply,
    'square': square,
    'cube': cube
}

result_add = operations['add'](10, 20)   # 30
result_square = operations['square'](5)  # 25

print(result_add)     # 30
print(result_square)  # 25
