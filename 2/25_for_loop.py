# Тема: Цикл for
# ------------------
# Використовується для ітерації по елементах послідовності
# (список, кортеж, рядок тощо).

fruit = 'apple'
for char in fruit:
    print(char)
# a
# p
# p
# l
# e

alphabet = "abcdefghijklmnopqrstuvwxyz"
for char in alphabet:
    print(char, end=" ")
print()
# a b c d e f g h i j k l m n o p q r s t u v w x y z

some_iterable = ["a", "b", "c"]
for i in some_iterable:
    print(i)
# a
# b
# c

odd_numbers = [1, 3, 5, 7, 9]
for i in odd_numbers:
    print(i ** 2)
# 1
# 9
# 25
# 49
# 81


# Задача: підрахунок символів та пробілів у введеному рядку
def count_chars_and_spaces_demo():
    user_input = input("Введіть рядок: ")
    total_chars = len(user_input)  # загальна кількість символів у рядку
    space_count = 0  # кількість пробілів

    for char in user_input:
        if char == " ":
            space_count += 1

    print(f"Загальна кількість символів у рядку: {total_chars}")
    print(f"Кількість пробілів у рядку: {space_count}")


if __name__ == "__main__":
    count_chars_and_spaces_demo()
