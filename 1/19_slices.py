# Тема: Зрізи у Python (Slice)
# --------------------------------
# Синтаксис: послідовність[початок:кінець:крок]
# початок - включно, кінець - НЕ включно, крок - за замовчуванням 1.

# Перші 5 символів рядка
s = "Hello, World!"
first_five = s[:5]
print(first_five)  # Hello

# Список чисел від 1 до 10
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Непарні числа (індекси 0, 2, 4, ... з кроком 2)
odd_numbers = numbers[0:10:2]
print(odd_numbers)  # [1, 3, 5, 7, 9]

# Скорочений запис (за замовчуванням від початку до кінця)
odd_numbers = numbers[::2]
print(odd_numbers)  # [1, 3, 5, 7, 9]

# Парні числа (починаючи з індексу 1)
even_numbers = numbers[1:10:2]
print(even_numbers)  # [2, 4, 6, 8, 10]

# Скорочений запис
even_numbers = numbers[1::2]
print(even_numbers)  # [2, 4, 6, 8, 10]

# Числа, кратні трьом (починаючи з індексу 2, крок 3)
three_numbers = numbers[2:10:3]
print(three_numbers)  # [3, 6, 9]

# Скорочений запис
three_numbers = numbers[2::3]
print(three_numbers)  # [3, 6, 9]

# Зворотний порядок за допомогою від'ємного кроку
reverse_numbers = numbers[::-1]
print(reverse_numbers)  # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

# Копія списку за допомогою зрізу [:]
copy_numbers = numbers[:]
print(copy_numbers)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] - незалежна копія
