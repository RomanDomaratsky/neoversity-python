# Тема: Метод isdigit() - перевірка, чи рядок складається з цифр
# --------------------------------------------------------------------

number = "12345"
print(number.isdigit())  # True

text = "Number123"
print(text.isdigit())  # False


# Практичне застосування: isdigit() - швидкий і поширений спосіб
# валідації введення користувача в консольних програмах та формах,
# перш ніж перетворювати рядок у число (int).
def validate_user_number_demo():
    user_input = input("Введіть число: ")
    if user_input.isdigit():
        print("Це дійсно число!")
    else:
        print("Це не число!")


# Перевірка кожного символу рядка окремо
for char in "Hello 123":
    if char.isdigit():
        print(f"'{char}' - це цифра")
    else:
        print(f"'{char}' - не цифра")


if __name__ == "__main__":
    validate_user_number_demo()
