# Тема: List Comprehensions
# ------------------------------------------------------------------------
# Синтаксис: [new_item for item in iterable if condition]

# Спосіб "по-старому" через цикл for
sq = []
for i in range(1, 6):
    sq.append(i ** 2)
print(sq)  # [1, 4, 9, 16, 25]

# Той самий результат через list comprehension - один рядок
sq = [x ** 2 for x in range(1, 6)]
print(sq)  # [1, 4, 9, 16, 25]


# З умовою: квадрати тільки ПАРНИХ чисел від 1 до 9
even_squares = [x ** 2 for x in range(1, 10) if x % 2 == 0]
print(even_squares)  # [4, 16, 36, 64]

# Той самий результат через звичайний цикл (для порівняння обсягу коду)
even_squares = []
for x in range(1, 10):
    if x % 2 == 0:
        even_squares.append(x ** 2)
print(even_squares)  # [4, 16, 36, 64]
