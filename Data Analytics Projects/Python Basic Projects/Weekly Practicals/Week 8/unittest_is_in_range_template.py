import unittest
import math

def square(n):
    return n**1/2

def is_positive(n):
    if n > 0:
        return True
    else:
        return False
    
def average(a,b):
    return (a+b)/2

class TestMyCode(unittest.TestCase):
    def test_my_function(self):
        self.assertEqual(square(5), 25)
    
    def test_negative(self):
        self.assertEqual(square(-2),4)
    
    def test_float(self):
        self.assertEqual(square(2.5),6.25)
    
    def test_zero(self)
        self.assertEqual(square(0),0)

    def test_one(self)
        self.assertEqual(square(1),1)

    def test_true(self)
        self.assertTrue(is_positive(20))
        self.assertAlmostEqual(average(3,4),3.5)


def is_in_range(n, min, max):
    if n > min and n < max:
        return True
    else:
        return False

class Tester(unittest.TestCase):
    def test_is_in_range(self):
        self.assertTrue(is_in_range(10.2, 5.3, 18.9))
        self.assertTrue(is_in_range(-5.1, -5.1, 218.9))
        self.assertTrue(is_in_range(183.9, 5.3, 183.9))
        self.assertTrue(is_in_range(-5.09, -5.1, 218.9))
        self.assertTrue(is_in_range(183.8, 5.3, 183.9))
        self.assertFalse(is_in_range(5.2, 5.3, 18.9))
        self.assertFalse(is_in_range(18.91, 5.3, 18.9))
        self.assertFalse(is_in_range(-1118.9, 5.3, 1118.9))
        self.assertFalse(is_in_range(1729, 5.3, 1728))
        self.assertFalse(is_in_range(-5.11, -5.1, 218.9))
    
'''
return True if val is between low and high (inclusive on both sides), False otherwise.
'''
def is_in_range(val, low, high):
    return False

if __name__ == "__main__":    
    unittest.main() 
