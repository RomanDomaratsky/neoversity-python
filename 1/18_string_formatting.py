# Тема: Форматування рядків за допомогою методу format()
# -------------------------------------------------------------
# До появи f-рядків у Python активно використовували метод format().
# Він замінює {} у рядку на аргументи, передані методу format().

# Просте форматування рядка
name = 'John'
print('Hello, {}!'.format(name))
# Hello, John!

# Форматування з декількома аргументами
age = 25
print('Hello, {}. You are {} years old.'.format(name, age))
# Hello, John. You are 25 years old.

# Використання іменованих аргументів
print('Hello, {name}. You are {age} years old.'.format(name='Jane', age=30))
# Hello, Jane. You are 30 years old.

# Використання індексів для вказівки порядку аргументів
print('Hello, {1}. You are {0} years old.'.format(age, name))
# Hello, John. You are 25 years old.
