# Тема: Метод translate() та str.maketrans()
# --------------------------------------------------

# Створення таблиці перекладу: заміна голосних на цифри
intab = "aeiou"
outtab = "12345"
trantab = str.maketrans(intab, outtab)
text = "This is string example"
print(text.translate(trantab))  # Th3s 3s str3ng 2x1mpl2

# Видалення символів: третій аргумент maketrans() - символи для видалення
intab = "aeiou"
trantab = str.maketrans('', '', intab)
text = "This is string example"
print(text.translate(trantab))  # Ths s strng xmpl


# --- Задача: конвертація шістнадцяткових символів у двійковий код ---
# Практичне застосування: такий підхід (побудова таблиці перекладу через
# ord() + translate) використовують для швидкого масового кодування/
# декодування символів - наприклад, у власних текстових кодуваннях,
# симуляторах низькорівневих обчислень або навчальних завданнях з логіки.
symbols = "0123456789ABCDEF"
code = [
        '0000', '0001', '0010', '0011', '0100', '0101', '0110', '0111',
        '1000', '1001', '1010', '1011', '1100', '1101', '1110', '1111'
        ]
MAP = {}
for s, c in zip(symbols, code):
    MAP[ord(s)] = c
    MAP[ord(s.lower())] = c

result = "34 DF 56 AC".translate(MAP)
print(result)  # 00110100 11011111 01010110 10101100


# --- Задача: конвертація тексту в код Морзе ---
morze_dict = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
              'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
              'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
              'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
              'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---',
              '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...',
              '8': '---..', '9': '----.'}

# Перетворення ключів словника на Unicode коди (для translate)
table_morze_dict = {}
for k, v in morze_dict.items():
    table_morze_dict[ord(k)] = v

string = "Hello world"
result = ""
for ch in string:
    result = result + ch.upper().translate(table_morze_dict)

print(result)
