# Тема: Робота з випадковими величинами (модуль random)
# --------------------------------------------------------------

import random

# randint(a, b) - випадкове ціле число N, де a <= N <= b
print(random.randint(1, 1000))

dice_roll = random.randint(1, 6)
print(f"Ви кинули {dice_roll}")

# random() - випадкове дійсне число в [0.0, 1.0)
num = random.random()
print(num)

fill_percentage = random.random() * 100
print(f"Заповнення: {fill_percentage:.2f}%")

# randrange(start, stop[, step]) - випадкове число із заданого діапазону
print(random.randrange(10))  # від 0 до 9

target = random.randrange(1, 11, 2)  # тільки непарні від 1 до 9
print(f"Ціль: {target}")

# shuffle(x) - перемішує список x "на місці"
cards = ["Туз", "Король", "Дама", "Валет", "10", "9", "8", "7", "6"]
random.shuffle(cards)
print(f"Перемішана колода: {cards}")

# choice(seq) - випадковий елемент зі списку/кортежу
fruits = ['apple', 'banana', 'orange']
print(random.choice(fruits))

# choices(population, weights=None, cum_weights=None, k=1) - вибірка з повтореннями
items = ['яблуко', 'банан', 'вишня', 'диня']
chosen_item = random.choices(items, k=1)
print(chosen_item)

numbers = [1, 2, 3, 4, 5]
chosen_numbers = random.choices(numbers, k=3)
print(chosen_numbers)

# Вибір із вагами - 'червоний' має набагато більшу ймовірність
colors = ['червоний', 'зелений', 'синій']
weights = [10, 1, 1]
chosen_color = random.choices(colors, weights, k=1)
print(chosen_color)

# sample(population, k) - k УНІКАЛЬНИХ елементів (без повторень)
participants = ['Анна', 'Богдан', 'Віктор', 'Галина', 'Дмитро',
                'Олена', 'Женя', 'Зорян', 'Ігор', 'Йосип']
team = random.sample(participants, 4)
print(f"Команда: {team}")

# uniform(a, b) - випадкове дійсне число N, де a <= N <= b
price = random.uniform(50, 100)
print(f"Випадкова ціна: {price:.2f}")


random.seed(42)
print(random.randint(1, 100))

random.seed(42)
print(random.randint(1, 100))