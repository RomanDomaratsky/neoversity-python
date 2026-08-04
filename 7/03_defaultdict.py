# Тема: defaultdict з модуля collections - значення за замовчуванням для нових ключів
# ------------------------------------------------------------------------------------
# У звичайному dict доступ до неіснуючого ключа викидає KeyError.
# defaultdict автоматично створює значення за замовчуванням через "фабричну" функцію.

from collections import defaultdict

# defaultdict(list) - для кожного нового ключа автоматично створюється []
d = defaultdict(list)
d['a'].append(1)
d['a'].append(2)
d['b'].append(4)
print(d)  # defaultdict(<class 'list'>, {'a': [1, 2], 'b': [4]})

# defaultdict(int) - для кожного нового ключа автоматично 0
d = defaultdict(int)
d['a'] += 1
d['b'] += 1
d['a'] += 1
print(d)  # defaultdict(<class 'int'>, {'a': 2, 'b': 1})


# --- Практична задача: групування слів за першою літерою ---

# Без defaultdict - потрібна ручна перевірка існування ключа
words = ['apple', 'zoo', 'lion', 'lama', 'bear', 'bet', 'wolf', 'appendix']
grouped_words = {}
for word in words:
    char = word[0]
    if char not in grouped_words:
        grouped_words[char] = []
    grouped_words[char].append(word)
print(grouped_words)
# {'a': ['apple', 'appendix'], 'z': ['zoo'], 'l': ['lion', 'lama'],
#  'b': ['bear', 'bet'], 'w': ['wolf']}


# Той самий результат через defaultdict - без перевірки "чи є ключ"
# Практичне застосування: групування записів за категорією/датою/ID -
# дуже поширена задача при обробці логів, звітів чи результатів запитів до БД.
grouped_words = defaultdict(list)
for word in words:
    char = word[0]
    grouped_words[char].append(word)
print(dict(grouped_words))



# Real-world data: E-commerce orders
orders = [
    {"customer": "Alice", "item": "Laptop"},
    {"customer": "Bob", "item": "Mouse"},
    {"customer": "Alice", "item": "Keyboard"},
]

# Grouping items by customer
customer_orders = defaultdict(list)

for order in orders:
    # No if-else check needed
    customer_orders[order["customer"]].append(order["item"])

print(dict(customer_orders))
# Output: {'Alice': ['Laptop', 'Keyboard'], 'Bob': ['Mouse']}
