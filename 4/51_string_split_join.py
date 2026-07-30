# Тема: Поділ (split) та об'єднання (join) рядків
# --------------------------------------------------------

# split() - розбиває рядок на список підрядків (за замовчуванням - за пробілом)
text = "hello world"
result = text.split()
print(result)  # ['hello', 'world']

# split(separator) - розбиття за вказаним роздільником
text = "apple,banana,cherry"
result = text.split(',')
print(result)  # ['apple', 'banana', 'cherry']

# join() - об'єднання послідовності рядків через роздільник (зворотне до split)
list_of_strings = ['Hello', 'world']
result = ' '.join(list_of_strings)
print(result)  # Hello world

elements = ['earth', 'air', 'fire', 'water']
result = ', '.join(elements)
print(result)  # earth, air, fire, water


# --- Задача: розбір параметрів URL пошукового запиту ---
# Практичне застосування: саме так у веброзробці "розпаковують" query-параметри
# URL (наприклад, для логування пошукових запитів, аналітики або побудови API),
# перетворюючи рядок параметрів у зручний для роботи словник Python.
url_search = "https://www.google.com/search?q=Cat+and+dog&ie=utf-8&oe=utf-8&aq=t"

query = url_search.split('?')
print(query)  # q=Cat+and+dog&ie=utf-8&oe=utf-8&aq=t

obj_query = {}
for el in query.split('&'):
    key, value = el.split('=')
    obj_query.update({key: value.replace('+', ' ')})

print(obj_query)
# {'q': 'Cat and dog', 'ie': 'utf-8', 'oe': 'utf-8', 'aq': 't'}
