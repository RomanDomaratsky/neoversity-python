# Тема: Гетери та сетери через декоратор @property
# ------------------------------------------------------------------------
# @property перетворює метод-гетер на "поле" (виклик без дужок).
# @<ім'я>.setter визначає сетер для того самого імені - дозволяє
# валідацію/обробку значення перед присвоєнням.

class Person:
    def __init__(self, age):
        self.__age = age  # Пряме присвоєння - БЕЗ валідації (проблема нижче)

    @property
    def age(self):
        return self.__age  # Геттер повертає значення приватного поля

    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError("Вік не може бути від'ємним")
        self.__age = value


if __name__ == "__main__":
    person = Person(10)
    print(person.age)  # 10
    try:
        person.age = -5  # сетер спрацьовує і валідує
    except ValueError as e:
        print(f"ValueError: {e}")

    # ПРОБЛЕМА: конструктор присвоює __age напряму, минаючи сетер,
    # тому невалідне значення при СТВОРЕННІ об'єкта не ловиться:
    bad_person = Person(-10)
    print(bad_person.age)  # -10 (!) - валідація не спрацювала


# --- Виправлення: конструктор має йти через сетер (self.age = age) ---
class PersonFixed:
    def __init__(self, age):
        self.__age = None
        # Використовуємо сеттер для встановлення віку - це вмикає валідацію
        self.age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError("Вік не може бути від'ємним")
        self.__age = value


if __name__ == "__main__":
    try:
        bad_person_fixed = PersonFixed(-10)
    except ValueError as e:
        print(f"ValueError: {e}")  # Тепер помилка ловиться одразу при створенні


# --- Переписаний приклад інкапсуляції з попередньої лекції через property ---
class PersonEncapsulated:
    def __init__(self, name: str, age: int, is_active: bool, is_admin: bool):
        self.name = name
        self.age = age
        self._is_active = None
        self.__is_admin = None
        self._is_active = is_active
        self.__is_admin = is_admin

    @property
    def is_active(self):
        return self._is_active

    @is_active.setter
    def is_active(self, value: bool):
        self._is_active = value

    @property
    def is_admin(self):
        return self.__is_admin

    @is_admin.setter
    def is_admin(self, value: bool):
        self.__is_admin = value

    def greeting(self):
        return f"Hi {self.name}"


if __name__ == "__main__":
    p = PersonEncapsulated("Boris", 34, True, False)
    print(p.is_admin)   # False - геттер
    p.is_admin = True   # сеттер
    print(p.is_admin)   # True

# Практичне застосування: @property - стандартний спосіб додати валідацію
# "заднім числом" без ламання зовнішнього API класу (обʼєкт.поле лишається
# обʼєкт.поле, хоча всередині вже виконується перевірка) - наприклад, для
# балансу рахунку, email, або відсотка знижки, який має бути в межах 0-100.
