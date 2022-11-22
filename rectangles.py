from points import Point
import unittest


class Rectangle:
    """Klasa reprezentująca prostokąt na płaszczyźnie."""

    def __init__(self, x1, y1, x2, y2):
        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)

    def __str__(self):  # "[(x1, y1), (x2, y2)]"
        # return("[" + str(self.pt1.__str__()) + ", " + str(self.pt2.__str__()) + "]")
        return "[({},{}), ({},{})]".format(self.pt1.__str__(), self.pt2.__str__())

    def __repr__(self):  # "Rectangle(x1, y1, x2, y2)"
        return "Rectangle" + self.__str__()

    def __eq__(self, other):  # obsługa rect1 == rect2
        return self.pt1 == other.pt1 and self.pt2 == other.pt2

    def __ne__(self, other):  # obsługa rect1 != rect2
        return not self == other

    def center(self):  # zwraca środek prostokąta
        x = (self.pt1.x + self.pt2.x) / 2
        y = (self.pt1.y + self.pt2.y) / 2

        return Point(x, y)

    def area(self):  # pole powierzchni
        a = self.pt1.x - self.pt2.x
        b = self.pt1.y - self.pt2.y

        return abs(a * b)

    def move(self, x, y):  # przesunięcie o (x, y)
        self.pt1.x = self.pt1.x + x
        self.pt1.y = self.pt1.y + y
        self.pt2.x = self.pt2.x + x
        self.pt2.y = self.pt2.y + y


# Kod testujący moduł.


p1 = Point(1, 2)
p2 = Point(3, 4)
p4 = Point(5, 5)

r1 = Rectangle(p1.x, p1.y, p2.x, p2.y)
r2 = Rectangle(p1.x, p1.y, p2.x, p2.y)
r3 = Rectangle(p2.x, p2.y, p4.x, p4.y)


class TestRectangle(unittest.TestCase):

    def test__str__(self):
        self.assertEqual(r1 == Rectangle(2, 2, 2, 6), False)
        self.assertEqual(r2 == Rectangle(1, 2, 3, 4), True)
        self.assertEqual(r3 == Rectangle(2, 2, 2, 2), False)

    def test__eq__(self):
        self.assertEqual(r1 == r2, True)
        self.assertEqual(r1 == r3, False)
        self.assertEqual(r2 == r3, False)

    def test__ne__(self):
        self.assertEqual(r1 != r3, True)
        self.assertEqual(r2 != r3, True)

    def test__center__(self):
        self.assertEqual(r2.center() == Point(2, 3), True)
        self.assertEqual(r2.center() == Point(1, 1), False)
        self.assertEqual(r3.center() == Point(2, 2), False)

    def test__area__(self):
        self.assertEqual((r1.area() == 1), False)
        self.assertEqual((r2.area() == 3), False)

    def test__move__(self):
        r1.move(1, 2)
        self.assertEqual(r1 == Rectangle(2, 4, 4, 6), True)
        self.assertEqual(r1 == Rectangle(1, 2, 3, 4), False)
        r3.move(2, 2)
        self.assertEqual(r2 == Rectangle(1, 1, 1, 3), False)


if __name__ == '__main__':
    unittest.main()
