# Тема: Функція map() - застосування функції до кожного елемента
# ------------------------------------------------------------------------
# Синтаксис: map(function, iterable, ...)
# map() повертає ІТЕРАТОР (генератор), а не список.

numbers = [1, 2, 3, 4, 5]

# map() повертає ітератор - переберемо його в циклі for
for i in map(lambda x: x ** 2, numbers):
    print(i)
# 1 4 9 16 25 (кожне на своєму рядку)

# Якщо потрібен саме список - обгортаємо у list()
squared_nums = list(map(lambda x: x ** 2, numbers))
print(squared_nums)  # [1, 4, 9, 16, 25]

# map() з ДЕКІЛЬКОМА списками одночасно
nums1 = [1, 2, 3]
nums2 = [4, 5, 6]
sum_nums = map(lambda x, y: x + y, nums1, nums2)
print(list(sum_nums))  # [5, 7, 9]


# --- Сучасна альтернатива: list comprehension замість map() ---
# Після появи comprehensions їх часто обирають замість map() - код
# читається лінійно зліва праворуч, без "вкладеної" лямбди.
nums = [1, 2, 3, 4, 5]
squared_nums = [x * x for x in nums]
print(squared_nums)  # [1, 4, 9, 16, 25]

# Аналог map() з двома списками через zip() у comprehension
nums1 = [1, 2, 3]
nums2 = [4, 5, 6]
sum_nums = [x + y for x, y in zip(nums1, nums2)]
print(sum_nums)  # [5, 7, 9]
