# Тема: Створення та виклик функцій, параметри, типізація, return
# ------------------------------------------------------------------------

# Найпростіша функція без параметрів
def say_hello():
    # тіло функції
    print('Привіт, Світ!')


say_hello()
say_hello()


# Функція з параметрами (a, b - параметри; при виклику передаються аргументи)
def print_max(a, b):
    if a > b:
        print(a, 'максимально')
    elif a == b:
        print(a, 'дорівнює', b)
    else:
        print(b, 'максимально')


print_max(3, 4)  # пряма передача значень

x = 5
y = 7
print_max(x, y)  # передача змінних як аргументів


# Типізація параметрів (type hints) - не впливає на виконання, лише підказка
def print_max_typed(a: int, b: int):
    if a > b:
        print(a, 'максимально')
    elif a == b:
        print(a, 'дорівнює', b)
    else:
        print(b, 'максимально')


print_max_typed(3, 4)


# --- Повернення результату через return ---

def add_numbers(num1: int, num2: int) -> int:
    total = num1 + num2
    return total


result = add_numbers(5, 10)
print(result)  # 15


def greet(name: str) -> str:
    return f"Привіт, {name}!"


greeting = greet("Олексій")
print(greeting)  # Привіт, Олексій!


def is_even(num: int) -> bool:
    return num % 2 == 0


check_even = is_even(4)
print(check_even)  # True
