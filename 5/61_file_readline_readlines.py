# Тема: Порядкове читання файлів - readline() та readlines()
# ------------------------------------------------------------------------

# readline() - читає один рядок за раз (зберігає символ \n)
fh = open('test.txt', 'w')
fh.write('first line\nsecond line\nthird line')
fh.close()

fh = open('test.txt', 'r')
while True:
    line = fh.readline()
    if not line:
        break
    print(line)
fh.close()

# readlines() - читає весь файл одразу і повертає список рядків
fh = open('test.txt', 'w')
fh.write('first line\nsecond line\nthird line')
fh.close()

fh = open('test.txt', 'r')
lines = fh.readlines()
print(lines)  # ['first line\n', 'second line\n', 'third line']
fh.close()

# Видалення символу переносу рядка \n за допомогою strip()
fh = open("test.txt", "w")
fh.write("first line\nsecond line\nthird line")
fh.close()

fh = open("test.txt", "r")
lines = [el.strip() for el in fh.readlines()]
print(lines)  # ['first line', 'second line', 'third line']
fh.close()
