# Тема: Методи рядків
# -----------------------
# Рядок - незмінна впорядкована послідовність символів.

# Одинарні лапки дозволяють використати подвійні всередині рядка, і навпаки
game_string = 'My favorite "Game"'
print(game_string)  # My favorite "Game"

# Впорядкованість: доступ до символів рядка за індексом
s = "Hello world!"
print(s[0])   # H
print(s[-1])  # !

# Незмінність: змінити символ рядка не можна
s = "Hello world!"
# s[0] = "Q"  # розкоментуй, щоб побачити TypeError

# upper() - переводить рядок у верхній регістр
s = "Hello"
print(s.upper())  # HELLO

# lower() - переводить рядок у нижній регістр
s = "Some Text"
print(s.lower())  # some text

# startswith() - перевіряє, чи рядок починається з підрядка
s = "Bill Jons"
print(s.startswith("Bi"))  # True

# endswith() - перевіряє, чи рядок закінчується підрядком
s = "hello.jpg"
print(s.endswith("jpg"))  # True

# capitalize() - перший символ великий, решта - малі
s = "hello world".capitalize()
print(s)  # Hello world

# title() - перша літера кожного слова велика
s = "hello world".title()
print(s)  # Hello World

# isdigit(), isalpha(), isspace() - перевірки вмісту рядка
print("123".isdigit())   # True
print("hello".isalpha())  # True
print(" ".isspace())      # True
