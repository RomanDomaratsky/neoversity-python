# Тема: Логічний тип (bool) та оператори порівняння
# ----------------------------------------------------

# Спосіб 1: пряме присвоєння True/False
is_active = True
is_delete = False
print(is_active, is_delete)  # True False

# Спосіб 2: результат логічного виразу (порівняння)
age = 18
is_adult = age >= 18
print(is_adult)  # True

age = 15
is_adult = age >= 18
print(is_adult)  # False

# Оператори порівняння
x = 5
y = 3

print(x == y)  # False, рівність
print(x != y)  # True, нерівність
print(x > y)   # True, більше
print(x < y)   # False, менше
print(x >= y)  # True, більше або дорівнює
print(x <= y)  # False, менше або дорівнює
