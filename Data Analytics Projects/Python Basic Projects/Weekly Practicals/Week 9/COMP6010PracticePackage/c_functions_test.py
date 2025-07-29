import unittest
import c_functions as functions

class Tester(unittest.TestCase):
    def test_cube(self):
        self.assertEqual(functions.cube(5), 125)
        self.assertEqual(functions.cube(3), 27)
        self.assertEqual(functions.cube(4), 64)
        self.assertEqual(functions.cube(12), 1728)
        self.assertEqual(functions.cube(-2), -8)
    
    def test_repeat_pattern(self):
        self.assertEqual(functions.repeat_pattern("abc", 3), "abcabcabc")
        self.assertEqual(functions.repeat_pattern("a", 4), "aaaa")
        self.assertEqual(functions.repeat_pattern("hahi", 5), "hahihahihahihahihahi")
        
    def test_mean(self):
        self.assertEqual(functions.mean(10, 15, 20), 15)
        self.assertEqual(functions.mean(15, 10, 20), 15)
        self.assertEqual(functions.mean(10, 20, 15), 15)
        self.assertAlmostEqual(functions.mean(10, 10, 18), 12.6666, places=3)
        self.assertAlmostEqual(functions.mean(11, 70, 14), 31.6666, places=3)
        self.assertAlmostEqual(functions.mean(50, 20, 30), 33.3333, places=3)
        
    
    def test_median(self):
        self.assertEqual(functions.median(10, 14, 20), 14)
        self.assertEqual(functions.median(14, 10, 20), 14)
        self.assertEqual(functions.median(10, 20, 14), 14)
        self.assertEqual(functions.median(11, 70, 14), 14)
        self.assertEqual(functions.median(50, 20, 30), 30)
        self.assertEqual(functions.median(10, 10, 18), 10)
        self.assertEqual(functions.median(10, 10, 10), 10)
        self.assertEqual(functions.median(18, 10, 10), 10)
        self.assertEqual(functions.median(10, 18, 10), 10)
    
    def test_num_digits(self):
        self.assertEqual(functions.num_digits(1729), 4)
        self.assertEqual(functions.num_digits(1729304), 7)
        self.assertEqual(functions.num_digits(0), 0)
        self.assertEqual(functions.num_digits(3), 1)
        self.assertEqual(functions.num_digits(12643), 5)
    
    def test_sum_digits(self):
        self.assertEqual(functions.sum_digits(1729), 19)
        self.assertEqual(functions.sum_digits(1729304), 26)
        self.assertEqual(functions.sum_digits(0), 0)
        self.assertEqual(functions.sum_digits(3), 3)
        self.assertEqual(functions.sum_digits(12643), 16)
    
    def test_sum_digit_less(self):
        self.assertEqual(functions.sum_digits_less(1729, 8), 10)
        self.assertEqual(functions.sum_digits_less(1729, 7), 3)
        self.assertEqual(functions.sum_digits_less(17293504, 6), 15)
        self.assertEqual(functions.sum_digits_less(34567, 2), 0)
    
    def test_gcd(self):
        self.assertEqual(functions.gcd(100, 35), 5)
        self.assertEqual(functions.gcd(35, 100), 5)
        self.assertEqual(functions.gcd(15, 32), 1)
        self.assertEqual(functions.gcd(-51, 153), 51)
        self.assertEqual(functions.gcd(51, -153), 51)
        self.assertEqual(functions.gcd(80, 36), 4)
    
    def test_sum_odd(self):
        self.assertEqual(functions.sum_odd(3, 7), 8)
        self.assertEqual(functions.sum_odd(-3, 7), 5)
        self.assertEqual(functions.sum_odd(5, 8), 12)
        self.assertEqual(functions.sum_odd(4, 7), 5)
        self.assertEqual(functions.sum_odd(4, 8), 12)
        self.assertEqual(functions.sum_odd(40, 93), 1716)
    
    def test_sum_odd_2(self):
        self.assertEqual(functions.sum_odd_2(3), 9)
        self.assertEqual(functions.sum_odd_2(7), 49)
        self.assertEqual(functions.sum_odd_2(4), 16)
        self.assertEqual(functions.sum_odd_2(9), 81)
        
    def test_contains_all(self):
        self.assertTrue(functions.contains_all("lab", "lambda"))
        self.assertFalse(functions.contains_all("tea", "nintendo"))
        self.assertTrue(functions.contains_all("tee", "nintendo"))
        self.assertTrue(functions.contains_all("abce", "bccade"))
        self.assertFalse(functions.contains_all("abce", "ccade"))
        
    def test_remove_n(self):
        self.assertEqual(functions.remove_n("nintendo", "n", 2), "itendo")
        self.assertEqual(functions.remove_n("papaya", "pa", 10), "ya")
        self.assertEqual(functions.remove_n("paApaya", "pa", 1), "Apaya")
        self.assertEqual(functions.remove_n("A good cook could cook as many cookies as a good cook who could cook cookies", "coo", 4), "A good k could k as many kies as a good k who could cook cookies")
        self.assertEqual(functions.remove_n("Silly Sally swiftly shooed seven silly sheep. The seven silly sheep Silly Sally shooed shilly-shallied south. These sheep shouldn't sleep in a shack.", "ill", 100), "Sy Sally swiftly shooed seven sy sheep. The seven sy sheep Sy Sally shooed shy-shallied south. These sheep shouldn't sleep in a shack.")
    
    
if __name__ == "__main__":    
    unittest.main() 