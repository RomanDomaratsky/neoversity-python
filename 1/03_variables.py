# Тема: Змінні
# -------------
# Змінна - це елемент пам'яті, у якого є ім'я і в якому можуть зберігатися дані.

age = 20
user_name = "Boris"
user_age = 30
ADULT_THR = 18

print(age)         # 20
print(user_name)   # Boris
print(user_age)    # 30
print(ADULT_THR)    # 18

# Python не потребує вказувати тип змінної під час оголошення -
# тип визначається автоматично під час присвоєння значення.
x = 10
print(x)  # 10

# Значення, що зберігається у змінній, можна змінити:
x = 20
print(x)  # 20

# Python чутливий до регістру: data і Data - це різні змінні
data = "нижній регістр"
Data = "Верхній регістр"
print(data)  # нижній регістр
print(Data)  # Верхній регістр

# Приклади зарезервованих слів, які НЕ можна використовувати як імена змінних
# (розкоментуй, щоб побачити помилку):
# class = 5      # SyntaxError, бо "class" - зарезервоване слово
# if = "test"    # SyntaxError, бо "if" - зарезервоване слово

# Повний перелік зарезервованих слів Python:
# False, None, True, and, as, assert, async, await, break, class, continue,
# def, del, elif, else, except, finally, for, from, global, if, import, in,
# is, lambda, nonlocal, not, or, pass, raise, return, try, while, with, yield
