import math

def tearDown(frac):  # funkcja do skracania ulamkow
    if frac[0] == 0 and frac[1] != 0:
        frac[1] = 1
    return [frac[0] / math.gcd(frac[0], frac[1]), frac[1] / math.gcd(frac[0], frac[1])]


def add_frac(frac1, frac2): # frac1 + frac2
    return tearDown([(frac1[0] * frac2[1] + frac2[0] * frac1[1]), frac1[1] * frac2[1]])


def sub_frac(frac1, frac2): # frac1 - frac2
    return tearDown([(frac1[0] * frac2[1] - frac2[0] * frac1[1]), frac1[1] * frac2[1]])


def mul_frac(frac1, frac2): # frac1 * frac2
    return tearDown([frac1[0] * frac2[0], frac1[1] * frac2[1]])


def div_frac(frac1, frac2):  # frac1 / frac2
    return tearDown([frac1[0] * frac2[1], frac1[1] * frac2[0]])


def is_positive(frac): # bool, czy dodatni
    if frac[0] / frac[1] > 0:
        return True
    else:
        return False


def is_zero(frac):  # bool, typu [0, x]
    if frac[0] == 0:
        return True
    else:
        return False


def cmp_frac(frac1, frac2):  # -1 | 0 | +1

    f1 = frac1[0]/frac1[1]
    f2 = frac2[0]/frac2[1]

    if f1 > f2:
        return 1
    elif f1 < f2:
        return -1
    else:
        return 0


def frac2float(frac): # konwersja do float

    x = frac[0] / frac[1]
    return x


# f1 = [-1, 2]      # -1/2
# f2 = [1, -2]      # -1/2 (niejednoznaczność)
# f3 = [0, 1]       # zero
# f4 = [0, 2]       # zero (niejednoznaczność)
# f5 = [3, 1]       # 3
# f6 = [6, 2]       # 3 (niejednoznaczność)



import unittest


class TestFractions(unittest.TestCase):

    def setUp(self):
        self.zero = [0, 1]

    def test_add_frac(self):
        self.assertEqual(add_frac([1, 2], [1, 3]), [5, 6])
        self.assertEqual(add_frac([2, 5], [1, 4]), [13, 20])

    def test_sub_frac(self):
        self.assertEqual(sub_frac([1, 2], [1, 3]), [1, 6])
        self.assertEqual(sub_frac([2, 5], [1, 4]), [3, 20])


    def test_mul_frac(self):
        self.assertEqual(mul_frac([1, 2], [1, 3]), [1, 6])
        self.assertEqual(mul_frac([2, 5], [1, 4]), [1, 10])


    def test_div_frac(self):
        self.assertEqual(div_frac([1, 2], [1, 3]), [3, 2])
        self.assertEqual(div_frac([2, 5], [1, 4]), [8, 5])


    def test_is_positive(self):
        self.assertEqual(is_positive([1, 3]), True)
        self.assertEqual(is_positive([1, -3]), False)


    def test_is_zero(self):
        self.assertEqual(is_zero([0, 3]), True)
        self.assertEqual(is_zero([3, 0]), False)

    def test_cmp_frac(self):
        self.assertEqual(cmp_frac([1, 2], [1, 3]), 1)
        self.assertEqual(cmp_frac([1, 2], [1, 2]), 0)
        self.assertEqual(cmp_frac([5, 2], [7, 2]), -1)

    def test_frac2float(self):
        self.assertEqual(frac2float([3,2]), 1.5)

    def test_tearDown(self):
        self.assertEqual(tearDown([2,4]), [1,2])
        self.assertEqual(tearDown([3,6]), [1,2])


if __name__ == '__main__':
    unittest.main()     # uruchamia wszystkie testy