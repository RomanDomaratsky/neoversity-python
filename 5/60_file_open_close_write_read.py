# Тема: Відкриття/закриття файлів, базовий запис і читання (open, write, read)
# ------------------------------------------------------------------------------
# open(file, mode='r', ...): 'r' читання, 'w' запис (перезапис), 'a' додавання,
# 'b' бінарний режим, '+' читання і запис одночасно.

# Відкриття файлу (за замовчуванням - тільки читання, файл має існувати)
fh = open('test_file_demo.txt', 'w')  # створимо файл, щоб приклад нижче спрацював
fh.write("placeholder")
fh.close()

fh = open('test_file_demo.txt')
fh.close()

# Запис у файл (режим 'w' створює новий файл або перезаписує існуючий)
fh = open('test.txt', 'w')
symbols_written = fh.write('hello!')
print(symbols_written)  # 6
fh.close()

# Читання певної кількості символів (режим 'w+' - і запис, і читання)
fh = open('test.txt', 'w+')
fh.write('hello!')
fh.seek(0)  # повертаємо курсор на початок файлу

first_two_symbols = fh.read(2)
print(first_two_symbols)  # 'he'
fh.close()

# Читання всього вмісту файлу за раз
fh = open('test.txt', 'w')
fh.write('hello!')
fh.close()

fh = open('test.txt', 'r')
all_file = fh.read()
print(all_file)  # 'hello!'
fh.close()

# Читання файлу по одному символу, поки файл не закінчиться
fh = open('test.txt', 'w')
fh.write('hello!')
fh.close()

fh = open('test.txt', 'r')
while True:
    symbol = fh.read(1)
    if len(symbol) == 0:
        break
    print(symbol)
fh.close()
