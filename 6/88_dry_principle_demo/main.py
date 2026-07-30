# Тема: Використання спільної функції з math_operations.py у декількох місцях
# ------------------------------------------------------------------------------
# ПОРІВНЯЙТЕ з порушенням DRY (закомментовано нижче) - без винесення в
# функцію формулу length * width довелося б дублювати щоразу:
#
#   length1, width1 = 5, 10
#   area1 = length1 * width1
#   ...
#   length2, width2 = 7, 12
#   area2 = length2 * width2
#
# Проблема: якщо формула зміниться, треба виправляти КОЖНЕ місце дублювання.

from math_operations import calculate_area

area1 = calculate_area(5, 10)
area2 = calculate_area(7, 12)

print(area1)  # 50
print(area2)  # 84
