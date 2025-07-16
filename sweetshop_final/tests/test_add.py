import unittest
from sweetshop_final.manager.sweet_manager import SweetManager

class TestAddSweet(unittest.TestCase):

    def setUp(self):
        self.manager = SweetManager()

    # ✅ Valid Sweet Addition
    def test_add_valid_sweet(self):
        sweet = self.manager.add_sweet(1, "Ladoo", "Indian", 10, 5)
        self.assertEqual(sweet["id"], 1)
        self.assertEqual(sweet["name"], "Ladoo")
        self.assertEqual(len(self.manager.sweets), 1)

    # ✅ Duplicate ID
    def test_add_duplicate_sweet_id(self):
        self.manager.add_sweet(1, "Ladoo", "Indian", 10, 5)
        with self.assertRaises(ValueError):
            self.manager.add_sweet(1, "Barfi", "Milk", 20, 5)

    # ✅ Empty ID
    def test_add_sweet_with_empty_id(self):
        with self.assertRaises(ValueError):
            self.manager.add_sweet("", "Ladoo", "Indian", 10, 5)

    # ✅ Whitespace ID
    def test_add_sweet_with_whitespace_id(self):
        with self.assertRaises(ValueError):
            self.manager.add_sweet("   ", "Ladoo", "Indian", 10, 5)

    # ✅ None as ID
    def test_add_sweet_with_none_id(self):
        with self.assertRaises(ValueError):
            self.manager.add_sweet(None, "Ladoo", "Indian", 10, 5)

    # ✅ Negative ID
    def test_add_sweet_with_negative_id(self):
        with self.assertRaises(ValueError):
            self.manager.add_sweet(-10, "Invalid", "Error", 10, 5)

    # ✅ ID as zero
    def test_add_sweet_with_zero_integer_id(self):
        sweet = self.manager.add_sweet(0, "ZeroSweet", "Special", 15, 5)
        self.assertEqual(sweet["id"], 0)
        self.assertIn(0, self.manager.sweets)

    # ✅ ID as numeric string
    def test_add_sweet_with_numeric_string_id(self):
        sweet = self.manager.add_sweet("001", "Chocolate", "Candy", 5, 25)
        self.assertEqual(sweet["id"], "001")
        self.assertIn("001", self.manager.sweets)

    # ✅ Special characters in ID
    def test_add_sweet_with_special_characters_in_id(self):
        sweet = self.manager.add_sweet("S#@123", "Barfi", "Milk", 25, 10)
        self.assertEqual(sweet["id"], "S#@123")
        self.assertIn("S#@123", self.manager.sweets)

    # ✅ Negative Price
    def test_add_sweet_with_negative_price(self):
        with self.assertRaises(ValueError):
            self.manager.add_sweet("P-10", "Ladoo", "Dry", -10, 5)

    # ✅ Negative Quantity
    def test_add_sweet_with_negative_quantity(self):
        with self.assertRaises(ValueError):
            self.manager.add_sweet("Q-5", "Ladoo", "Dry", 10, -5)

    # ✅ Zero Quantity
    def test_add_sweet_with_zero_quantity(self):
        with self.assertRaises(ValueError):
            self.manager.add_sweet("Q0", "Ladoo", "Dry", 10, 0)

    # ✅ Empty Name
    def test_add_sweet_with_empty_name(self):
        with self.assertRaises(ValueError):
            self.manager.add_sweet("E1", "", "Dry", 10, 5)

    # ✅ Name with only spaces
    def test_add_sweet_with_spaces_only_name(self):
        with self.assertRaises(ValueError):
            self.manager.add_sweet("E2", "   ", "Milk", 10, 5)

    # ✅ Empty Category
    def test_add_sweet_with_empty_category(self):
        with self.assertRaises(ValueError):
            self.manager.add_sweet("E3", "Ladoo", "", 10, 5)

    # ✅ Category with only spaces
    def test_add_sweet_with_spaces_only_category(self):
        with self.assertRaises(ValueError):
            self.manager.add_sweet("E4", "Rasgulla", "   ", 10, 5)

if __name__ == "__main__":
    unittest.main()
