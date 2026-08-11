# Тема: Модуль dataclasses - декларативне визначення класів даних
# ------------------------------------------------------------------------
# Декоратор @dataclass (Python 3.7+) автоматично генерує __init__ та інші
# магічні методи на основі оголошених атрибутів класу, усуваючи
# "бойлерплейт" код.

from dataclasses import dataclass


# --- Традиційний спосіб: ручне визначення __init__ ---
class PersonClassic:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age


# --- Той самий результат, але через @dataclass ---
@dataclass
class Person:
    name: str
    age: int


p = Person("Boris", 34)
print(p)  # Person(name='Boris', age=34) - __repr__ згенерований автоматично


# --- Атрибути зі стандартними значеннями ---
@dataclass
class Article:
    title: str
    author: str
    views: int = 0


article = Article("Python OOP", "Roman")
print(article)  # Article(title='Python OOP', author='Roman', views=0)


# --- Практичний приклад: Rectangle з методом area() ---
@dataclass
class Rectangle:
    width: int
    height: int

    def area(self) -> int:
        return self.width * self.height


rect1 = Rectangle(10, 5)
rect2 = Rectangle(7, 3)
rect3 = Rectangle(8, 6)

print(f"Площа прямокутника 1: {rect1.area()}")  # 50
print(f"Площа прямокутника 2: {rect2.area()}")  # 21
print(f"Площа прямокутника 3: {rect3.area()}")  # 48

# Практичне застосування: @dataclass ідеально підходить для сутностей
# бази даних (моделей), конфігураційних об'єктів та DTO (Data Transfer
# Object) для передачі даних між шарами системи чи через API - там, де
# основна мета класу - зберігати дані без складної логіки.
