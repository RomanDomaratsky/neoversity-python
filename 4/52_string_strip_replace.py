# Тема: strip/lstrip/rstrip, replace, removeprefix/removesuffix
# ------------------------------------------------------------------------

# strip() - видаляє пробіли на початку і в кінці рядка
clean = '   spacious   '.strip()
print(clean)  # "spacious"

# lstrip() - тільки зліва, rstrip() - тільки справа
print('   spacious   '.lstrip())  # "spacious   "
print('   spacious   '.rstrip())  # "   spacious"

# Практичне застосування: strip() незамінний при обробці введених
# користувачем даних (наприклад, з форми або файлу CSV), де випадкові
# пробіли на краях можуть зламати подальше порівняння чи валідацію.
user_input = "   alice@example.com  \n"
cleaned_email = user_input.strip()
print(cleaned_email)  # "alice@example.com"


# replace(old, new, count=-1) - заміна підрядка (повертає НОВИЙ рядок)
text = "Hello world"
new_text = text.replace("world", "Python")
print(new_text)  # Hello Python

# Обмеження кількості замін
text = "one fish, two fish, red fish, blue fish"
new_text = text.replace("fish", "bird", 2)
print(new_text)  # one bird, two bird, red fish, blue fish

# replace() для видалення підрядка (заміна на порожній рядок)
text = "Hello, world!"
new_text = text.replace(" world", "")
print(new_text)  # Hello,!

# removeprefix() - видаляє фіксований префікс (якщо він є)
print('TestHook'.removeprefix('Test'))  # Hook
print('TestHook'.removeprefix('Hook'))  # TestHook (не змінюється - не префікс)

# removesuffix() - видаляє фіксований суфікс (якщо він є)
print('TestHook'.removesuffix('Test'))  # TestHook (не змінюється - не суфікс)
print('TestHook'.removesuffix('Hook'))  # Test
