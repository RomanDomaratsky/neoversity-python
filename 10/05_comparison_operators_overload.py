# Тема: Перевизначення операторів порівняння
# ------------------------------------------------------------------------
# __eq__ -> ==   __ne__ -> !=   __lt__ -> <   __gt__ -> >
# __le__ -> <=   __ge__ -> >=
# Повернення NotImplemented сигналізує Python спробувати інший спосіб
# порівняння (наприклад, метод іншого об'єкта); якщо жоден не підходить -
# виникає TypeError.

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def __eq__(self, other):
        if not isinstance(other, Rectangle):
            return NotImplemented
        return self.area() == other.area()

    def __ne__(self, other):
        return not self.__eq__(other)

    def __lt__(self, other):
        if not isinstance(other, Rectangle):
            return NotImplemented
        return self.area() < other.area()

    def __le__(self, other):
        return self.__lt__(other) or self.__eq__(other)

    def __gt__(self, other):
        if not isinstance(other, Rectangle):
            return NotImplemented
        return self.area() > other.area()

    def __ge__(self, other):
        return self.__gt__(other) or self.__eq__(other)


if __name__ == "__main__":
    rect1 = Rectangle(5, 10)
    rect2 = Rectangle(3, 20)
    rect3 = Rectangle(5, 10)
    print(f"Площа прямокутників: {rect1.area()}, {rect2.area()}, {rect3.area()}")
    # Площа прямокутників: 50, 60, 50
    print(rect1 == rect3)  # True
    print(rect1 != rect2)  # True
    print(rect1 < rect2)   # True
    print(rect1 <= rect3)  # True
    print(rect1 > rect2)   # False
    print(rect1 >= rect3)  # True

    # rect1 > 10 викличе TypeError, бо int не має площі для порівняння
    try:
        print(rect1 > 10)
    except TypeError as e:
        print(f"TypeError: {e}")


# --- Практичний приклад: точки у 2D просторі ---
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        if not isinstance(other, Point):
            return NotImplemented
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        return not self.__eq__(other)

    def __lt__(self, other):
        if not isinstance(other, Point):
            return NotImplemented
        return self.x < other.x and self.y < other.y

    def __gt__(self, other):
        if not isinstance(other, Point):
            return NotImplemented
        return self.x > other.x and self.y > other.y

    def __le__(self, other):
        if not isinstance(other, Point):
            return NotImplemented
        return self.x <= other.x and self.y <= other.y

    def __ge__(self, other):
        if not isinstance(other, Point):
            return NotImplemented
        return self.x >= other.x and self.y >= other.y


if __name__ == "__main__":
    print(Point(0, 0) == Point(0, 0))   # True
    print(Point(0, 0) != Point(0, 0))   # False
    print(Point(0, 0) < Point(1, 0))    # False
    print(Point(0, 0) > Point(0, 1))    # False
    print(Point(0, 2) >= Point(0, 1))   # True
    print(Point(0, 0) <= Point(0, 0))   # True

# Практичне застосування: перевизначені оператори порівняння дозволяють
# сортувати (sorted()), знаходити мінімум/максимум (min()/max()) та
# упорядковувати власні об'єкти (замовлення за сумою, версії ПЗ за
# семантичним номером тощо) звичними Python-засобами.
