# Тема: Set Comprehensions
# ------------------------------------------------------------------------
# Синтаксис: {new_item for item in iterable if condition}

numbers = [1, 4, 1, 3, 2, 5, 2, 6]
sq = {i ** 2 for i in numbers}
print(sq)  # {1, 4, 36, 9, 16, 25} - дублікати автоматично прибрані (множина)

# З умовою: квадрати тільки НЕПАРНИХ чисел від 1 до 9
odd_squares = {x ** 2 for x in range(1, 10) if x % 2 != 0}
print(odd_squares)  # {1, 9, 81, 49, 25}
