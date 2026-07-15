# Тема: Заморожені множини (Frozen Sets)
# -------------------------------------------
# frozenset - незмінна версія множини. Після створення не можна
# додавати або видаляти елементи.

my_frozenset = frozenset([1, 2, 3, 4, 5])
print(my_frozenset)  # frozenset({1, 2, 3, 4, 5})

# my_frozenset.add(6)     # AttributeError - методу add() немає
# my_frozenset.remove(1)  # AttributeError - методу remove() немає

# Операції, які НЕ змінюють саму множину, доступні:
a = frozenset([1, 2, 3])
b = frozenset([3, 4, 5])

union = a | b                       # Об'єднання множин
intersection = a & b                # Перетин множин
difference = a - b                  # Різниця множин
symmetric_difference = a ^ b        # Симетрична різниця

print(union)                 # frozenset({1, 2, 3, 4, 5})
print(intersection)          # frozenset({3})
print(difference)            # frozenset({1, 2})
print(symmetric_difference)  # frozenset({1, 2, 4, 5})

# Заморожені множини є хешованими, тому їх можна використовувати
# як ключі словника або елементи інших множин
lookup = {
    frozenset([1, 2, 3]): "перша група",
    frozenset([4, 5, 6]): "друга група",
}
print(lookup[frozenset([1, 2, 3])])  # перша група
