import unittest
import numpy as np

def factoriali(n):
    f = 1
    while n > 1:
        f *= n
        n -= 1
    return f

def factorialr(n):
    if n <= 1:
        return 1
    return n * factorialr(n-1)

class TestFactorial(unittest.TestCase):

    def recur(self, n):
        self.assertEqual(factorialr(n), np.math.factorial(n))

    def iter(self, n):
        self.assertEqual(factoriali(n), np.math.factorial(n))

    def test_r0(self):
        self.recur(0)

    def test_r1(self):
        self.recur(1)

    def test_r2(self):
        self.recur(2)

    def test_r3(self):
        self.recur(3)

    def test_r10(self):
        self.recur(10)

    def test_r100(self):
        self.recur(100)

    def test_i0(self):
        self.iter(0)

    def test_i1(self):
        self.iter(1)

    def test_i2(self):
        self.iter(2)

    def test_i3(self):
        self.iter(3)

    def test_i10(self):
        self.iter(10)

    def test_i100(self):
        self.iter(100)

    def test_i100000(self):
        self.iter(100000)

    def test_i100001(self):
        self.iter(100001)

if __name__ == '__main__':
    unittest.main()
