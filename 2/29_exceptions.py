# Тема: Винятки (exceptions) та try/except/else/finally
# --------------------------------------------------------------

# int("a") викличе ValueError - розкоментуй, щоб побачити:
# int("a")

# Приклади помилок, що призводять до різних винятків:
# 2 / 'a'      -> TypeError
# int("a")     -> ValueError
# 1 / 0        -> ZeroDivisionError

# Основні типи винятків:
# SyntaxError      - синтаксична помилка
# IndentationError - помилка виділення блоків пробілами
# TabError         - змішування табуляцій і пробілів
# TypeError        - операція неможлива для даного типу
# ValueError       - тип відповідний, але значення некоректне
# ZeroDivisionError - ділення на нуль


# Механізм обробки винятків: try / except / else / finally
val = 'a'
try:
    val = int(val)
except ValueError:
    print(f"val {val} is not a number")
else:
    print(val > 0)
finally:
    print("This will be printed anyway")


# Приклад: обробка введення користувача з перевіркою на повноліття
def age_check_demo():
    age = input("How old are you? ")
    try:
        age = int(age)
        if age >= 18:
            print("You are adult.")
        else:
            print("You are infant")
    except ValueError:
        print(f"{age} is not a number")


if __name__ == "__main__":
    age_check_demo()
