import unittest
import e_dictionaries as dictionaries

class Tester(unittest.TestCase):
    def test_is_none(self):
        self.assertTrue(dictionaries.is_none(None))
        self.assertFalse(dictionaries.is_none({10:"Gaurav", 70:"Carl", 20:"Emilie", 90:"Yan"}))
        
    def test_add_value(self):
        self.assertEqual(dictionaries.add_value(None, 0, 5), {0:5})
        self.assertEqual(dictionaries.add_value({10:"Gaurav", 70:"Carl", 20:"Emilie", 90:"Yan"}, 10, "Afroja"), {10:"Gaurav", 70:"Carl", 20:"Emilie", 90:"Yan"})
        self.assertEqual(dictionaries.add_value({10:"Gaurav", 70:"Carl", 20:"Emilie", 90:"Yan"}, "Nat", "David"), {10:"Gaurav", 70:"Carl", 20:"Emilie", 90:"Yan", "Nat":"David"})
        
    def test_occurances(self):
        self.assertEqual(dictionaries.occurances(None), None)
        self.assertEqual(dictionaries.occurances([10, 70, 20, 90]), {10:1, 70:1, 20:1, 90:1})
        self.assertEqual(dictionaries.occurances([10, 70, 20, 20, 20, 90, "Nat", 70, 10, "Charanya"]), {10:2, 70:2, 20:3, 90:1, "Nat":1, "Charanya":1})
        
    def test_min_dist(self):
        self.assertEqual(dictionaries.min_dist(None), None)
        self.assertEqual(dictionaries.min_dist([10, 70, 20, 90]), 4)
        self.assertEqual(dictionaries.min_dist([10, 70, 20, 20, 20, 90, "Nat", 70, 10, "Charanya"]), 1)
        self.assertEqual(dictionaries.min_dist([70, 20, 10, "Gaurav", 90, 70, 10, "Gaurav"]), 4)
        self.assertEqual(dictionaries.min_dist([10, 70, 20, 10, 20, 90, "Nat", 70, 10, "Charanya"]), 2)
        
    def test_most_popular_list(self):
        self.assertEqual(dictionaries.most_popular_list(None), None)
        self.assertEqual(
            q.most_popular_list([[10, 70, 20, 90], 
                               [10, 70, 20, 90], 
                               [10, 90, 20, 70]]), ([(10, 20, 70, 90)], 3))
        self.assertEqual(
            q.most_popular_list([[10, 70, 20, 90], 
                               [1, 7, 20, 90], 
                               [10, 90, 20, 70],
                               [1, 20, 7, 90],
                               [90, 7, 20, 1]]), ([(1, 7, 20, 90)], 3))
        self.assertEqual(
            q.most_popular_list([[10, 70, 20, 90], 
                               [-1, 7, 20, 90], 
                               [10, 90, 20, 70],
                               [-1, 90, 7, 20], 
                               [-1, -7, 4, 33]]), ([(10, 20, 70, 90), (-1, 7, 20, 90)], 2))
        
if __name__ == "__main__":    
    unittest.main() 