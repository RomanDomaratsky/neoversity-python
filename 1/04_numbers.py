# Тема: Типи даних - Числа (int, float, complex)
# -------------------------------------------------

# Цілі числа (int)
int_number = 3
print(int_number, type(int_number))  # 3 <class 'int'>

# Дійсні числа (float)
float_number = 3.3
print(float_number, type(float_number))  # 3.3 <class 'float'>

# Комплексні числа (complex): a + bj
complex_number = 3.3 + 2j
print(complex_number, type(complex_number))  # (3.3+2j) <class 'complex'>

# Особливість представлення дійсних чисел у пам'яті комп'ютера:
a = 0.2 + 0.1
print(a)  # 0.30000000000000004 (а не рівно 0.3)

# Тому порівнювати дійсні числа напряму через == небезпечно.
# Краще порівнювати різницю з певною точністю:
tolerance = 0.000001
print(abs(a - 0.3) < tolerance)  # True
