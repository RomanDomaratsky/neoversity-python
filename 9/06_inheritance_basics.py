# Тема: Наслідування - базовий клас, похідні класи, super()
# ------------------------------------------------------------------------
# Наслідування дозволяє одному класу (похідному/subclass) переймати
# властивості та методи іншого класу (базового/батьківського/superclass).

class Animal:
    def __init__(self, nickname: str, age: int):
        self.nickname = nickname
        self.age = age

    def make_sound(self):
        pass


class Cat(Animal):
    def make_sound(self) -> str:
        return "Meow"


class Dog(Animal):
    def make_sound(self) -> str:
        return "Woof"


class Cow(Animal):
    def make_sound(self):
        return "Moo"


my_cat = Cat("Simon", 4)
my_dog = Dog("Rex", 5)
my_cow = Cow("Bessie", 3)

print(my_cat.make_sound())  # Meow
print(my_dog.make_sound())  # Woof
print(my_cow.make_sound())  # Moo


# --- Розширення похідного класу власним конструктором через super() ---
class DogWithBreed(Animal):
    def __init__(self, nickname: str, age: int, breed: str):
        super().__init__(nickname, age)  # Викликаємо конструктор базового класу
        self.breed = breed               # Додаємо нову властивість

    def make_sound(self) -> str:
        return "Woof"

    def chase_tail(self) -> str:
        return f"{self.nickname} is chasing its tail!"


my_dog2 = DogWithBreed("Rex", 5, "Golden Retriever")
print(my_dog2.make_sound())    # Woof
print(my_dog2.chase_tail())    # Rex is chasing its tail!

# Практичне застосування: базовий клас (наприклад, BaseModel, Vehicle,
# Employee) визначає спільні поля/методи один раз, а похідні класи
# (Car, Truck; Manager, Developer) додають лише свою специфіку - це
# зменшує дублювання коду (принцип DRY) і полегшує підтримку системи.
