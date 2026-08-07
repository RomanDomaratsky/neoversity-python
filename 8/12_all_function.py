# Тема: Функція all() - True, тільки якщо УСІ елементи істинні
# ------------------------------------------------------------------------
# УВАГА: для ПОРОЖНЬОГО об'єкта ітерації all() повертає True!

nums = [1, 2, 3, 4]
result = all(nums)
print(result)  # True (усі числа істинні, тобто не 0)

# all() з генераторним виразом: чи всі числа парні?
nums = [1, 2, 3, 4]
is_all_even = all(x % 2 == 0 for x in nums)
print(is_all_even)  # False (1 і 3 - непарні)

# Чи всі слова у списку написані з великої букви?
words = ["Hello", "World", "Python"]
is_all_title_case = all(word.istitle() for word in words)
print(is_all_title_case)  # True

# Практичне застосування: перевірка валідності форми/вхідних даних -
# наприклад, "усі обов'язкові поля заповнені" замість циклу з прапорцем.
required_fields = {"name": "Олена", "email": "olena@example.com", "age": "25"}
all_filled = all(value.strip() for value in required_fields.values())
print(all_filled)  # True
