# Тема: Регулярні вирази - метод re.search()
# ------------------------------------------------
# re.search(pattern, string) шукає ПЕРШЕ входження шаблону.
# Повертає об'єкт Match (з методами .group(), .span()) або None.

import re

# Простий пошук точного слова
text = "Вивчення Python може бути веселим."
pattern = "Python"
match = re.search(pattern, text)
if match:
    print("Знайдено:", match.group())
else:
    print("Не знайдено.")


# Пошук за шаблоном з метасимволами: слово, що починається на "в"
# і закінчується на "м" (\w* - нуль або більше "словесних" символів)
text = "Вивчення Python може бути веселим."
pattern = r"в\w*м"
match = re.search(pattern, text, re.IGNORECASE)
if match:
    print("Знайдено:", match.group())


# Пошук електронної адреси в тексті
# Практичне застосування: базова валідація/пошук email у формах
# зворотного зв'язку, парсингу листів або перевірці введених даних
# перед збереженням у базу.
text = "Моя електронна адреса: example@example.com"
pattern = r"\w+@\w+\.\w+"
match = re.search(pattern, text)
if match:
    print("Електронна адреса:", match.group())


# Групи в регулярних виразах: розділення email на ім'я користувача й домен
email = "username@domain.com"
pattern = r"(\w+)@(\w+\.\w+)"
match = re.search(pattern, email)
if match:
    user_name = match.group(1)
    domain_name = match.group(2)
    print("Ім'я користувача:", user_name)
    print("Домен:", domain_name)
