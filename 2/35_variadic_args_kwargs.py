# Тема: Змінна кількість параметрів (*args, **kwargs) та розпакування
# ------------------------------------------------------------------------

# --- *args: довільна кількість позиційних аргументів (упаковані в кортеж) ---
def print_all_args(*args):
    for arg in args:
        print(arg)


print_all_args(1, 'hello', True)
# 1
# hello
# True


def concatenate(*args) -> str:
    result = ""
    for arg in args:
        result += arg
    return result


print(concatenate("Hello", " ", "world", "!"))  # Hello world!

# Ім'я параметра після * може бути будь-яким, не обов'язково "args"
def concatenate_v2(*strings) -> str:
    result = ""
    for arg in strings:
        result += arg
    return result


print(concatenate_v2("Hello", " ", "world", "!"))  # Hello world!


# --- **kwargs: довільна кількість ключових аргументів (упаковані в словник) ---
def greet(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


greet(name="Alice", age=25)
# name: Alice
# age: 25


# --- *args та **kwargs разом (args має йти першим) ---
def example_function(*args, **kwargs):
    print("Позиційні аргументи:", args)
    print("Ключові аргументи:", kwargs)


example_function(1, 2, 3, name="Alice", age=25)
# Позиційні аргументи: (1, 2, 3)
# Ключові аргументи: {'name': 'Alice', 'age': 25}


# --- Розпакування списків ---
my_list = [1, 2, 3]
a, b, c = my_list
print(a, b, c)  # 1 2 3

# Ігнорування елемента через _
a, _, c = my_list
print(a, c)  # 1 3

# Розпакування "залишку" через *
a, *rest = my_list
print(a, rest)  # 1 [2, 3]


# --- Розпакування словників у виклику функції ---
def greet_person(name, age):
    print(f"Hello {name}, you are {age} years old.")


person_info = {"name": "Alice", "age": 25}
greet_person(**person_info)
# Hello Alice, you are 25 years old.
