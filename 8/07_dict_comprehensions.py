# Тема: Dictionary Comprehensions
# ------------------------------------------------------------------------
# Синтаксис: {key: value for item in iterable if condition}

sq = {x: x ** 2 for x in range(1, 10)}
print(sq)  # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}

# З умовою: тільки для чисел, більших за 5
sq_dict = {x: x ** 2 for x in range(1, 10) if x > 5}
print(sq_dict)  # {6: 36, 7: 49, 8: 64, 9: 81}
