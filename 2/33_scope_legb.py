# Тема: Області видимості - правило LEGB (Local, Enclosing, Global, Built-in)
# ------------------------------------------------------------------------------

# --- Local ---
x = 50


def func():
    x = 2
    print('Зміна локального x на', x)  # Зміна локального x на 2


func()
print('Глобальний x, як і раніше', x)  # Глобальний x, як і раніше 50


# --- Enclosing ---
def outer_func():
    enclosing_var = "Я змінна у функції, що охоплює"

    def inner_func():
        print("Всередині вкладеної функції:", enclosing_var)

    inner_func()


outer_func()
# Всередині вкладеної функції: Я змінна у функції, що охоплює


# Зміна змінної з охоплюваної області видимості через nonlocal
def func_outer():
    x = 2

    def func_inner():
        nonlocal x
        x = 5

    func_inner()
    return x


result = func_outer()
print(result)  # 5


# --- Global ---
x = 50


def func_global():
    global x
    print('x дорівнює', x)  # x дорівнює 50
    x = 2
    print('Змінюємо глобальне значення x на', x)  # Змінюємо глобальне значення x на 2


func_global()
print('Значення x складає', x)  # Значення x складає 2
