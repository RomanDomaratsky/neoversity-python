# Тема: Counter з модуля collections - підрахунок елементів
# ------------------------------------------------------------------------

# Підрахунок "вручну" через звичайний словник
student_marks = [4, 2, 4, 6, 7, 4, 2, 3, 4, 5, 6, 6, 7, 1, 1, 1, 3, 5]
mark_counts = {}
for mark in student_marks:
    if mark in mark_counts:
        mark_counts[mark] += 1
    else:
        mark_counts[mark] = 1
print(mark_counts)  # {4: 4, 2: 2, 6: 3, 7: 2, 3: 2, 5: 2, 1: 3}


# Той самий результат за допомогою Counter - один рядок замість шести
import collections

mark_counts = collections.Counter(student_marks)
print(mark_counts)  # Counter({4: 4, 6: 3, 1: 3, 2: 2, 7: 2, 3: 2, 5: 2})


# most_common() - список елементів за частотою, від найчастіших
print(mark_counts.most_common())    # [(4, 4), (6, 3), (1, 3), (2, 2), (7, 2), (3, 2), (5, 2)]
print(mark_counts.most_common(1))   # [(4, 4)]
print(mark_counts.most_common(2))   # [(4, 4), (6, 3)]


# Counter напряму з рядка - підрахунок символів
from collections import Counter

letter_count = Counter("banana")
print(letter_count)  # Counter({'a': 3, 'n': 2, 'b': 1})


# Практичне застосування: підрахунок частоти слів у тексті - типова
# задача базового аналізу тексту (найпопулярніші теги, ключові слова тощо).
sentence = "the quick brown fox jumps over the lazy dog"
words = sentence.split()
word_count = Counter(words)

for word, count in word_count.items():
    print(f"{word}: {count}")
