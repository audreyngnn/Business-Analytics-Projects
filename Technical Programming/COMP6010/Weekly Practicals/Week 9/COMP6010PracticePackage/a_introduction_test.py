import unittest
import a_introduction as introduction

class Tester(unittest.TestCase):
            
    def test_get_last_digit(self):
        self.assertEqual(introduction.get_last_digit(1729), 9)
        self.assertEqual(introduction.get_last_digit(23528435), 5)
        self.assertEqual(introduction.get_last_digit(235284), 4)
        self.assertEqual(introduction.get_last_digit(3), 3)
    
    def test_get_negative_last_digit(self):
        self.assertEqual(introduction.get_negative_last_digit(-1729), 9)
        self.assertEqual(introduction.get_negative_last_digit(-23528435), 5)
        self.assertEqual(introduction.get_negative_last_digit(-235284), 4)
        self.assertEqual(introduction.get_negative_last_digit(-3), 3)

    def test_get_second_last_digit(self):
        self.assertEqual(introduction.get_second_last_digit(1729), 2)
        self.assertEqual(introduction.get_second_last_digit(23528435), 3)
        self.assertEqual(introduction.get_second_last_digit(16), 1)
        self.assertEqual(introduction.get_second_last_digit(-1729), 2)
        self.assertEqual(introduction.get_second_last_digit(-23528435), 3)
        self.assertEqual(introduction.get_second_last_digit(-16), 1)

    def test_get_first_digit(self):
        self.assertEqual(introduction.get_first_digit(1729), 1)
        self.assertEqual(introduction.get_first_digit(31729), 3)
        self.assertEqual(introduction.get_first_digit(2), 2)
        self.assertEqual(introduction.get_first_digit(-1729), 1)
        self.assertEqual(introduction.get_first_digit(-31729), 3)
        self.assertEqual(introduction.get_first_digit(-2), 2)

    def test_both_even(self):
        self.assertTrue(introduction.both_even(12, 18))
        self.assertTrue(introduction.both_even(-12, 18))
        self.assertTrue(introduction.both_even(12, 0))
        self.assertFalse(introduction.both_even(12, 17))
        self.assertFalse(introduction.both_even(17, 12))
        self.assertFalse(introduction.both_even(-19, 17))
        self.assertFalse(introduction.both_even(0, 17))

    def test_both_odd(self):
        self.assertTrue(introduction.both_odd(19, 17))
        self.assertTrue(introduction.both_odd(-19, 17))
        self.assertTrue(introduction.both_odd(19, -17))
        self.assertTrue(introduction.both_odd(1729, 927113))
        self.assertFalse(introduction.both_odd(12, 18))
        self.assertFalse(introduction.both_odd(-12, 18))
        self.assertFalse(introduction.both_odd(-12, 17))
        self.assertFalse(introduction.both_odd(12, 0))
        self.assertFalse(introduction.both_odd(12, 17))
        self.assertFalse(introduction.both_odd(17, 12))
        self.assertFalse(introduction.both_odd(0, 17))

    def test_different_oddity(self):
        self.assertFalse(introduction.different_oddity(19, 17))
        self.assertFalse(introduction.different_oddity(-19, 17))
        self.assertFalse(introduction.different_oddity(19, -17))
        self.assertFalse(introduction.different_oddity(1729, 927113))
        self.assertFalse(introduction.different_oddity(12, 18))
        self.assertFalse(introduction.different_oddity(-12, 18))
        self.assertTrue(introduction.different_oddity(-12, 17))
        self.assertFalse(introduction.different_oddity(12, 0))
        self.assertTrue(introduction.different_oddity(12, 17))
        self.assertTrue(introduction.different_oddity(17, 12))
        self.assertTrue(introduction.different_oddity(0, 17))

    def test_atleast_one_odd(self):
        self.assertFalse(introduction.atleast_one_odd(10, 20, 30, 40, 50))
        self.assertTrue(introduction.atleast_one_odd(11, 20, 30, 40, 50))
        self.assertTrue(introduction.atleast_one_odd(-11, 20, 30, 40, 50))
        self.assertTrue(introduction.atleast_one_odd(10, 27, 30, 40, 50))
        self.assertTrue(introduction.atleast_one_odd(10, -27, 30, 40, 50))
        self.assertTrue(introduction.atleast_one_odd(10, 20, 31, 40, 50))
        self.assertTrue(introduction.atleast_one_odd(10, 20, -31, 40, 50))
        self.assertTrue(introduction.atleast_one_odd(10, 20, 30, 45, 50))
        self.assertTrue(introduction.atleast_one_odd(10, 20, 30, -45, 50))
        self.assertTrue(introduction.atleast_one_odd(10, 20, 30, 40, 59))
        self.assertTrue(introduction.atleast_one_odd(10, 20, 30, 40, -59))
        self.assertTrue(introduction.atleast_one_odd(19, 20, 31, 40, 50))
        self.assertTrue(introduction.atleast_one_odd(10, 21, 30, 47, 53))
        self.assertTrue(introduction.atleast_one_odd(11, 23, 35, 47, 50))
        self.assertTrue(introduction.atleast_one_odd(10, 29, 37, 45, 53))
        
            
    def test_higher(self):
        self.assertEqual(introduction.higher(10, 70, 20), 70)
        self.assertEqual(introduction.higher(70, 10, 20), 70)
        self.assertEqual(introduction.higher(10, 20, 70), 70)
        self.assertEqual(introduction.higher(10, 20, 20), 20)
        self.assertEqual(introduction.higher(20, 10, 20), 20)
        self.assertEqual(introduction.higher(20, 20, 20), 20)
        self.assertEqual(introduction.higher(1, 11, 2.5), 11)
        
    def test_first_char(self):
        self.assertEqual(introduction.first_char("Super Nintendo Chalmers"), 'S')
        self.assertEqual(introduction.first_char("Nintendo"), 'N')
        self.assertEqual(introduction.first_char("$"), '$')
        
    def test_last_char(self):
        self.assertEqual(introduction.last_char("Super Nintendo Chalmers!"), '!')
        self.assertEqual(introduction.last_char("Nintendo"), 'o')
        self.assertEqual(introduction.last_char("$"), '$')
        
    def test_all_but_first_word(self):
        self.assertEqual(introduction.all_but_first_word("Super Nintendo Chalmers"), "Nintendo Chalmers")
        self.assertEqual(introduction.all_but_first_word("There's literally no one in the world that I don't hate right now"), "literally no one in the world that I don't hate right now")
        self.assertEqual(introduction.all_but_first_word("I am removing the first word"), "am removing the first word")
        
    def test_caesar_cipher(self):
        self.assertEqual(introduction.caesar_cipher('a', 1), 'b')
        self.assertEqual(introduction.caesar_cipher('c', 3), 'f')
        self.assertEqual(introduction.caesar_cipher('z', 1), 'a')
        self.assertEqual(introduction.caesar_cipher('b', 26), 'b')
        self.assertEqual(introduction.caesar_cipher('k', 32), 'q')
        self.assertEqual(introduction.caesar_cipher('x', 85), 'e')
        self.assertEqual(introduction.caesar_cipher('p', 1065), 'o')
        
    def test_manhattan_distance(self):
        self.assertEqual(introduction.manhattan_distance(5, 1, 5, 4), 3)
        self.assertEqual(introduction.manhattan_distance(5, 4, 5, 1), 3)
        self.assertEqual(introduction.manhattan_distance(10, 1, 70, 1), 60)
        self.assertEqual(introduction.manhattan_distance(-10, 1, -70, 1), 60)
        self.assertEqual(introduction.manhattan_distance(10, 2, 70, 3), 61)
        self.assertEqual(introduction.manhattan_distance(10, 5, 90, 3), 82)
        
    def test_distance(self):
        self.assertAlmostEqual(introduction.distance(1, 5, 1, 5), 0, places=4)
        self.assertAlmostEqual(introduction.distance(5, 1, 5, 4), 3, places=4)
        self.assertAlmostEqual(introduction.distance(1, 3, 4, 5), 3.60555, places=4)
        self.assertAlmostEqual(introduction.distance(5, 4, 5, 1), 3, places=4)
        self.assertAlmostEqual(introduction.distance(34, 15, 2, 18), 32.1403, places=4)
        self.assertAlmostEqual(introduction.distance(-10, 1, -70, 1), 60, places=4)
        self.assertAlmostEqual(introduction.distance(10, 2, 70, 3), 60.008332, places=4)
        self.assertAlmostEqual(introduction.distance(10, 5, 90, 3), 80.02499, places=4)
        
    def test_decimal_difference(self):
        self.assertAlmostEqual(introduction.decimal_difference(10.0), 0, places=4)
        self.assertAlmostEqual(introduction.decimal_difference(70.5), 0.5, places=4)
        self.assertAlmostEqual(introduction.decimal_difference(20.25), 0.25, places=4)
        self.assertAlmostEqual(introduction.decimal_difference(90.75), 0.25, places=4)
        self.assertAlmostEqual(introduction.decimal_difference(-10.0), 0, places=4)
        self.assertAlmostEqual(introduction.decimal_difference(-70.5), 0.5, places=4)
        self.assertAlmostEqual(introduction.decimal_difference(-20.25), 0.25, places=4)
        self.assertAlmostEqual(introduction.decimal_difference(-90.75), 0.25, places=4)
        self.assertAlmostEqual(introduction.decimal_difference(20.504), 0.496, places=4)
        
    def test_days_in_year(self):
        self.assertAlmostEqual(introduction.days_in_year(2022), 365)
        self.assertAlmostEqual(introduction.days_in_year(2021), 365)
        self.assertAlmostEqual(introduction.days_in_year(2019), 365)
        self.assertAlmostEqual(introduction.days_in_year(2018), 365)
        self.assertAlmostEqual(introduction.days_in_year(2017), 365)
        self.assertAlmostEqual(introduction.days_in_year(2020), 366)
        self.assertAlmostEqual(introduction.days_in_year(2016), 366)
        self.assertAlmostEqual(introduction.days_in_year(2000), 366)
        self.assertAlmostEqual(introduction.days_in_year(2800), 366)
        self.assertAlmostEqual(introduction.days_in_year(1900), 365)
        self.assertAlmostEqual(introduction.days_in_year(1800), 365)
        
    def test_next_multiple(self):
        self.assertEqual(introduction.next_multiple(12, 5), 15)
        self.assertEqual(introduction.next_multiple(10, 5), 15)
        self.assertEqual(introduction.next_multiple(23, 6), 24)
        self.assertEqual(introduction.next_multiple(14, 14), 28)
        self.assertEqual(introduction.next_multiple(14, 15), 15)
        
    def test_compare_to(self):
        self.assertEqual(introduction.compare_to(10, 70), -1)
        self.assertEqual(introduction.compare_to(70, 10), 1)
        self.assertEqual(introduction.compare_to(90, 90), 0)
        
        self.assertEqual(introduction.compare_to(5.4, 4.3), 1)
        self.assertEqual(introduction.compare_to(4.3, 4.4), -1)
        self.assertEqual(introduction.compare_to(10.3, 10.3), 0)
        
        self.assertEqual(introduction.compare_to(True, False), 1)
        self.assertEqual(introduction.compare_to(False, True), -1)
        self.assertEqual(introduction.compare_to(True, True), 0)
        
        self.assertEqual(introduction.compare_to("Desk", "Desks"), -1)
        self.assertEqual(introduction.compare_to("a", "b"), -1)
        self.assertEqual(introduction.compare_to("b", "a"), 1)
        self.assertEqual(introduction.compare_to("Hello", "nintendo"), -1)
        self.assertEqual(introduction.compare_to("hello", "Nintendo"), 1)
        self.assertEqual(introduction.compare_to("Same", "Same"), 0)
        
    def test_find_substring(self):
        self.assertIsNone(introduction.find_substring("Hello", -1, 3))
        self.assertIsNone(introduction.find_substring("Hello", 2, 10))
        self.assertIsNone(introduction.find_substring("Hello", 3, 1))
        self.assertEqual(introduction.find_substring("Hello", 1, 3), "el")
        self.assertEqual(introduction.find_substring("Nintendo", 0, 4), "Nint")
        self.assertEqual(introduction.find_substring("Nintendo", 4, 8), "endo")
        
    def test_reverse(self):
        self.assertEqual(introduction.reverse(""), "")
        self.assertEqual(introduction.reverse("abc"), "cba")
        self.assertEqual(introduction.reverse("super"), "repus")
    
    def test_generate_randomized_total(self):
        occurances = {}
        for i in range(50000):
            total = q.generate_randomized_total()
            dec = total - (int)(total)
            self.assertLessEqual(total, 10000)
            self.assertLessEqual(dec, 100)
            self.assertGreaterEqual(total, 0)
            
            occurances[total] = occurances.get(total, 0) + 1
            self.assertLessEqual(occurances[total], 10)
        

if __name__ == "__main__":    
    unittest.main() 
