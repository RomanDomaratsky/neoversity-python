# Тема: Масив байтів bytearray (змінна версія bytes)
# ------------------------------------------------------------

# bytearray - ЗМІННИЙ тип; елементи - цілі числа 0-255, а не символи
byte_array = bytearray(b'Kill Bill')
byte_array[0] = 'B'
byte_array[5] = ord('K')
print(byte_array)  # bytearray(b'Bill Kill')

# append() - додавання елемента (bytearray можна змінювати "на місці")
byte_array = bytearray(b"Hello")
byte_array.append(ord("!"))
print(byte_array)  # bytearray(b'Hello!')

# decode() - перетворення bytearray назад у звичайний рядок
byte_array = bytearray(b"Hello World")
string = byte_array.decode("utf-8")
print(string)  # Hello World

# bytearray корисний при обробці бінарних даних: читання файлів у
# бінарному режимі, обробка мережевих пакетів, робота з образами в пам'яті.
