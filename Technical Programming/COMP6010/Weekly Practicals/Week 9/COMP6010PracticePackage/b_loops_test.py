import unittest
import b_loops as loops

class Tester(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(loops.sum(1), 1)
        self.assertEqual(loops.sum(2), 3)
        self.assertEqual(loops.sum(3), 6)
        self.assertEqual(loops.sum(10), 55)
        self.assertEqual(loops.sum(7), 28)
        self.assertEqual(loops.sum(30), 465)

    def test_count_divisible_by(self):
        self.assertEqual(loops.count_divisible_by(1, 4, 11), 8)
        self.assertEqual(loops.count_divisible_by(3, 3, 3), 1)
        self.assertEqual(loops.count_divisible_by(3, 2, 7), 2)
        self.assertEqual(loops.count_divisible_by(5, 10, 23), 3)
        self.assertEqual(loops.count_divisible_by(5, 11, 24), 2)
        self.assertEqual(loops.count_divisible_by(5, -11, 24), 7)

    def test_sum_even(self):
        self.assertEqual(loops.sum_even(2, 6), 6)
        self.assertEqual(loops.sum_even(6, 14), 36)
        self.assertEqual(loops.sum_even(10, 20), 70)
        self.assertEqual(loops.sum_even(5, 14), 36)
        self.assertEqual(loops.sum_even(6, 15), 50)
        self.assertEqual(loops.sum_even(5, 15), 50)
     
    def test_sum_even_2(self):
        self.assertEqual(loops.sum_even_2(2), 6)
        self.assertEqual(loops.sum_even_2(5), 30)
        self.assertEqual(loops.sum_even_2(3), 12)
        self.assertEqual(loops.sum_even_2(8), 72)
        self.assertEqual(loops.sum_even_2(6), 42)
        self.assertEqual(loops.sum_even_2(45), 2070)
        
    def test_divisible_in_range(self):
        self.assertTrue(loops.divisible_in_range(3, 3, 3))
        self.assertTrue(loops.divisible_in_range(9, 2, 7))
        self.assertTrue(loops.divisible_in_range(20, 10, 23))
        self.assertTrue(loops.divisible_in_range(45, 10, 23))
        self.assertTrue(loops.divisible_in_range(14, 0, 3))
        self.assertTrue(loops.divisible_in_range(22, 11, 12))
        self.assertFalse(loops.divisible_in_range(47, 10, 23))
        self.assertFalse(loops.divisible_in_range(1, 4, 11))
        self.assertFalse(loops.divisible_in_range(5, 11, 24))
        self.assertFalse(loops.divisible_in_range(47, 0, 0))
        self.assertTrue(loops.divisible_in_range(8, -3, 0))
        
    def test_is_prime(self):
        for i in range(1, 36):
            if i == 2 or i == 3 or i == 5 or i == 7 or i == 11 or i == 13 or i == 17 or i == 19 or i == 23 or i == 29 or i == 31:
                self.assertTrue(loops.is_prime(i))
            else:
                self.assertFalse(loops.is_prime(i))
                
    def test_num_primes(self):
        self.assertEqual(loops.num_primes(0, 8), 4)
        self.assertEqual(loops.num_primes(1, 11), 4)
        self.assertEqual(loops.num_primes(2, 11), 3)
        self.assertEqual(loops.num_primes(2, 12), 4)
        self.assertEqual(loops.num_primes(45, 256), 40)
        self.assertEqual(loops.num_primes(17, 165), 31)
        self.assertEqual(loops.num_primes(15, 165), 32)
        self.assertEqual(loops.num_primes(17, 17), 0)
        self.assertEqual(loops.num_primes(16, 17), 0)
        
    def test_binary(self):
        for i in range(1, 5000):
            self.assertEqual(loops.binary(i), bin(i)[2:])
            
    def test_first_power(self):
        self.assertEqual(loops.first_power(124, 5), 125)
        self.assertEqual(loops.first_power(16, 2), 16)
        self.assertEqual(loops.first_power(31, 2), 32)
        self.assertEqual(loops.first_power(900, 3), 2187)
        self.assertEqual(loops.first_power(900, -3), 6561)
        self.assertEqual(loops.first_power(-3, -90), 8100)
        
    def test_palindrome(self):
        self.assertTrue(loops.palindrome(""))
        self.assertTrue(loops.palindrome("I"))
        self.assertTrue(loops.palindrome("anna"))
        self.assertTrue(loops.palindrome("level"))
        self.assertTrue(loops.palindrome("kayak"))
        self.assertTrue(loops.palindrome("redder"))
        self.assertFalse(loops.palindrome("refers"))
        self.assertFalse(loops.palindrome("Madam"))
        self.assertFalse(loops.palindrome("madim"))
        self.assertFalse(loops.palindrome("hanoah"))
        
    def test_pyramids(self):
        self.assertEqual(loops.pyramids(1), 1)
        self.assertEqual(loops.pyramids(10), 2)
        self.assertEqual(loops.pyramids(35), 3)
        self.assertEqual(loops.pyramids(84), 4)
        self.assertEqual(loops.pyramids(85), 4)
        self.assertEqual(loops.pyramids(83), 3)
        self.assertEqual(loops.pyramids(70), 3)
        self.assertEqual(loops.pyramids(95038230423), 4146)
        
    def test_scrambled_letters(self):
        self.assertEqual(loops.scrambled_letters('bcz'), 2)
        self.assertEqual(loops.scrambled_letters('czecb'), 3)
        self.assertEqual(loops.scrambled_letters('zabcdef'), 0)
        self.assertEqual(loops.scrambled_letters('hacacacz'), 1)
        self.assertEqual(loops.scrambled_letters('bgzacae'), 4)
        
    def test_sum_multiple_even(self):
        self.assertEqual(loops.sum_multiple_even(3, 8), 44)
        self.assertEqual(loops.sum_multiple_even(2, 8), 61)
        self.assertEqual(loops.sum_multiple_even(4, 9), 49)
        self.assertEqual(loops.sum_multiple_even(5, 12), 114)
    
if __name__ == "__main__":    
    unittest.main() 