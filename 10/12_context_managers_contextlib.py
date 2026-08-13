# Тема: Створення менеджерів контексту через @contextmanager (contextlib)
# ------------------------------------------------------------------------
# contextlib.contextmanager дозволяє створити менеджер контексту з
# генераторної функції замість повноцінного класу з __enter__/__exit__.
# Код ДО yield виконується як __enter__, значення yield потрапляє в "as X",
# код у finally ПІСЛЯ yield виконується як __exit__ (гарантовано, навіть
# якщо в блоці with виникло виключення).

from contextlib import contextmanager


@contextmanager
def my_context_manager():
    print("Enter the block")
    try:
        yield  # Місце виконання блоку `with`
    except Exception as e:
        print(f"Error detected: {e}")
        raise
    finally:
        print("Exit the block")


if __name__ == "__main__":
    try:
        with my_context_manager():
            print("Inside the block")
            raise Exception("Something went wrong")
    except Exception as e:
        print(f"Caught outside: {e}")
    # Enter the block
    # Inside the block
    # Error detected: Something went wrong
    # Exit the block
    # Caught outside: Something went wrong


# --- Практичний приклад: file_manager - функціональний аналог класу FileManager ---
@contextmanager
def file_manager(filename, mode='w', encoding='utf-8'):
    print("Відкриваємо файл", filename)
    file = open(filename, mode, encoding=encoding)
    try:
        yield file
    finally:
        print("Закриваємо файл", filename)
        file.close()
        print("Завершення блоку with")


if __name__ == '__main__':
    with file_manager('demo_new_file2.txt') as f:
        f.write('Hello world!\n')
        f.write('The end\n')
    # Відкриваємо файл demo_new_file2.txt
    # Закриваємо файл demo_new_file2.txt
    # Завершення блоку with

    import os
    try:
        if os.path.exists('demo_new_file2.txt'):
            os.remove('demo_new_file2.txt')
    except OSError:
        pass


# --- Розширений приклад: логування часу відкриття/закриття файлу ---
from datetime import datetime


@contextmanager
def managed_resource(*args, **kwargs):
    log = ''
    timestamp = datetime.now().timestamp()
    msg = f'{timestamp:<20}|{args[0]:^15}| open \n'
    log += msg
    file_handler = open(*args, **kwargs)
    try:
        yield file_handler
    finally:
        diff = datetime.now().timestamp() - timestamp
        msg = f'{timestamp:<20}|{args[0]:^15}| closed {round(diff, 6):>15}s \n'
        log += msg
        file_handler.close()
        print(log)


if __name__ == '__main__':
    # Спочатку створюємо тестовий файл, який будемо читати нижче
    with open('demo_source.txt', 'w', encoding='utf-8') as f:
        f.write('Hello world!\nThe end\n')

    with managed_resource('demo_source.txt', 'r') as f:
        print(f.read())
    # Hello world!
    # The end
    #
    # <timestamp>          | demo_source.txt | open
    # <timestamp>          | demo_source.txt | closed        0.0000xxs

    try:
        os.remove('demo_source.txt')
    except OSError:
        pass

# Практичне застосування: @contextmanager - лаконічний спосіб створювати
# менеджери для одноразових/простих задач: тимчасова зміна робочої
# директорії, вимірювання часу виконання блоку коду, тимчасове відключення
# логування, транзакція БД (commit при успіху, rollback при виключенні).
