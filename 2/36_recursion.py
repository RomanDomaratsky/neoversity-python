# Тема: Рекурсія (факторіал, числа Фібоначчі, стек викликів)
# ------------------------------------------------------------------------

# Факторіал: n! = 1, якщо n == 0; інакше n * (n-1)!
def factorial(n):
    if n == 0:              # базовий випадок
        return 1
    else:
        return n * factorial(n - 1)  # рекурсивний випадок


print(factorial(5))  # 120


# Числа Фібоначчі: F(0)=0, F(1)=1, F(n) = F(n-1) + F(n-2)
def fibonacci(n):
    if n <= 1:              # базовий випадок
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)  # рекурсивний випадок


print(fibonacci(10))  # 55


# Демонстрація стеку викликів рекурсії (з print для наочності)
def factorial_verbose(n):
    print("Виклик функції factorial з n = ", n)
    if n == 1:
        print("Базовий випадок, n = 1, повернення 1")
        return 1
    else:
        result = n * factorial_verbose(n - 1)
        print("Повернення результату для n = ", n, ": ", result)
        return result


print(factorial_verbose(5))  # 120, з докладним логом виконання

# Примітка: максимальна глибина рекурсії у Python - зазвичай 1000 викликів.
# Без досягнення базового випадку рекурсія призведе до RecursionError
# (переповнення стеку викликів, stack overflow).
