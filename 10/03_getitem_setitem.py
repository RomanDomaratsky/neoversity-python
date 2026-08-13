# Тема: Магічні методи __getitem__ та __setitem__
# ------------------------------------------------------------------------
# Дозволяють об'єкту імітувати поведінку контейнерів (списків, словників)
# при доступі через квадратні дужки obj[key].
# __getitem__(self, key) - читання obj[key]
# __setitem__(self, key, value) - запис obj[key] = value

class SimpleDict:
    def __init__(self):
        self.__data = {}

    def __getitem__(self, key):
        return self.__data.get(key, "Key not found")

    def __setitem__(self, key, value):
        self.__data[key] = value


simple_dict = SimpleDict()
simple_dict['name'] = 'Boris'
print(simple_dict['name'])  # Boris
print(simple_dict['age'])   # Key not found


# --- Практичний приклад: список з обмеженням значень (наприклад, температур) ---
class BoundedList:
    def __init__(self, min_value: int, max_value: int):
        self.min_value = min_value
        self.max_value = max_value
        self.__data = []

    def __getitem__(self, index: int):
        return self.__data[index]

    def __setitem__(self, index: int, value: int):
        if not (self.min_value <= value <= self.max_value):
            raise ValueError(f"Value {value} must be between {self.min_value} and {self.max_value}")
        if index >= len(self.__data):
            self.__data.append(value)
        else:
            self.__data[index] = value

    def __repr__(self):
        return f"BoundedList({self.max_value}, {self.min_value})"

    def __str__(self):
        return str(self.__data)


if __name__ == '__main__':
    temperatures = BoundedList(18, 26)

    for i, el in enumerate([20, 22, 25, 27]):
        try:
            temperatures[i] = el
        except ValueError as e:
            print(e)

    print(temperatures)
    # Value 27 must be between 18 and 26
    # [20, 22, 25]


# --- Той самий підхід, побудований поверх UserList (менше коду) ---
from collections import UserList


class BoundedUserList(UserList):
    def __init__(self, min_value: int, max_value: int, initial_list=None):
        super().__init__(initial_list if initial_list is not None else [])
        self.min_value = min_value
        self.max_value = max_value
        self.__validate_list()

    def __validate_list(self):
        for item in self.data:
            self.__validate_item(item)

    def __validate_item(self, item):
        if not (self.min_value <= item <= self.max_value):
            raise ValueError(f"Item {item} must be between {self.min_value} and {self.max_value}")

    def append(self, item):
        self.__validate_item(item)
        super().append(item)

    def insert(self, i, item):
        self.__validate_item(item)
        super().insert(i, item)

    def __setitem__(self, i, item):
        self.__validate_item(item)
        super().__setitem__(i, item)

    def __repr__(self):
        return f"BoundedList({self.max_value}, {self.min_value})"

    def __str__(self):
        return str(self.data)


if __name__ == '__main__':
    temps2 = BoundedUserList(18, 26, [19, 21, 22])
    print(temps2)  # [19, 21, 22]

    for el in [20, 22, 25, 27]:
        try:
            temps2.append(el)
        except ValueError as e:
            print(e)

    print(temps2)
    # Item 27 must be between 18 and 26
    # [19, 21, 22, 20, 22, 25]

# Примітка: __getitem__ тут не перевизначався - UserList вже надає його
# стандартну поведінку. Його можна перевизначити додатково, наприклад для
# логування доступу до елементів (print перед super().__getitem__(index)).

# Практичне застосування: власна індексація корисна для типізованих
# колекцій з бізнес-правилами - наприклад, список температур з допустимим
# діапазоном, чергу замовлень з обмеженням розміру, або "розумний" словник
# конфігурації, що логує кожне звернення до параметра.
