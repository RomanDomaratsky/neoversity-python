# Тема: Цикл while, нескінченні цикли, break та continue
# -----------------------------------------------------------

# Базовий цикл while
k = 0
while k < 10:
    k = k + 1
    print(k)
# 1 2 3 4 5 6 7 8 9 10


# "Нескінченний" цикл із виходом через break
a = 0
while True:
    print(a)
    if a >= 20:
        break
    a = a + 1


# Echo-скрипт: виводить введене, доки не введуть "exit"
def echo_demo():
    while True:
        user_input = input()
        print(user_input)
        if user_input == "exit":
            break


# continue - пропускає інструкції, що залишились в ітерації
a = 0
while a < 6:
    a = a + 1
    if not a % 2:
        continue
    print(a)
# 1
# 3
# 5


# break/continue впливають тільки на цикл, у якому вони знаходяться.
# У вкладених циклах break виходить лише з внутрішнього циклу.
def countdown_demo():
    while True:
        number = input("number = ")
        number = int(number)
        while True:
            print(number)
            number = number - 1
            if number < 0:
                break
        # тут зовнішній цикл продовжує виконуватись нескінченно


# Використання break/continue поза циклом - SyntaxError (розкоментуй, щоб побачити):
# number = int(input("number = "))
# if number < 0:
#     break
