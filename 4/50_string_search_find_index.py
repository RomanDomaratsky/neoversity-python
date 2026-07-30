# Тема: Пошук у рядку - find, index, rfind, rindex
# --------------------------------------------------------

# find - повертає індекс першого збігу, або -1, якщо не знайдено
s = "Hi there!"
start = 0
end = 7
print(s.find("er", start, end))  # 5
print(s.find("q"))               # -1

# index - як find, але викидає ValueError, якщо підрядок не знайдено
s = "Hi there!"
print(s.index("er"))  # 5
# s.index("q")  # розкоментуй, щоб побачити ValueError

# rfind - пошук справа (повертає індекс ОСТАННЬОГО збігу)
s = 'Some words'
print(s.find("o"))   # 1
print(s.rfind('o'))  # 6

# rindex - "правий" аналог index (викидає ValueError, якщо не знайдено)
s = 'Some words'
print(s.index("o"))   # 1
print(s.rindex('o'))  # 6

# Практичне застосування: find/rfind часто використовують для розбору
# шляхів до файлів - наприклад, rfind('.') знаходить позицію останньої
# крапки, щоб виділити розширення файлу, а rfind('/') - ім'я файлу без шляху.
path = "/home/user/report.final.pdf"
dot_index = path.rfind(".")
extension = path[dot_index + 1:]
print(extension)  # pdf
