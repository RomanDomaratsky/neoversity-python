# Тема: Спеціальні (керувальні/escape) символи в рядках
# --------------------------------------------------------------
# \n - перенесення рядка   \t - табуляція   \r - повернення каретки
# \f - перенесення сторінки   \v - вертикальна табуляція   \b - забій

print("Hello\nWorld")
# Hello
# World

print("Hello\tWorld")
# Hello   World

print("Hello my little\rsister")
# sistermy little  (\r повертає курсор на початок рядка)

print("Hello\bWorld")
# HellWorld (\b видаляє попередній символ)

# Виведення самого символу зворотної скісної риски
print("Hello\\World")
# Hello\World

# Екранування лапок, щоб використати їх усередині рядка
print('It\'s a beautiful day')
print('He said, "Hello"')
# It's a beautiful day
# He said, "Hello"
