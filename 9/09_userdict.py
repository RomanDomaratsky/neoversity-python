# Тема: collections.UserDict - модифіковані словники
# ------------------------------------------------------------------------
# Наслідування безпосередньо від dict/list/str може призводити до
# неочікуваних помилок. Правильний спосіб отримати "кастомний" контейнер -
# використати UserDict/UserList/UserString з модуля collections. Дані
# зберігаються у полі self.data, а сам клас поводиться як звичайний
# контейнер.

from collections import UserDict


class MyDictionary(UserDict):
    # Приклад додавання нового методу
    def add_key(self, key, value):
        self.data[key] = value


my_dict = MyDictionary({'a': 1, 'b': 2})
my_dict.add_key('c', 3)
print(my_dict)  # {'a': 1, 'b': 2, 'c': 3}


# --- Практичний приклад: клас Customer з методами доступу до контактів ---
contacts = [
    {
        "name": "Allen Raymond",
        "email": "nulla.ante@vestibul.co.uk",
        "phone": "(992) 914-3792",
        "favorite": False,
    },
    {
        "name": "Chaim Lewis",
        "email": "dui.in@egetlacus.ca",
        "phone": "(294) 840-6685",
        "favorite": False,
    },
    {
        "name": "Kennedy Lane",
        "email": "mattis.Cras@nonenimMauris.net",
        "phone": "(542) 451-7038",
        "favorite": True,
    }
]


class Customer(UserDict):
    def phone_info(self):
        return f"{self.get('name')}: {self.get('phone')}"

    def email_info(self):
        return f"{self.get('name')}: {self.get('email')}"


if __name__ == "__main__":
    customers = [Customer(el) for el in contacts]

    print("---------------------------")

    for customer in customers:
        print(customer.phone_info())

    print("---------------------------")

    for customer in customers:
        print(customer.email_info())

# Практичне застосування: такий підхід зручний, коли треба перетворити
# "сирі" словники (наприклад, отримані з JSON відповіді API або з CSV) у
# об'єкти з власними методами доступу/форматування, зберігаючи всю звичну
# поведінку dict (get, ключі, items тощо).
