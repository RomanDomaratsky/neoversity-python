# Тема: Регулярні вирази - метод re.findall()
# --------------------------------------------------
# re.findall(pattern, string) знаходить ВСІ входження шаблону
# і повертає список (порожній, якщо нічого не знайдено).

import re

# Знаходження всіх чисел у тексті
text = "Рік 2023 був складнішим, ніж 2022"
pattern = r"\d+"
matches = re.findall(pattern, text)
print(matches)  # ['2023', '2022']

# Знаходження всіх слів у тексті
text = "Python - це проста, але потужна мова програмування."
pattern = r"\w+"
matches = re.findall(pattern, text)
print(matches)  # ['Python', 'це', 'проста', 'але', 'потужна', 'мова', 'програмування']

# Знаходження всіх електронних адрес у тексті
# Практичне застосування: масовий парсинг/скрапінг тексту чи сторінок для
# збору контактних даних, наприклад під час аналізу листів або веб-сторінок.
text = "Контакти: example1@example.com, example2@sample.org"
pattern = r"\w+@\w+\.\w+"
matches = re.findall(pattern, text)
print(matches)  # ['example1@example.com', 'example2@sample.org']
