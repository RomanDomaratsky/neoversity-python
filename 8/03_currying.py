# Тема: Каррінг (currying) - перетворення функції з кількома аргументами
# на послідовність функцій з ОДНИМ аргументом кожна
# ------------------------------------------------------------------------

# Звичайна функція з двома аргументами
def add(a, b):
    return a + b


print(add(5, 10))  # 15


# Та сама функція, але через каррінг
def add_curried(a):
    def add_b(b):
        return a + b
    return add_b


add_5 = add_curried(5)
result = add_5(10)
print(result)  # 15


# --- Практичний приклад: обчислення знижки на товар ---
def apply_discount(price: float, discount_percentage: int) -> float:
    return price * (1 - discount_percentage / 100)


print(apply_discount(500, 10))  # 450.0
print(apply_discount(500, 20))  # 400.0


# Каррінг дозволяє створити "заготовлені" функції для конкретних знижок,
# кожна з яких приймає тільки ціну. Практичне застосування: типово для
# прайс-листів/акцій інтернет-магазину, де знижка фіксована, а ціна - змінна.
from typing import Callable


def discount(discount_percentage: int) -> Callable[[float], float]:
    def apply(price: float) -> float:
        return price * (1 - discount_percentage / 100)
    return apply


ten_percent_discount = discount(10)
twenty_percent_discount = discount(20)

print(ten_percent_discount(500))    # 450.0
print(twenty_percent_discount(500))  # 400.0


# Зберігання каррі-функцій у словнику - легко додавати нові знижки
from typing import Dict

discount_functions: Dict[str, Callable] = {
    "10%": discount(10),
    "20%": discount(20),
    "30%": discount(30)
}

price = 500
discount_type = "20%"
discounted_price = discount_functions[discount_type](price)
print(f"Ціна зі знижкою {discount_type}: {discounted_price}")  # 400.0
