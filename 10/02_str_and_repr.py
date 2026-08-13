# Тема: Магічні методи __str__ та __repr__
# ------------------------------------------------------------------------
# __repr__ - "офіційне" представлення об'єкта, ідеально таке, щоб його
# можна було виконати як код Python для відтворення об'єкта. Викликається
# repr(obj) та інтерактивною консоллю.
# __str__ - "неофіційне", зручне для читання людиною представлення.
# Викликається str(obj) та print(obj). Якщо __str__ не визначений, Python
# використає __repr__ як запасний варіант.

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point(x={self.x}, y={self.y})"


point = Point(2, 3)
print(repr(point))  # Point(x=2, y=3)


# --- Використання __repr__ для відтворення об'єкта через eval() ---
original_point = Point(2, 3)
print(repr(original_point))  # Point(x=2, y=3)

# УВАГА: eval() виконує рядок як код - небезпечно для даних з ненадійних
# джерел. Тут використовується лише для демонстрації механізму __repr__.
new_point = eval(repr(original_point))
print(new_point)  # Point(x=2, y=3) - тому що немає __str__, Python бере __repr__


# --- __str__ для зрозумілого людині представлення ---
class Human:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Human named {self.name} who is {self.age} years old"

    def __repr__(self):
        return f"Human({self.name}, {self.age})"


human = Human("Alice", 30)
print(human)         # Human named Alice who is 30 years old (викликає __str__)
print(repr(human))   # Human(Alice, 30) (викликає __repr__)

# Практичне застосування: __repr__ незамінний під час налагодження в
# консолі/логах (щоб точно бачити стан об'єкта, наприклад User(id=5,
# email='a@b.com')), а __str__ використовують для показу об'єкта кінцевому
# користувачу (наприклад, у чеку, звіті чи повідомленні).
