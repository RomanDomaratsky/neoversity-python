# Тема: Інкапсуляція - public та protected атрибути/методи
# ------------------------------------------------------------------------
# Інкапсуляція - приховування внутрішньої структури класу та захист даних
# від прямого доступу ззовні. В Python рівні доступу базуються на КОНВЕНЦІЯХ
# (немає справжніх модифікаторів доступу, як у Java):
#   Public    - без підкреслення, доступний звідусіль.
#   Protected - один underscore "_", доступ можливий, але вважається поганою
#               практикою звертатись до нього ззовні класу.
#   Private   - два underscore "__", ім'я "перетворюється" (name mangling).

# --- Public: доступ вільний з будь-якого місця ---
class PersonPublic:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def greeting(self) -> str:
        return f"Hi {self.name}"


p = PersonPublic("Boris", 34)
print(p.name, p.age)   # Boris 34 - вільний доступ до публічних полів
print(p.greeting())    # Hi Boris


# --- Protected: одне підкреслення, "не варто" читати/змінювати ззовні ---
class Person:
    def __init__(self, name: str, age: int, is_active: bool):
        self.name = name
        self.age = age
        self._is_active = is_active  # protected за конвенцією

    def greeting(self):
        return f"Hi {self.name}"


p = Person("Boris", 34, True)
print(p.name, p.age, p._is_active)  # Boris 34 True (технічно доступно, але погана практика)
print(p.greeting())                 # Hi Boris


# --- Правильний підхід: доступ до protected поля через публічні методи ---
class PersonWithAccessors:
    def __init__(self, name: str, age: int, is_active: bool):
        self.name = name
        self.age = age
        self._is_active = is_active

    def greeting(self):
        return f"Hi {self.name}"

    def is_active(self):
        return self._is_active

    def set_active(self, active: bool):
        self._is_active = active


p = PersonWithAccessors("Boris", 34, True)
print(p.name, p.age, p.is_active())  # Boris 34 True
print(p.greeting())                  # Hi Boris

# Практичне застосування: гетери/сетери (is_active/set_active) дозволяють
# додати логіку перевірки при зміні даних - наприклад, заборонити встановити
# від'ємний баланс рахунку або некоректний email, не даючи змінювати поле
# напряму без перевірки.
