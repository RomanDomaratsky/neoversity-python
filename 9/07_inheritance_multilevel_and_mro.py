# Тема: Багаторівневе наслідування та Method Resolution Order (MRO)
# ------------------------------------------------------------------------
# Багаторівневе наслідування - клас наслідує від класу, який сам є похідним,
# утворюючи "ланцюжок" наслідування.

class Animal:
    def __init__(self, nickname: str, age: int):
        self.nickname = nickname
        self.age = age

    def make_sound(self):
        pass


class Bird(Animal):
    def make_sound(self):
        return "Chirp"


class Parrot(Bird):
    def can_fly(self):
        return True


class TalkingParrot(Parrot):
    def say_phrase(self, phrase):
        return f"The parrot says: '{phrase}'"


my_parrot = TalkingParrot("Alice", 2)
print(my_parrot.make_sound())              # Chirp
print(my_parrot.can_fly())                 # True
print(my_parrot.say_phrase("Hello, World!"))  # The parrot says: 'Hello, World!'


# --- MRO: порядок пошуку методів/атрибутів при множинному наслідуванні ---
class A:
    pass


class B(A):
    pass


class C(A):
    pass


class D(B, C):
    pass


print(D.mro())
# [<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>,
#  <class '__main__.A'>, <class 'object'>]


# --- Наочний приклад впливу порядку батьків на MRO ---
class ClsA:
    name = "Я клас A"


class ClsB:
    name = "Я клас B"
    property = "Я знаходжусь в класі B"


class ClsC(ClsA, ClsB):
    property = "Я знаходжусь в класі C"


c = ClsC()
print(c.name)      # Я клас A (бо ClsA першим у списку батьків)
print(c.property)  # Я знаходжусь в класі C


class ClsC2(ClsB, ClsA):  # змінили порядок батьків
    property = "Я знаходжусь в класі C"


c2 = ClsC2()
print(c2.name)      # Я клас B (тепер ClsB першим у списку батьків)
print(c2.property)  # Я знаходжусь в класі C

# Практичне застосування: розуміння MRO критично важливе при множинному
# наслідуванні (наприклад, коли клас наслідує і від Mixin для логування, і
# від Mixin для серіалізації) - без нього легко отримати неочікуваний метод
# або атрибут, взятий "не з того" класу.
