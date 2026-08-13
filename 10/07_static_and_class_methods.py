# Тема: Статичні методи (@staticmethod) та класові методи (@classmethod)
# ------------------------------------------------------------------------
# Обидва можна викликати без створення екземпляра класу.
# @staticmethod - НЕ має доступу ані до self, ані до cls. "Допоміжна"
#                 функція, логічно пов'язана з класом.
# @classmethod  - отримує cls (сам клас) першим аргументом. Часто
#                 використовується для фабричних методів (альтернативних
#                 конструкторів).

class Geometry:
    PI = 3.14159

    @staticmethod
    def area_of_circle(radius):
        return Geometry.PI * radius ** 2


print(Geometry.area_of_circle(5))  # 78.53975


class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    @classmethod
    def from_string(cls, employee_info):
        name, position = employee_info.split(',')
        return cls(name, position)


employee_info = "John Doe,Manager"
john_doe = Employee.from_string(employee_info)

print(john_doe.name)      # John Doe
print(john_doe.position)  # Manager

# Практичне застосування: @staticmethod - для утилітних функцій, логічно
# приналежних класу (наприклад, Validator.is_valid_email(email)).
# @classmethod - для альтернативних конструкторів: User.from_json(data),
# Config.from_file(path), Date.from_timestamp(ts) - різні способи створити
# об'єкт класу, крім стандартного __init__.
