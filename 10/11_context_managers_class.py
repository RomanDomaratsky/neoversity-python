# Тема: Власні менеджери контексту (клас з __enter__ та __exit__)
# ------------------------------------------------------------------------
# Об'єкт-менеджер контексту керує оператором with...as..., так само як
# ітератор керує for-in. __enter__ викликається на вході в блок with (його
# повернене значення потрапляє в "as X"). __exit__ викликається на виході
# з блоку, навіть якщо сталося виключення.
# __exit__(self, exc_type, exc_val, exc_tb) повертає:
#   False - виключення прокидається далі (не гаситься)
#   True  - виключення поглинається (не прокидається)

class MyContextManager:
    def __enter__(self):
        print("Enter the block")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Exit the block")
        if exc_type:
            print(f"Error detected: {exc_value}")
        return False  # виключення НЕ гаситься - прокинеться далі


if __name__ == "__main__":
    try:
        with MyContextManager() as my_resource:
            print("Inside the block")
            raise Exception("Something went wrong")
    except Exception as e:
        print(f"Caught outside: {e}")
    # Enter the block
    # Inside the block
    # Exit the block
    # Error detected: Something went wrong
    # Caught outside: Something went wrong


# --- Практичний приклад: FileManager - робота з файлами + логування ---
class FileManager:
    def __init__(self, filename, mode='w', encoding='utf-8'):
        self.file = None
        self.opened = False
        self.filename = filename
        self.mode = mode
        self.encoding = encoding

    def __enter__(self):
        self.file = open(self.filename, self.mode, encoding=self.encoding)
        self.opened = True
        print("Відкриваємо файл", self.filename)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Завершення блоку with")
        if self.opened:
            print("Закриваємо файл", self.filename)
            self.file.close()
        self.opened = False


if __name__ == '__main__':
    with FileManager('demo_new_file.txt') as f:
        f.write('Hello world!\n')
        f.write('The end\n')
    # Відкриваємо файл demo_new_file.txt
    # Завершення блоку with
    # Закриваємо файл demo_new_file.txt

    import os
    try:
        if os.path.exists('demo_new_file.txt'):
            os.remove('demo_new_file.txt')  # прибираємо за собою тестовий файл
    except OSError:
        pass

# Практичне застосування: власні контекстні менеджери використовують для
# гарантованого звільнення ресурсів - з'єднань з БД, мережевих сокетів,
# файлових дескрипторів, блокувань (locks) - незалежно від того, чи
# виникла помилка всередині блоку with.
