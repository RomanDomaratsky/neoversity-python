# Тема: Модуль math
# ----------------------

import math

# Константи
print(math.pi)    # ~3.14159...
print(math.e)     # ~2.71828...
print(math.tau)   # ~6.28318... (2*pi)
print(math.inf)   # нескінченність
print(math.nan)   # Not a Number

# Функції округлення
x = 3.7
ceil_result = math.ceil(x)    # округлення вгору
floor_result = math.floor(x)  # округлення вниз
trunc_result = math.trunc(x)  # відсікання дробової частини
print(ceil_result, floor_result, trunc_result)  # 4 3 3

# Тригонометричні функції
angle = math.radians(60)  # конвертація з градусів у радіани
print(math.sin(angle))
print(math.cos(angle))
print(math.tan(angle))

# Експоненційні та логарифмічні функції
print(math.exp(1))       # e^1
print(math.log(10, 2))   # логарифм 10 за основою 2
print(math.log(math.e))  # натуральний логарифм

# Ступінь і корінь
print(math.pow(2, 10))  # 2 у ступені 10
print(math.sqrt(9))     # квадратний корінь з 9

# Інші корисні функції
print(math.fabs(-5))        # модуль числа
print(math.factorial(5))    # факторіал: 120
print(math.gcd(12, 18))     # найбільший спільний дільник: 6

# Примітка: для комплексних чисел існує аналогічний пакет cmath
