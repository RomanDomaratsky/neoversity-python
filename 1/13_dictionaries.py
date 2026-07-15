# Тема: Словники (Dictionaries)
# ---------------------------------
# Словник - контейнер, який зберігає пари ключ-значення.
# Ключем може бути будь-який незмінний тип даних (число, рядок, кортеж тощо).

# Створення порожнього словника
my_dict = {}

# Створення словника з парами ключ-значення
my_dict = {"name": "Alice", "age": 25, "city": "New York"}
print(my_dict)

# Доступ до значення за ключем
print(my_dict["name"])  # Alice

# Зміна значення та додавання нової пари ключ-значення
my_dict["age"] = 26  # Змінює вік на 26
my_dict["email"] = "alice@example.com"  # Додає нову пару ключ-значення
print(my_dict)
# {'name': 'Alice', 'age': 26, 'city': 'New York', 'email': 'alice@example.com'}

# Видалення елемента за ключем через оператор del
del my_dict["age"]
print(my_dict)
# {'name': 'Alice', 'city': 'New York', 'email': 'alice@example.com'}

# Перевірка наявності ключа через оператор in
print("name" in my_dict)  # True
print("age" in my_dict)   # False


# --- Методи словників ---

# pop() - видаляє елемент за ключем і повертає його значення
my_dict = {"name": "Alice", "age": 25}
age = my_dict.pop("age")
print(age, my_dict)  # 25 {'name': 'Alice'}

# update() - оновлює словник іншим словником або парами ключ-значення
my_dict = {"name": "Alice", "age": 25}
my_dict.update({"email": "alice@example.com", "age": 26})
print(my_dict)
# {'name': 'Alice', 'age': 26, 'email': 'alice@example.com'}

# clear() - очищує словник
my_dict.clear()
print(my_dict)  # {}

# copy() - створює поверхневу копію словника
my_dict = {"name": "Alice", "age": 25}
new_dict = my_dict.copy()
print(new_dict)  # {'name': 'Alice', 'age': 25}

# get() - безпечне отримання значення за ключем (не викидає помилку)
my_dict = {"name": "Alice", "age": 25}
age = my_dict.get("age")      # 25
gender = my_dict.get("gender")  # None, оскільки ключа немає
print(age, gender)

# Для порівняння: доступ через [] викине KeyError, якщо ключа немає
name = my_dict["name"]  # 'Alice'
print(name)
# gender = my_dict["gender"]  # розкоментуй, щоб побачити KeyError
