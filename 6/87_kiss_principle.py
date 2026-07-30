# Тема: Принцип KISS (Keep It Simple, Stupid)
# ------------------------------------------------------------------------
# Ідея: уникати зайвої складності, писати рішення настільки просто,
# наскільки це можливо без втрати коректності.

# --- Приклад 1: перевірка парності числа ---

# Без урахування KISS - зайва конструкція if-else навколо булевого виразу
def is_even_verbose(number: int) -> bool:
    if number % 2 == 0:
        return True
    else:
        return False


# З урахуванням KISS - вираз сам по собі вже True/False, зайвий if-else прибрано
def is_even(number: int) -> bool:
    return number % 2 == 0


print(is_even_verbose(4), is_even(4))  # True True
print(is_even_verbose(7), is_even(7))  # False False


# --- Приклад 2: перевірка рядка на паліндром ---
# Наприклад, рядок "Козак з казок" є паліндромом (читається однаково з обох боків).

# Без урахування KISS - явний цикл порівняння символів по індексах
def is_palindrome_verbose(s: str) -> bool:
    new_s = ""
    for char in s:
        if char.isalnum():
            new_s += char.lower()

    s = new_s
    length = len(s)
    for i in range(length // 2):
        if s[i] != s[length - i - 1]:
            return False
    return True


# З урахуванням KISS - зріз s[::-1] розвертає рядок, порівняння в один рядок
def is_palindrome(s: str) -> bool:
    new_s = ""
    for char in s:
        if char.isalnum():
            new_s += char.lower()

    s = new_s
    return s == s[::-1]


print(is_palindrome_verbose("Козак з казок"))  # True
print(is_palindrome("Козак з казок"))          # True
print(is_palindrome("Python"))                 # False
