# Тема: Створення власного ітератора та генератора
# ------------------------------------------------------------------------
# Ітератор реалізує __iter__() (повертає self) та __next__() (повертає
# наступний елемент, або викидає StopIteration, коли елементи закінчились).
# Ітератор можна перебрати лише ОДИН раз - це "одноразовий" об'єкт.
# Генератор (функція з yield) - спрощений спосіб створити ітератор:
# Python автоматично реалізує __iter__()/__next__() за вас.

class CountDown:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current == 0:
            raise StopIteration
        self.current -= 1
        return self.current


if __name__ == '__main__':
    counter = CountDown(5)
    for count in counter:
        print(count)
    # 4 3 2 1 0


# --- Той самий результат через генератор (менше коду) ---
def count_down(start):
    current = start
    current -= 1
    while current >= 0:
        yield current
        current -= 1


print("--- generator version ---")
for count in count_down(5):
    print(count)
# 4 3 2 1 0


# --- Практичний приклад: ітератор випадкових чисел з обмеженою кількістю ---
from random import randint, seed


class RandIterator:
    def __init__(self, start, end, quantity):
        self.start = start
        self.end = end
        self.quantity = quantity
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.count += 1
        if self.count > self.quantity:
            raise StopIteration
        else:
            return randint(self.start, self.end)


if __name__ == '__main__':
    print("--- RandIterator (значення випадкові, seed=1 для відтворюваності) ---")
    seed(1)
    my_random_list = RandIterator(1, 20, 5)
    for rn in my_random_list:
        print(rn, end=' ')
    print()


# --- Той самий результат через генератор ---
def rand_generator(start, end, quantity):
    count = 0
    while count < quantity:
        yield randint(start, end)
        count += 1


print("--- rand_generator (значення випадкові, seed=1 для відтворюваності) ---")
seed(1)
for rn in rand_generator(1, 20, 5):
    print(rn, end=' ')
print()

# Практичне застосування: власні ітератори/генератори корисні для лінивого
# читання великих файлів рядок за рядком, пагінації результатів API
# (сторінка за сторінкою без завантаження всього одразу), або генерації
# тестових/випадкових даних без зберігання всього набору в пам'яті.
