# Тема: collections.UserString - модифіковані рядки
# ------------------------------------------------------------------------
# UserString дозволяє наслідувати поведінку звичайного рядка, додаючи
# нові методи або змінюючи стандартну поведінку.

from collections import UserString


class MyString(UserString):
    # Перевірка, чи рядок є паліндромом
    def is_palindrome(self):
        return self.data == self.data[::-1]


my_string = MyString("radar")
print("Рядок:", my_string)                       # Рядок: radar
print("Чи є паліндромом?", my_string.is_palindrome())  # True

another_string = MyString("hello")
print("Рядок:", another_string)                        # Рядок: hello
print("Чи є паліндромом?", another_string.is_palindrome())  # False


# --- Практичний приклад: рядок з обмеженням максимальної довжини ---
class TruncatedString(UserString):
    MAX_LEN = 7

    def truncate(self):
        self.data = self.data[:self.MAX_LEN]


ts = TruncatedString('hello world!')
ts.truncate()
print(ts)  # hello w

# Практичне застосування: корисно для валідації/нормалізації текстових
# полів - наприклад, обмеження довжини slug для URL, автоматичне усічення
# заголовків для прев'ю картки товару, або спеціалізовані "рядки-значення"
# (email, phone) з власними методами перевірки формату.
