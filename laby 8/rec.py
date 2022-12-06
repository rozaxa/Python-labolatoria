from points import Point


class Rectangle:
    """Klasa reprezentująca prostokąty na płaszczyźnie."""

    def __init__(self, x1, y1, x2, y2):
        # Chcemy, aby x1 < x2, y1 < y2.

        if x1 >= x2 or y1 >= y2:
            raise ValueError("Try again, invalid value!")
        else:
            self.pt1 = Point(x1, y1)
            self.pt2 = Point(x2, y2)

    def __str__(self):  # "[(x1, y1), (x2, y2)]"
        return "[({},{}), ({},{})]".format(self.pt1.__str__(), self.pt2.__str__())

    def __repr__(self):  # "Rectangle(x1, y1, x2, y2)"
        return "Rectangle" + self.__str__()

    def __eq__(self, other):  # obsługa rect1 == rect2
        if isinstance(other, Rectangle):
            return self.pt1 == other.pt1 and self.pt2 == other.pt2
        else:
            raise ValueError("Try again, invalid value of other!")

    def __ne__(self, other):  # obsługa rect1 != rect2
        if isinstance(other, Rectangle):
            return not self == other
        else:
            raise ValueError("Try again, invalid value of other!")

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

    def intersection(self, other):
        if isinstance(other, Rectangle):
            new_x1 = max(self.pt1.x, other.pt1.x)
            new_x2 = min(self.pt2.x, other.pt2.x)
            new_y1 = max(self.pt1.y, other.pt1.y)
            new_y2 = min(self.pt2.y, other.pt2.y)
            return Rectangle(new_x1, new_y1, new_x2, new_y2)
        else:
            raise ValueError("Try again, invalid value of other!")

    def cover(self, other):  # prostąkąt nakrywający oba
        if isinstance(other, Rectangle):
            new_x1 = min(self.pt1.x, other.pt1.x)
            new_x2 = max(self.pt2.x, other.pt2.x)
            new_y1 = min(self.pt1.y, other.pt1.y)
            new_y2 = max(self.pt2.y, other.pt2.y)
            return Rectangle(new_x1, new_y1, new_x2, new_y2)
        else:
            raise ValueError("Try again, invalid value of other!")

    def make4(self):  # zwraca krotkę czterech mniejszych
        xM = self.pt1.x + ((self.pt2.x - self.pt1.x) / 2)
        yM = self.pt1.y + ((self.pt2.y - self.pt1.y) / 2)

        r1 = Rectangle(self.pt1.x, self.pt1.y, xM, yM)
        r2 = Rectangle(xM, self.pt1.y, self.pt2.x, yM)
        r3 = Rectangle(self.pt1.x, yM, xM, self.pt2.y)
        r4 = Rectangle(xM, yM, self.pt2.x, self.pt2.y)

        return (r1, r2, r3, r4)

    @classmethod
    def from_points(cls, points):
        point1, point2 = points

        if isinstance(point1, Point) and isinstance(point2, Point):
            x1 = point1.x
            y1 = point1.y
            x2 = point2.x
            y2 = point2.y
            return cls(x1, y1, x2, y2)
        else:
            raise ValueError("Try again, invalid value!")

    @property
    def top(self):
        return self.pt2.y

    @property
    def left(self):
        return self.pt1.y


    @property
    def bottom(self):
        return self.pt1.x

    @property
    def right(self):
        return self.pt2.x

    @property
    def width(self):
        return (self.pt2.x - self.pt1.x)

    @property
    def height(self):
        return (self.pt2.y - self.pt1.y)

    @property
    def topleft(self):
        return Point(self.pt1.x, self.pt2.y)

    @property
    def bottomleft(self):
        return Point(self.pt1.x, self.pt1.y)

    @property
    def topright(self):
        return Point(self.pt2.x, self.pt2.y)

    @property
    def bottomright(self):
        return Point(self.pt2.x, self.pt1.y)