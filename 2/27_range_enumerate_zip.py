# Тема: Функції range, enumerate, zip у циклі for
# ------------------------------------------------------

# range(stop) - числа від 0 до stop-1
for i in range(5):
    print(i)
# 0 1 2 3 4

# range(start, stop) - числа від start до stop-1
for i in range(2, 10):
    print(i)
# 2 3 4 5 6 7 8 9

# range(start, stop, step) - з кроком
for i in range(0, 10, 2):
    print(i)
# 0 2 4 6 8


# enumerate - отримання індексу та значення одночасно
some_list = ["apple", "banana", "cherry"]
for index, value in enumerate(some_list):
    print(index, value)
# 0 apple
# 1 banana
# 2 cherry


# zip - одночасна ітерація по кількох колекціях
list1 = ["зелене", "стигла", "червоний"]
list2 = ["яблуко", "вишня", "томат"]
for number, letter in zip(list1, list2):
    print(number, letter)
# зелене яблуко
# стигла вишня
# червоний томат

# zip зупиняється на найкоротшій колекції
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c', 'd', 'e']
for number, letter in zip(list1, list2):
    print(number, letter)
# 1 a
# 2 b
# 3 c
# ('d' та 'e' з list2 ігноруються)
