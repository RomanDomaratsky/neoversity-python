# Тема: Функція filter() - вибір елементів, що задовольняють умову
# ------------------------------------------------------------------------
# Синтаксис: filter(function, iterable)
# function повертає True/False для кожного елемента; filter() лишає
# тільки ті елементи, для яких результат True.

even_nums = filter(lambda x: x % 2 == 0, range(1, 11))
print(list(even_nums))  # [2, 4, 6, 8, 10]


# filter() можна використовувати і зі звичайною (не лямбда) функцією
def is_positive(x):
    return x > 0


nums = [-2, -1, 0, 1, 2]
positive_nums = filter(is_positive, nums)
print(list(positive_nums))  # [1, 2]


# Практичний приклад: залишити тільки букви нижнього регістру в рядку
some_str = 'Видавництво А-БА-БА-ГА-ЛА-МА-ГА'
new_str = ''.join(list(filter(lambda x: x.islower(), some_str)))
print(new_str)  # идавництво


# --- Сучасна альтернатива: list comprehension замість filter() ---
nums = [1, 2, 3, 4, 5, 6]
even_nums = [x for x in nums if x % 2 == 0]
print(even_nums)  # [2, 4, 6]

some_str = 'Видавництво А-БА-БА-ГА-ЛА-МА-ГА'
new_str = ''.join([x for x in some_str if x.islower()])
print(new_str)  # идавництво
