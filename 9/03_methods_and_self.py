# Тема: Методи класу, self та конструктор __init__
# ------------------------------------------------------------------------
# Метод класу - функція, що оперує полями класу та/або своїми аргументами.
# Перший аргумент методу завжди сам об'єкт - за конвенцією називається self.
# __init__ - спеціальний метод-конструктор, викликається автоматично під
# час створення нового екземпляра класу.

class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def say_name(self) -> None:
        print(f'Hi! I am {self.name} and I am {self.age} years old.')

    def set_age(self, age: int) -> None:
        self.age = age


bob = Person('Boris', 34)
bob.say_name()   # Hi! I am Boris and I am 34 years old.
bob.set_age(25)
bob.say_name()   # Hi! I am Boris and I am 25 years old.


# --- Практичний приклад: клас Pokemon з декількома методами ---
class Pokemon:
    def __init__(self, name, type, health):
        self.name = name      # Ініціалізація атрибута імені
        self.type = type      # Ініціалізація атрибута типу
        self.health = health  # Ініціалізація атрибута здоров'я

    def attack(self, other_pokemon):
        print(f"{self.name} attacks {other_pokemon.name}!")

    def dodge(self):
        print(f"{self.name} dodged the attack!")

    def evolve(self, new_form):
        print(f"{self.name} is evolving into {new_form}!")
        self.name = new_form


# Створення об'єкта Pikachu
pikachu = Pokemon("Pikachu", "Electric", 100)

# Використання методів
pikachu.attack(Pokemon("Charmander", "Fire", 100))  # Pikachu attacks Charmander!
pikachu.dodge()          # Pikachu dodged the attack!
pikachu.evolve("Raichu")  # Pikachu is evolving into Raichu!

# Практичне застосування: такий підхід (клас з полями стану та методами дій)
# лежить в основі моделювання будь-яких сутностей з поведінкою - персонажів
# гри, замовлень з методами оплати/скасування, банківського рахунку з
# методами пополнення/списання коштів тощо.
