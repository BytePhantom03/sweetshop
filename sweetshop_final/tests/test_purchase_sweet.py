import unittest
from sweetshop_final.manager.sweet_manager import SweetManager

class TestPurchaseSweet(unittest.TestCase):

    def setUp(self):
        self.manager = SweetManager()
        self.manager.add_sweet(1, "Ladoo", "Indian", 10, 10)  # initial stock: 10

    # ✅ Valid Purchase
    def test_valid_purchase(self):
        result = self.manager.purchase_sweet(1, 3)
        self.assertEqual(result["quantity"], 7)  # 10 - 3

    # ✅ Purchase Full Quantity
    def test_purchase_entire_stock(self):
        result = self.manager.purchase_sweet(1, 10)
        self.assertEqual(result["quantity"], 0)

    # ❌ Purchase More Than Stock
    def test_purchase_more_than_available(self):
        with self.assertRaises(ValueError):
            self.manager.purchase_sweet(1, 15)

    # ❌ Purchase Zero Quantity
    def test_purchase_zero_quantity(self):
        with self.assertRaises(ValueError):
            self.manager.purchase_sweet(1, 0)

    # ❌ Purchase Negative Quantity
    def test_purchase_negative_quantity(self):
        with self.assertRaises(ValueError):
            self.manager.purchase_sweet(1, -5)

    # ❌ Purchase Non-Existent Sweet
    def test_purchase_non_existent_id(self):
        with self.assertRaises(ValueError):
            self.manager.purchase_sweet(999, 1)

    # ❌ Purchase with None as ID
    def test_purchase_with_none_id(self):
        with self.assertRaises(ValueError):
            self.manager.purchase_sweet(None, 1)

    # ❌ Purchase with Empty String ID
    def test_purchase_with_empty_string_id(self):
        with self.assertRaises(ValueError):
            self.manager.purchase_sweet("", 1)

    # ❌ Purchase with Whitespace ID
    def test_purchase_with_whitespace_id(self):
        with self.assertRaises(ValueError):
            self.manager.purchase_sweet("   ", 1)

    # ✅ Purchase using special character ID
    def test_purchase_special_character_id(self):
        self.manager.add_sweet("S@100", "Halwa", "Special", 20, 5)
        result = self.manager.purchase_sweet("S@100", 2)
        self.assertEqual(result["quantity"], 3)

if __name__ == "__main__":
    unittest.main()
