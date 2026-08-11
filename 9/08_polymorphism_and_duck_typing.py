# Тема: Поліморфізм та качина типізація (Duck Typing)
# ------------------------------------------------------------------------
# Поліморфізм - об'єкти різних класів можуть мати метод з однаковою назвою,
# але різною реалізацією, і викликатись через спільний інтерфейс.

class Animal:
    def __init__(self, nickname: str, age: int):
        self.nickname = nickname
        self.age = age

    def make_sound(self):
        pass


class Cat(Animal):
    def make_sound(self):
        return "Meow"


class Dog(Animal):
    def make_sound(self):
        return "Woof"


def animal_sounds(animals):
    for animal in animals:
        print(animal.make_sound())


animals = [Cat("Simon", 4), Dog("Rex", 5)]
animal_sounds(animals)
# Meow
# Woof


# --- Качина типізація: важливо не тип об'єкта, а наявність потрібного методу ---
class Duck:
    def quack(self):
        print("Quack, quack!")


class Person:
    def quack(self):
        print("I'm Quacking Like a Duck!")


def make_it_quack(duck):
    duck.quack()


duck = Duck()
person = Person()
make_it_quack(duck)    # Quack, quack!
make_it_quack(person)  # I'm Quacking Like a Duck!


# --- Duck typing + статичні анотації типів через typing.Protocol ---
from typing import Protocol


class Speaker(Protocol):
    def speak(self) -> str:
        pass


class DogSpeaker:
    def speak(self) -> str:
        return "Woof"


class CatSpeaker:
    def speak(self) -> str:
        return "Meow"


class Robot:
    def speak(self) -> str:
        return "Beep boop"


def make_it_speak(speaker: Speaker) -> None:
    print(speaker.speak())


make_it_speak(DogSpeaker())  # Woof
make_it_speak(CatSpeaker())  # Meow
make_it_speak(Robot())       # Beep boop

# Практичне застосування: поліморфізм + duck typing дозволяють писати
# функції, що приймають "будь-що з потрібним методом" (наприклад, будь-який
# об'єкт з методом .write() підходить туди, де очікується файл, будь-який
# об'єкт з .render() підходить у систему рендерингу) - це основа гнучких,
# розширюваних архітектур без жорсткої прив'язки до конкретних класів.
