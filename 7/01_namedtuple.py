# Тема: Іменовані кортежі (namedtuple) з модуля collections
# ------------------------------------------------------------------------
# namedtuple дозволяє звертатися до елементів кортежу за ІМЕНЕМ, а не
# лише за індексом - це робить код зрозумілішим, коли елементів багато.

from collections import namedtuple

# Створення іменованого кортежу
Point = namedtuple('Point', ['x', 'y'])

p = Point(11, 22)
print(p.x)  # 11
print(p.y)  # 22


# Порівняння зі звичайним кортежем: person[0] нічого не каже про зміст
person_plain = ('Mick', 'Nitch', 35, 'Boston', '01146')
print(person_plain[0])  # 'Mick' - треба пам'ятати, що це саме ім'я


# Той самий приклад через namedtuple - зрозуміліше і безпечніше
import collections

Person = collections.namedtuple('Person', ['first_name', 'last_name', 'age', 'birth_place', 'post_index'])
person = Person('Mick', 'Nitch', 35, 'Boston', '01146')

print(person.first_name)  # Mick
print(person.post_index)  # 01146
print(person.age)         # 35
print(person[3])          # Boston (доступ за індексом теж працює)


# Практичне застосування: namedtuple зручний для передачі структурованих
# "записів" між функціями-обробниками (наприклад, рядок з бази даних чи
# результат парсингу) - читабельніше за словник і безпечніше за звичайний
# кортеж, бо неможливо випадково переплутати порядок полів.
Cat = collections.namedtuple('Cat', ['nickname', 'age', 'owner'])
cat = Cat('Simon', 4, 'Krabat')

print(f'This is {cat.nickname}, a {cat.age}-year-old cat. His owner is {cat.owner}')
# This is Simon, a 4-year-old cat. His owner is Krabat.

# Для порівняння - той самий вивід через індекси набагато менш зрозумілий:
print(f'This is {cat[0]}, a {cat[1]}-year-old cat. His owner is {cat[2]}')
