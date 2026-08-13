# Тема: Функтори та магічний метод __call__
# ------------------------------------------------------------------------
# Функтор - об'єкт класу, який можна викликати як функцію: object(args).
# Реалізується через магічний метод __call__. Функтори можуть зберігати
# стан між викликами, на відміну від звичайних функцій.

class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, other):
        return self.factor * other


double = Multiplier(2)
triple = Multiplier(3)

print(double(5))  # 10
print(triple(3))  # 9


# --- Функтор зі станом: лічильник викликів ---
class Counter:
    def __init__(self):
        self.count = 0

    def __call__(self, *args, **kwargs):
        self.count += 1


counter = Counter()
counter()
counter()
print(f"Викликано {counter.count} разів")  # Викликано 2 разів


# --- Функтор зі складною логікою: калькулятор з операцією, заданою при створенні ---
class SmartCalculator:
    def __init__(self, operation='add'):
        self.operation = operation

    def __call__(self, a, b):
        if self.operation == 'add':
            return a + b
        elif self.operation == 'subtract':
            return a - b
        else:
            raise ValueError("Невідома операція")


add = SmartCalculator('add')
print(add(5, 3))  # 8

subtract = SmartCalculator('subtract')
print(subtract(10, 7))  # 3

# Практичне застосування: функтори використовують для "параметризованих
# функцій" з внутрішнім станом - наприклад, кешуючий обчислювач, callback з
# конфігурацією (event handler з прив'язаними налаштуваннями), стратегія
# обробки даних, обрана під час ініціалізації об'єкта.
