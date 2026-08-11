# Тема: Перелічуваний тип даних (Enum)
# ------------------------------------------------------------------------
# Enum - спосіб визначення набору іменованих констант замість магічних
# чисел/рядків. Робить код читабельнішим і безпечнішим.

from enum import Enum, auto


class Day(Enum):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7


today = Day.MONDAY
print(today)  # Day.MONDAY

if today == Day.MONDAY:
    print("Сьогодні понеділок.")
else:
    print("Сьогодні не понеділок.")

print(today.name)   # MONDAY
print(today.value)  # 1

day_from_value = Day(1)
print(day_from_value)  # Day.MONDAY


# --- Практичний приклад: статуси замовлень інтернет-магазину ---
class OrderStatus(Enum):
    NEW = auto()
    PROCESSING = auto()
    SHIPPED = auto()
    DELIVERED = auto()


class Order:
    def __init__(self, name: str, status: OrderStatus):
        self.name = name
        self.status = status

    def update_status(self, new_status: OrderStatus):
        self.status = new_status
        print(f"Замовлення '{self.name}' оновлено до статусу {self.status.name}.")

    def display_status(self):
        print(f"Статус замовлення '{self.name}': {self.status.name}.")


order1 = Order("Ноутбук", OrderStatus.NEW)
order2 = Order("Книга", OrderStatus.NEW)

order1.display_status()
order2.display_status()

order1.update_status(OrderStatus.PROCESSING)
order2.update_status(OrderStatus.SHIPPED)

order1.display_status()
order2.display_status()

# Практичне застосування: Enum ідеально підходить для обмежених наборів
# станів - статуси замовлень, ролі користувачів (USER/MODERATOR/ADMIN),
# дні тижня, коди помилок API - додавання нового значення (наприклад,
# CANCELED) не вимагає змін в іншому коді, що спирається на ці константи.
