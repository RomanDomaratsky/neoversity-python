# Тема: Булева алгебра (and, or, not) та задача FizzBuzz
# --------------------------------------------------------------

# Складна умова з and: усі частини мають бути True
name = "Taras"
age = 17
has_driver_licence = True
if name and age >= 18 and has_driver_licence:
    print(f"User {name} can NOT rent a car")

# Оператор and (і) - True тільки якщо обидва операнди True
a = True and False  # False
print(a)

# Оператор or (або) - True якщо хоча б один операнд True
a = True or False  # True
print(a)

# Оператор not (ні) - інвертує значення
a = not 2 < 0  # True, бо 2 < 0 є False
print(a)


# Приклад: перевірка, чи число парне двозначне
def even_two_digit_demo():
    num = int(input("Введіть число: "))
    length = len(str(num))
    if length == 2 and num % 2 == 0:
        print("Парне двозначне число")
    else:
        print("Ні")


# --- Задача FizzBuzz ---
def fizzbuzz_demo():
    num = int(input())
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)


# Версія FizzBuzz для декількох чисел одразу (для демонстрації без input)
def fizzbuzz(num: int) -> str:
    if num % 3 == 0 and num % 5 == 0:
        return "FizzBuzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    else:
        return str(num)


if __name__ == "__main__":
    for n in range(1, 16):
        print(fizzbuzz(n))
