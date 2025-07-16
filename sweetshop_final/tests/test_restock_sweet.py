import unittest
from sweetshop_final.manager.sweet_manager import SweetManager

class TestRestockSweet(unittest.TestCase):

    def setUp(self):
        self.manager = SweetManager()
        self.manager.add_sweet(1, "Ladoo", "Indian", 10, 5)

    # ✅ Valid Restock
    def test_valid_restock(self):
        result = self.manager.restock_sweet(1, 10)
        self.assertEqual(result["quantity"], 15)

    # ✅ Restock Multiple Times
    def test_multiple_restock_accumulates_quantity(self):
        self.manager.restock_sweet(1, 5)
        result = self.manager.restock_sweet(1, 10)
        self.assertEqual(result["quantity"], 20)

    # ❌ Restock Non-Existent Sweet
    def test_restock_non_existent_sweet(self):
        with self.assertRaises(ValueError):
            self.manager.restock_sweet(999, 10)

    # ❌ Restock with Zero Quantity
    def test_restock_with_zero_quantity(self):
        with self.assertRaises(ValueError):
            self.manager.restock_sweet(1, 0)

    # ❌ Restock with Negative Quantity
    def test_restock_with_negative_quantity(self):
        with self.assertRaises(ValueError):
            self.manager.restock_sweet(1, -5)

    # ❌ Restock with None ID
    def test_restock_with_none_id(self):
        with self.assertRaises(ValueError):
            self.manager.restock_sweet(None, 10)

    # ❌ Restock with Empty String ID
    def test_restock_with_empty_string_id(self):
        with self.assertRaises(ValueError):
            self.manager.restock_sweet("", 10)

    # ❌ Restock with Whitespace ID
    def test_restock_with_whitespace_id(self):
        with self.assertRaises(ValueError):
            self.manager.restock_sweet("   ", 10)

    # ✅ Restock Sweet with Special Character ID
    def test_restock_special_character_id(self):
        self.manager.add_sweet("S@200", "Barfi", "Milk", 20, 5)
        result = self.manager.restock_sweet("S@200", 10)
        self.assertEqual(result["quantity"], 15)

if __name__ == "__main__":
    unittest.main()
