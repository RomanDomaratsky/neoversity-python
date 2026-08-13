# Тема: Магічний метод __init__
# ------------------------------------------------------------------------
# Магічні методи - методи для реалізації перевантаження операторів та інших
# спеціальних механізмів. Їх імена завжди починаються і закінчуються "__".
# __init__ - конструктор, викликається автоматично одразу після створення
# порожнього об'єкта, і використовується для його ініціалізації.

class Human:
    def __init__(self, name: str, age: int = 0):
        self.name = name
        self.age = age

    def say_hello(self) -> str:
        return f'Hello! I am {self.name}'


bill = Human('Bill')
print(bill.say_hello())  # Hello! I am Bill
print(bill.age)          # 0

jill = Human('Jill', 20)
print(jill.say_hello())  # Hello! I am Jill
print(jill.age)          # 20


# --- __init__ може виконувати додаткову логіку, а не лише присвоєння полів ---
class HumanWithCheck:
    def __init__(self, name: str, age: int = 0):
        self.name = name
        self.age = age
        # Виклик методу під час ініціалізації
        self.is_adult = self.__check_adulthood()

        # Приклад логування
        print(f"Створено Human: {self.name}, Вік: {self.age}, Дорослий: {self.is_adult}")

    def say_hello(self) -> str:
        return f'Hello! I am {self.name}'

    def __check_adulthood(self) -> bool:
        return self.age >= 18


bill2 = HumanWithCheck('Bill')
print(bill2.say_hello())
print(f"Вік: {bill2.age}, Дорослий: {bill2.is_adult}")

jill2 = HumanWithCheck('Jill', 20)
print(jill2.say_hello())
print(f"Вік: {jill2.age}, Дорослий: {jill2.is_adult}")

# Практичне застосування: __init__ часто виконує не лише присвоєння полів,
# а й валідацію вхідних даних, обчислення похідних значень (як is_adult
# тут), підключення до ресурсів (з'єднання з БД, відкриття файлу) або
# логування створення важливих об'єктів системи (наприклад, транзакцій).
