# Тема: Інкапсуляція - private атрибути та name mangling
# ------------------------------------------------------------------------
# Private атрибути позначаються ДВОМА підкресленнями "__". Python не дає
# справжньої приватності - він лише "перетворює" ім'я (name mangling),
# щоб запобігти випадковому доступу ззовні.

class Person:
    def __init__(self, name: str, age: int, is_active: bool, is_admin: bool):
        self.name = name
        self.age = age
        self._is_active = is_active
        self.__is_admin = is_admin  # private

    def greeting(self):
        return f"Hi {self.name}"

    def is_active(self):
        return self._is_active

    def set_active(self, active: bool):
        self._is_active = active


p = Person("Boris", 34, True, False)

# Прямий доступ до __is_admin ззовні класу викликає помилку:
try:
    print(p.__is_admin)
except AttributeError as e:
    print(f"AttributeError: {e}")  # 'Person' object has no attribute '__is_admin'

# Але ім'я лише "перетворене" - доступ можливий через _КласІм'я:
print(p._Person__is_admin)  # False


# --- Правильний підхід: доступ до private поля через публічні методи ---
class PersonWithAdminAccessors:
    def __init__(self, name: str, age: int, is_active: bool, is_admin: bool):
        self.name = name
        self.age = age
        self._is_active = is_active
        self.__is_admin = is_admin

    def greeting(self):
        return f"Hi {self.name}"

    def is_active(self):
        return self._is_active

    def set_active(self, active: bool):
        self._is_active = active

    def get_is_admin(self):
        return self.__is_admin

    def set_is_admin(self, is_admin: bool):
        # Тут можна додати будь-яку логіку перевірки або обробки
        self.__is_admin = is_admin


p2 = PersonWithAdminAccessors("Boris", 34, True, False)
print(p2.get_is_admin())  # False
p2.set_is_admin(True)
print(p2.get_is_admin())  # True

# Практичне застосування: name mangling часто використовують у бібліотеках,
# щоб уберегти внутрішній стан об'єкта (наприклад, __cache, __connection)
# від випадкового перезаписування зовнішнім кодом чи класами-нащадками, які
# випадково оголосять поле з тим самим ім'ям.
