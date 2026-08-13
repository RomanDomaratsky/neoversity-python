# Тема: Передача значень у генератор (send), закриття генератора (close)
# ------------------------------------------------------------------------
# yield може повертати значення так само, як виклик функції - це дозволяє
# передавати значення В генератор через метод send(). close() завершує
# роботу генератора, викликаючи всередині нього GeneratorExit.

def my_generator():
    received = yield "Ready"
    yield f"Received: {received}"


gen = my_generator()
print(next(gen))          # Ready
print(gen.send("Hello"))  # Received: Hello


# --- close() і перехоплення GeneratorExit ---
def my_generator_closable():
    try:
        yield "Working"
    except GeneratorExit:
        print("Generator is being closed")


gen2 = my_generator_closable()
print(next(gen2))  # Working
gen2.close()        # Generator is being closed


# --- Практичний приклад 1: генератор, що приймає числа та повертає квадрати ---
def square_numbers():
    try:
        while True:
            number = yield          # Отримання числа через send()
            square = number ** 2
            yield square             # Повернення результату
    except GeneratorExit:
        print("Generator closed")


gen3 = square_numbers()
next(gen3)  # Ініціалізація генератора (аналог gen.send(None))

result = gen3.send(10)
print(f"Square of 10: {result}")  # Square of 10: 100

next(gen3)  # Перехід до наступного очікування

result = gen3.send(5)
print(f"Square of 5: {result}")  # Square of 5: 25

gen3.close()  # Generator closed


# --- Практичний приклад 2: фільтрація рядків за ключовим словом ---
def filter_lines(keyword):
    print(f"Looking for {keyword}")
    try:
        while True:
            line = yield  # Отримання рядка через send()
            if keyword in line:
                yield f"Line accepted: {line}"
            else:
                yield None
    except GeneratorExit:
        print("Generator closed")


if __name__ == "__main__":
    gen4 = filter_lines("hello")
    next(gen4)  # Потрібно для старту генератора
    messages = ["this is a test", "hello world", "another hello world line", "hello again", "goodbye"]
    hello_messages = []
    for message in messages:
        result = gen4.send(message)
        if result:
            hello_messages.append(result)
        next(gen4)  # Продовжуємо до наступного yield

    gen4.close()
    print(hello_messages)
    # Looking for hello
    # Generator closed
    # ['Line accepted: hello world', 'Line accepted: another hello world line', 'Line accepted: hello again']

# Практичне застосування: send()-генератори використовують у "кооперативній
# багатозадачності" та обробці потоків даних - наприклад, конвеєр обробки
# рядків логів у реальному часі, де кожен новий рядок надсилається в
# генератор і одразу фільтрується/трансформується без зберігання всього
# потоку в пам'яті.
