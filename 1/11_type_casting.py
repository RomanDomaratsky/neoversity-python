# Тема: Приведення типів (type casting)
# -----------------------------------------

# input() повертає рядок (str), тому для порівняння з числом
# його потрібно привести до int
age = input("How old are you? ")
age = int(age)
print(type(age))  # <class 'int'>

# Приведення рядка до float
pi = float('3.14')
print(pi, type(pi))  # 3.14 <class 'float'>

# Приведення числа до рядка
pi_str = str(3.14)
age_str = str(29)
print(pi_str, type(pi_str))    # 3.14 <class 'str'>
print(age_str, type(age_str))  # 29 <class 'str'>

# Приведення до булевого типу
print(bool(0))   # False
print(bool(1))   # True
print(bool(""))  # False (порожній рядок)
print(bool([]))  # False (порожній список)
print(bool(None))  # False


# --- Приклад 1: периметр квадрата ---
def square_perimeter_demo():
    a = float(input("Введіть сторону квадрата a: "))
    P = 4 * a
    print(f"Периметр квадрата дорівнює {P}")
    # Приклад: якщо a = 5, то P = 20


# --- Приклад 2: вартість закупівлі для кава-брейків ---
def coffee_break_cost_demo():
    # Встановлюємо ціни на продукти
    price_per_croissant = 1.04
    price_per_glass = 0.34
    price_per_coffee_pack = 4.42

    # Кількість кожного продукту
    num_croissants = int(input("Введіть кількість круасанів: "))
    num_glasses = int(input("Введіть кількість склянок: "))
    num_coffee_packs = int(input("Введіть кількість упаковок кави: "))

    # Обчислення загальної вартості
    total_cost = num_croissants * price_per_croissant + \
                 num_glasses * price_per_glass + \
                 num_coffee_packs * price_per_coffee_pack

    # Визначаємо кількість повних доларів і центів
    total_dollars = int(total_cost)
    total_cents = int(total_cost * 100)

    # Вивід результату
    print(f"Загальна вартість у повних доларах: {total_dollars} доларів")
    print(f"Загальна вартість у центах: {total_cents} центів")
    # Приклад: 100 круасанів, 100 склянок, 50 упаковок кави ->
    # 359 доларів, 35900 центів


# --- Різниця між / та // ---
print(10 / 5)    # 2.0  (/ завжди повертає float)
print(7 / 2)     # 3.5

print(7 // 2)    # 3    (// повертає int, якщо обидва операнди int)
print(7.0 // 2)  # 3.0  (// повертає float, якщо хоч один операнд float)
print(7 // 2.0)  # 3.0


if __name__ == "__main__":
    square_perimeter_demo()
    coffee_break_cost_demo()
