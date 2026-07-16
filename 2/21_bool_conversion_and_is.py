# Тема: Приведення до bool та оператор is
# ---------------------------------------------

# Правило 1: число 0 приводиться до False
money = 0
if money:
    print(f"You have {money} on your bank account")
else:
    print("You have no money and no debts")
# You have no money and no debts

# Правило 2: None приводиться до False
result = None
if result:
    print(result)
else:
    print("Result is None, do something")
# Result is None, do something


def empty_string_demo():
    # Правило 3: порожній рядок/контейнер приводиться до False
    user_name = input("Enter your name: ")
    if user_name:
        print(f"Hello {user_name}")
    else:
        print("Hi Anonym!")


# Правило останнє: усе інше приводиться до True


# --- Оператор is ---
# is перевіряє, чи два імені вказують на ОДИН і той самий об'єкт у пам'яті
# (на відміну від ==, який перевіряє рівність значень)
a = [1, 2, 3]
b = a
c = [1, 2, 3]
print(a is b)  # True  (b - той самий об'єкт, що і a)
print(a is c)  # False (c - новий об'єкт з такими самими значеннями)

# Основне застосування is - перевірка на None
my_var = None
if my_var is None:
    print("my_var є None")


if __name__ == "__main__":
    empty_string_demo()
