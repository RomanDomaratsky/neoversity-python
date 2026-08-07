# Тема: Замикання (closures)
# ------------------------------------------------------------------------
# Замикання - коли внутрішня функція "запам'ятовує" змінні з оточення
# зовнішньої функції навіть ПІСЛЯ того, як зовнішня функція завершилась.

def outer_function(msg):
    message = msg

    def inner_function():
        print(message)

    return inner_function


my_func = outer_function("Hello, world!")
my_func()  # Hello, world! - message "запам'ятався" усередині inner_function


# --- Практичний приклад: лічильник викликів через замикання ---
# Практичне застосування: така конструкція - основа для створення функцій
# зі "своєю пам'яттю" без використання класів чи глобальних змінних -
# наприклад, лічильники подій, кешування останнього результату тощо.
from typing import Callable


def counter() -> Callable[[], int]:
    count = 0

    def increment() -> int:
        nonlocal count  # без nonlocal Python створив би НОВУ локальну count
        count += 1
        return count

    return increment


count_calls = counter()

print(count_calls())  # 1
print(count_calls())  # 2
print(count_calls())  # 3

# Другий лічильник має свій ВЛАСНИЙ стан count, незалежний від першого
another_counter = counter()
print(another_counter())  # 1 (а не 4!)
