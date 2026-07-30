# Тема: Модуль логування з кольоровим виводом (на основі colorama)
# ------------------------------------------------------------------------------
# Практичне застосування: у реальних консольних застосунках/скриптах кольорове
# розділення INFO/WARNING/ERROR суттєво прискорює читання логів під час
# налагодження - помилки одразу "кидаються в очі" червоним кольором.

from colorama import Fore


def log_info(message):
    print(f"{Fore.BLUE} [INFO] {Fore.RESET} {message}")


def log_warning(message):
    print(f"{Fore.YELLOW} [WARNING] {Fore.RESET} {message}")


def log_error(message):
    print(f"{Fore.RED} [ERROR] {Fore.RESET} {message}")
