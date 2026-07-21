# Тема: Модуль time
# ----------------------
# На відміну від datetime, не підтримує часові зони чи складні операції з датами.

import time

# time.time() - поточний час у секундах з 1 січня 1970 (epoch time)
current_time = time.time()
print(f"Поточний час: {current_time}")

# time.sleep(seconds) - зупиняє виконання програми на вказану кількість секунд
print("Початок паузи")
time.sleep(1)  # у конспекті 5 секунд, тут скорочено для демонстрації
print("Кінець паузи")

# time.ctime([seconds]) - часова мітка -> текстове представлення для людини
current_time = time.time()
readable_time = time.ctime(current_time)
print(f"Читабельний час: {readable_time}")

# time.localtime([seconds]) - часова мітка -> struct_time у місцевій зоні
local_time = time.localtime(current_time)
print(f"Місцевий час: {local_time}")
# Поля struct_time: tm_year, tm_mon, tm_mday, tm_hour, tm_min, tm_sec,
# tm_wday, tm_yday, tm_isdst

# time.gmtime([seconds]) - те саме, але в UTC
utc_time = time.gmtime(current_time)
print(f"UTC час: {utc_time}")

# time.perf_counter() - лічильник високої точності для вимірювання часу виконання
start_time = time.perf_counter()

for _ in range(1_000_000):
    pass  # оператор pass - "порожня" інструкція-заповнювач

end_time = time.perf_counter()
execution_time = end_time - start_time
print(f"Час виконання: {execution_time} секунд")

# Підкреслення у числах для читабельності великих чисел
a = 1_000_000       # один мільйон
b = 10_000_000      # десять мільйонів
c = 1_000_000_000   # один мільярд
print(a, b, c)  # 1000000 10000000 1000000000


# pass також використовується як заповнювач у ще не реалізованих функціях
def my_function():
    pass
