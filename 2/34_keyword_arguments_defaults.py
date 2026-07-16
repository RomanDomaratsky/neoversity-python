# Тема: Ключові аргументи та значення параметрів за замовчуванням
# ------------------------------------------------------------------------

# Ключовий параметр зі значенням за замовчуванням
def greet(name, message="Привіт"):
    print(f"{message}, {name}!")


greet("Олексій")                       # використовує значення за замовчуванням
greet("Марія", message="Добрий день")  # передача власного значення
# Привіт, Олексій!
# Добрий день, Марія!


# Гнучкість позиційних та ключових аргументів
def func(a, b=5, c=10):
    print('a дорівнює', a, ', b дорівнює', b, ', а c дорівнює', c)


func(3, 7)          # a=3, b=7, c=10 (за замовчуванням)
func(25, c=24)      # a=25, b=5 (за замовчуванням), c=24
func(c=50, a=100)   # a=100, b=5 (за замовчуванням), c=50


# Значення за замовчуванням - тільки для параметрів у кінці списку
def say(message, times=1):
    print(message * times)


say('Привіт')     # виведе один раз
say('Світ', 5)    # виведе п'ять разів

# def func(a=5, b):  # НЕ ДОПУСТИМО - призведе до помилки


# --- Задача: розрахунок ціни товару зі знижкою ---
def real_cost(base: int, discount: int = 0) -> int:
    return base * (1 - discount)


price_bread = 15
price_butter = 50
price_sugar = 60

current_price_bread = real_cost(price_bread)
current_price_butter = real_cost(price_butter, 0.05)
current_price_sugar = real_cost(price_sugar, 0.07)

print(f'Нова вартість хліба: {current_price_bread}')
print(f'Нова вартість масла: {current_price_butter}')
print(f'Нова вартість цукру: {current_price_sugar}')
# Нова вартість хліба: 15
# Нова вартість масла: 47.5
# Нова вартість цукру: 55.8
