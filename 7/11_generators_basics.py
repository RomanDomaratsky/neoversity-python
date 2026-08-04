# Тема: Основи генераторів (yield, next())
# ------------------------------------------------------------------------
# yield "заморожує" виконання функції та повертає значення. При наступному
# викликові next() виконання продовжується З ТОГО САМОГО МІСЦЯ, а не з початку.


def my_generator():
    yield 1
    yield 2
    yield 3


gen = my_generator()

print(next(gen))  # 1
print(next(gen))  # 2
print(next(gen))  # 3

# Якщо викликати next(gen) ще раз - значень більше немає, і Python
# викине виняток StopIteration (сигнал завершення ітерації).
try:
    print(next(gen))
except StopIteration:
    print("Генератор виснажено - StopIteration")
