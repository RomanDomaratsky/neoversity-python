# Тема: Кодування рядків - ASCII, UTF-8, CP1251, ord/chr
# ------------------------------------------------------------------------

# ord() - Unicode-код символу; chr() - символ за Unicode-кодом (зворотна операція)
print(ord('a'))    # 97
print(chr(97))     # 'a'

# Кодування одного тексту в різні формати
s = "Привіт!"

utf8 = s.encode()
print(f"UTF-8: {utf8}")

utf16 = s.encode("utf-16")
print(f"UTF-16: {utf16}")

cp1251 = s.encode("cp1251")
print(f"CP-1251: {cp1251}")

s_from_utf16 = utf16.decode("utf-16")
print(s_from_utf16 == s)  # True


# Декодування в НЕПРАВИЛЬНОМУ кодуванні дає непередбачуваний результат
print(b'Hello world!'.decode('utf-16'))


# Практичне застосування: файли, створені у Windows-програмах (Excel, Notepad
# зі старими налаштуваннями), нерідко зберігаються в CP-1251, тоді як сучасні
# системи й API очікують UTF-8. Явна вказівка кодування при відкритті файлу
# рятує від "кракозябр" і збоїв при обміні даними між системами.
with open('example_utf8.txt', 'w', encoding='utf-8') as file:
    file.write("Привіт світ!")

with open('example_utf8.txt', 'r', encoding='utf-8') as file:
    content = file.read()
    print(content)
