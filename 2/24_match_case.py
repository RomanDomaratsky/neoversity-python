# Тема: Оператор match (Python 3.10+)
# ------------------------------------------
# Аналог switch-case в інших мовах програмування.

# Простий приклад: порівняння з рядковими значеннями
fruit = "apple"
match fruit:
    case "apple":
        print("This is an apple.")
    case "banana":
        print("This is a banana.")
    case "orange":
        print("This is an orange.")
    case _:
        print("Unknown fruit.")
# This is an apple.

# Використання змінних у шаблонах (кортежі-координати)
point = (1, 0)
match point:
    case (0, 0):
        print("Точка в центрі координат")
    case (0, y):
        print(f"Точка лежить на осі Y: y={y}")
    case (x, 0):
        print(f"Точка лежить на осі X: x={x}")
    case (x, y):
        print(f"Точка має координати: x={x}, y={y}")
    case _:
        print("Це не точка")
# Точка лежить на осі X: x=1

point = (1, 1)
match point:
    case (0, 0):
        print("Точка в центрі координат")
    case (0, y):
        print(f"Точка лежить на осі Y: y={y}")
    case (x, 0):
        print(f"Точка лежить на осі X: x={x}")
    case (x, y):
        print(f"Точка має координати: x={x}, y={y}")
    case _:
        print("Це не точка")
# Точка має координати: x=1, y=1

# match з колекціями (списками)
pets = ["dog", "fish", "cat"]
match pets:
    case ["dog", "cat", _]:
        print("There's a dog and a cat.")
    case ["dog", _, _]:
        print("There's a dog.")
    case _:
        print("No dogs.")
# There's a dog.
