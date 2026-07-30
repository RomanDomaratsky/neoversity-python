# Тема: Керування курсором у файлі - seek() та tell()
# ------------------------------------------------------------

# seek(offset) - переміщує курсор на вказану позицію (за замовчуванням від початку)
fh = open('test.txt', 'w+')
fh.write('hello!')

fh.seek(1)
second = fh.read(1)
print(second)  # 'e'
fh.close()

# tell() - повертає поточну позицію курсора (номер символу від початку файлу)
fh = open("test.txt", "w+")
fh.write("hello!")

position = fh.tell()
print(position)  # 6 (курсор в кінці після запису)

fh.seek(1)
position = fh.tell()
print(position)  # 1

fh.read(2)
position = fh.tell()
print(position)  # 3 (прочитали 2 символи від позиції 1)

fh.close()
