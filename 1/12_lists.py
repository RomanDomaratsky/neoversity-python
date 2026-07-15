# Тема: Списки (Lists)
# ------------------------
# Список - впорядкований змінюваний контейнер даних.

# Два способи створити порожній список
my_list = list()
empty_list = []

# Створення списку з елементами
my_list = [1, 2, 3, 4, 5]
print(my_list)  # [1, 2, 3, 4, 5]

# Список може містити різні типи даних
my_list = [1, "Hello", "Hello", 3.14]
print(my_list)  # [1, 'Hello', 3.14]

# append() - додає елемент у кінець списку
my_list.append(67)
print(my_list)  # [1, 'Hello', 3.14, 4]

# remove() - видаляє перше входження елемента зі списку
my_list.remove("Hello")
print(my_list)  # [1, 3.14, 4]

# Доступ до елементів за індексом (індексація з 0)
some_iterable = ["a", "b", "c"]
first_letter = some_iterable[0]   # "a"
middle_one = some_iterable[1]     # "b"
last_letter = some_iterable[2]    # "c"
print(first_letter, middle_one, last_letter)

# Індексація з кінця (від -1)
some_iterable = ["a", "b", "c"]
first_letter = some_iterable[-3]  # "a"
middle_one = some_iterable[-2]    # "b"
last_letter = some_iterable[-1]   # "c"
print(first_letter, middle_one, last_letter)

# Зміна елемента списку за індексом (властивість змінності)
some_iterable = [1, 2, 3]
some_iterable[1] = -2
print(some_iterable)  # [1, -2, 3]

# pop(i) - повертає елемент за індексом і видаляє його зі списку
chars = ['a', 'b', 'c']
last = chars.pop(1)
print(last, chars)  # b ['a', 'c']

# extend() - розширює список елементами іншого списку
chars = ['a', 'b', 'c']
numbers = [1, 2]
chars.extend(numbers)
print(chars)    # ['a', 'b', 'c', 1, 2]
print(numbers)  # [1, 2] (без змін)

# insert(i, x) - вставляє елемент x на позицію з індексом i
chars = ["a", "c"]
chars.insert(1, "b")
print(chars)  # ['a', 'b', 'c']

# clear() - очищує список
chars = ['a', 'b']
chars.clear()
print(chars)  # []

# index() - знаходить індекс першого входження елемента
chars = ['a', 'b', 'c', 'd']
c_ind = chars.index('c')
print(c_ind)  # 2

# count() - підраховує кількість входжень елемента
my_list = [1, 2, 3, 4, 2, 2, 5, 2]
count_2 = my_list.count(2)
print(count_2)  # 4

# len() - кількість елементів у колекції
my_list = [1, 2, 3, 4, 5]
print(len(my_list))  # 5

# sort() - сортує список "на місці" (за зростанням за замовчуванням)
nums = [3, 1, 4, 1, 5, 9, 2]
nums.sort()
print(nums)  # [1, 1, 2, 3, 4, 5, 9]

# sort(reverse=True) - сортування за спаданням
nums.sort(reverse=True)
print(nums)  # [9, 5, 4, 3, 2, 1, 1]

# sort(key=...) - сортування за ключем (наприклад, за довжиною слова)
words = ["banana", "apple", "cherry"]
words.sort(key=len)
print(words)  # ['apple', 'banana', 'cherry']

# sorted() - повертає НОВИЙ відсортований список, не змінюючи оригінал
nums = [3, 1, 4, 1, 5, 9, 2]
sorted_nums = sorted(nums)
print(sorted_nums)  # [1, 1, 2, 3, 4, 5, 9]

sorted_nums_desc = sorted(nums, reverse=True)
print(sorted_nums_desc)  # [9, 5, 4, 3, 2, 1, 1]

words = ["banana", "apple", "cherry"]
sorted_words = sorted(words, key=len)
print(sorted_words)  # ['apple', 'banana', 'cherry']

# copy() - повертає копію списку
chars = ['a', 'b']
chars_copy = chars.copy()
print(chars_copy)  # ['a', 'b']

# reverse() - змінює порядок елементів списку на зворотний
chars = ["banana", "apple", "cherry"]
chars.reverse()
print(chars)  # ['cherry', 'apple', 'banana']
