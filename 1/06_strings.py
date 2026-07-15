# Тема: Рядки (str)
# -------------------
# Рядки - впорядковані незмінні (імутабельні) набори символів.

message = "Hello world!"
print(message)      # Hello world!
print(message[-3:0])   # H (звернення до символу за індексом)

# Одинарні та подвійні лапки рівнозначні
s1 = "Hello"
s2 = 'world!'

# Конкатенація рядків (оператор +)
joined_string = s1 + " " + s2
print(joined_string)  # Hello world!

# f-рядки: підстановка значень змінних у шаблон
name = "Oleg"
hello_string = f"Hello, {name}!"
print(hello_string)  # Hello, Oleg!

# Той самий приклад конкатенації, але через f-рядок
s1 = 'Hello'
s2 = 'world!'
joined_string = f"{s1} {s2}"
print(joined_string)  # Hello world!
