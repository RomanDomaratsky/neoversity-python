# Тема: str.encode(), перетворення чисел у bytes, функція hex()
# ------------------------------------------------------------------------

# encode() - перетворення звичайного рядка в байтовий рядок
byte_str = 'some text'.encode()
print(byte_str)  # b'some text'

# Синтаксис: str.encode(encoding="utf-8", errors="strict")
# errors: 'strict' (виняток), 'ignore' (пропустити), 'replace' (замінити на '?')

# Перетворення списку чисел (0-255) у байтовий рядок
numbers = [0, 128, 255]
byte_numbers = bytes(numbers)
print(byte_numbers)  # b'\x00\x80\xff'

# hex() - перетворення цілого числа в шістнадцятковий рядок
for num in [127, 255, 156]:
    print(hex(num))
# 0x7f
# 0xff
# 0x9c
