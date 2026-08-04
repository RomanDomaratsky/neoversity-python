# Тема: Стек (Stack) - LIFO (Last In, First Out)
# ------------------------------------------------------------------------
# Операції: push (додати), pop (вилучити), peek (подивитись верхній),
# is_empty (перевірка на порожнечу).
# Практичне застосування: стек природньо моделює стек викликів функцій,
# кнопку "Назад" у браузері, скасування дій (Undo) у редакторах тощо.


def create_stack():
    return []


def is_empty(stack):
    return len(stack) == 0


def push(stack, item):
    stack.append(item)


def pop(stack):
    if not is_empty(stack):
        return stack.pop()
    else:
        print("Стек порожній")


def peek(stack):
    if not is_empty(stack):
        return stack[-1]
    else:
        print("Стек порожній")


stack = create_stack()
push(stack, 'a')
push(stack, 'b')
push(stack, 'c')
print(stack)  # ['a', 'b', 'c']

print(peek(stack))  # 'c' - верхній елемент, стек не змінюється

print(pop(stack))   # 'c' - видаляємо верхній елемент
print(stack)        # ['a', 'b']

print(pop(stack))   # 'b'
print(pop(stack))   # 'a'

# Якщо стек уже порожній - обидві операції виводять повідомлення
print(pop(stack))   # Стек порожній -> None
print(peek(stack))  # Стек порожній -> None
