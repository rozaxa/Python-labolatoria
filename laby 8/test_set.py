import pytest
from rec import Rectangle
from points import Point

def tests_1():
    r = Rectangle.from_points((Point(1,1), Point(3,4)))
    r2 = Rectangle(1,2,3,4)
    assert ((r == r2), True)

    r = Rectangle.from_points((Point(2,2), Point(4,5)))
    r2 = Rectangle(2,2,4,5)
    assert ((r == r2), True)

def tests_2():
    r = Rectangle(1,2,3,4)
    assert r.top == 4
    assert r.left == 2
    assert r.bottom == 1
    assert r.right == 3
    assert r. width == 2
    assert r.height == 2

    r = Rectangle(3, 4, 5, 6)
    assert r.top == 6
    assert r.left == 4
    assert r.bottom == 3
    assert r.right == 5
    assert r. width == 2
    assert r.height == 2

def test_3():
    p1 = Point(1,2)
    p2 = Point(3,4)
    r = Rectangle.from_points((p1,p2))

    assert r.topright == p2
    assert r.topleft == Point(p1.x, p2.y)
    assert r.bottomright == Point(p2.x, p1.y)
    assert r.bottomleft == p1

