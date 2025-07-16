import unittest
from sweetshop_final.manager.sweet_manager import SweetManager

class TestSearchSweet(unittest.TestCase):

    def setUp(self):
        self.manager = SweetManager()
        self.manager.add_sweet(1, "Ladoo", "Indian", 10, 5)
        self.manager.add_sweet(2, "Barfi", "Milk", 15, 10)
        self.manager.add_sweet(3, "Chocolate Bar", "Candy", 20, 8)
        self.manager.add_sweet(4, "Laddu Special", "Festival", 12, 6)

    # ✅ Exact Match
    def test_search_exact_match(self):
        results = self.manager.search_sweets("Barfi")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]["name"], "Barfi")

    # ✅ Partial Match (Beginning)
    def test_search_partial_match_start(self):
        results = self.manager.search_sweets("Lad")
        self.assertEqual(len(results), 2)

    # ✅ Partial Match (Anywhere)
    def test_search_partial_match_anywhere(self):
        results = self.manager.search_sweets("colate")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]["name"], "Chocolate Bar")

    # ✅ Case Insensitive Match
    def test_search_case_insensitive(self):
        self.manager.add_sweet(10, "Ladoo", "Indian", 10, 5)
        results = self.manager.search_sweets("lADoO")
        print("DEBUG:", results)  # <- TEMPORARY
        self.assertTrue(any(sweet["name"].lower() == 'ladoo' for sweet in results))


    # ❌ No Match
    def test_search_no_match(self):
        results = self.manager.search_sweets("Jalebi")
        self.assertEqual(results, [])

    # ❌ Empty Search String
    def test_search_with_empty_string(self):
        with self.assertRaises(ValueError):
            self.manager.search_sweets("")

    # ❌ Whitespace Search String
    def test_search_with_whitespace(self):
        with self.assertRaises(ValueError):
            self.manager.search_sweets("   ")

    # ❌ None as Search Term
    def test_search_with_none(self):
        with self.assertRaises(ValueError):
            self.manager.search_sweets(None)

if __name__ == "__main__":
    unittest.main()
