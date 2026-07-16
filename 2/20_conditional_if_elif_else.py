# Тема: Умовне виконання коду (if / elif / else)
# ----------------------------------------------------

# Базовий if-else
num = 15
if num > 10:
    print("num більше за 10")
else:
    print("num не більше за 10")


def check_even_demo():
    x = int(input('Введіть число: '))
    if x % 2 == 0:
        print("Число x є парним.")
    else:
        print("Число x є непарним.")


# if ... elif ... else - перевірка знаку числа
def sign_demo():
    a = input('Введіть число: ')
    a = int(a)
    if a > 0:
        print('Число додатне')
    elif a < 0:
        print("Число від'ємне")
    else:
        print('Це число - нуль')


# Приклад ПОМИЛКИ: перевірка elif a == 1 ніколи не виконається,
# бо a > 0 вже "перехоплює" усі додатні числа, включно з 1
def buggy_demo():
    a = input('Введіть число: ')
    a = int(a)
    if a > 0:
        print('Число додатне')  # виведеться навіть якщо a == 1
    elif a == 1:
        print('Число дорівнює 1')  # НІКОЛИ не виконається
    else:
        print("a <= 0")


# Виправлений варіант: специфічніша перевірка йде першою
def fixed_demo():
    a = input('Введіть число: ')
    a = int(a)
    if a == 1:
        print('Число дорівнює 1')
    elif a > 0:
        print('Число додатне')
    else:
        print("a <= 0")


if __name__ == "__main__":
    check_even_demo()
    sign_demo()
    fixed_demo()
