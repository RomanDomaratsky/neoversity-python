# Тема: Атрибут класу vs поле об'єкта (instance field)
# ------------------------------------------------------------------------
# Атрибут класу - змінна на рівні класу, спільна для ВСІХ екземплярів.
# Поле об'єкта (instance field) - змінна на рівні конкретного екземпляра,
# у кожного об'єкта своя власна копія.

# --- Атрибут класу ---
class MyClassAttr:
    class_attribute = "I am a class attribute"


print(MyClassAttr.class_attribute)
print(MyClassAttr().class_attribute)


# --- Поле об'єкта (задається в __init__ через self) ---
class MyClassField:
    def __init__(self, value):
        self.instance_field = value  # Поле об'єкта


obj1 = MyClassField(5)
obj2 = MyClassField(10)
print(obj1.instance_field)  # 5
print(obj2.instance_field)  # 10 (незалежно від obj1)


# --- Наочна різниця: атрибут класу спільний, поле - персональне ---
class Person:
    count = 0  # атрибут класу - рахує всіх створених людей

    def __init__(self, name: str):
        self.name = name  # поле об'єкта - персональне ім'я
        Person.count += 1

    def how_many_persons(self):
        print(f"Кількість людей зараз {Person.count}")


first = Person('Boris')
first.how_many_persons()  # Кількість людей зараз 1
second = Person('Alex')
first.how_many_persons()  # Кількість людей зараз 2


# --- Якщо поле об'єкта має те саме ім'я, що і атрибут класу - воно
#     "перекриває" атрибут класу при доступі через об'єкт ---
class PersonA:
    count = 0

    def __init__(self):
        pass


person_a = PersonA()
print(person_a.count)  # 0 - атрибут класу видно, поля з таким ім'ям немає


class PersonB:
    count = 0

    def __init__(self):
        self.count = 10  # створює НОВЕ поле об'єкта, а не змінює атрибут класу


person_b = PersonB()
print(person_b.count)   # 10 - значення поля об'єкта
print(PersonB.count)    # 0  - атрибут класу лишився незмінним


# --- Присвоєння атрибуту напряму на екземплярі теж створює поле об'єкта ---
class PersonC:
    count = 0


person_c = PersonC()
person_c.count = 10
print(person_c.count)   # 10 - поле об'єкта person_c
print(PersonC.count)    # 0  - атрибут класу PersonC

# Практичне застосування: атрибути класу зручні для лічильників екземплярів,
# спільних конфігурацій або констант (наприклад, MAX_CONNECTIONS = 100),
# а поля об'єкта - для даних, унікальних для кожного об'єкта (ім'я, id, стан).
