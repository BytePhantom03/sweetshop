import unittest
from sweetshop_final.manager.sweet_manager import SweetManager

class TestUpdateSweet(unittest.TestCase):

    def setUp(self):
        self.manager = SweetManager()
        self.manager.add_sweet(1, "Ladoo", "Indian", 10, 5)

    # ✅ Update All Fields
    def test_update_all_fields(self):
        updated = self.manager.update_sweet(1, name="Barfi", category="Milk", price=15, quantity=20)
        self.assertEqual(updated["name"], "Barfi")
        self.assertEqual(updated["category"], "Milk")
        self.assertEqual(updated["price"], 15)
        self.assertEqual(updated["quantity"], 20)

    # ✅ Partial Update (Only Name)
    def test_update_partial_name(self):
        updated = self.manager.update_sweet(1, name="Rasgulla")
        self.assertEqual(updated["name"], "Rasgulla")
        self.assertEqual(updated["category"], "Indian")  # unchanged

    # ✅ Partial Update (Only Price and Quantity)
    def test_update_price_and_quantity(self):
        updated = self.manager.update_sweet(1, price=25, quantity=15)
        self.assertEqual(updated["price"], 25)
        self.assertEqual(updated["quantity"], 15)

    # ✅ Update with Invalid ID
    def test_update_non_existent_sweet(self):
        with self.assertRaises(ValueError):
            self.manager.update_sweet(999, name="NonExistent")

    # ✅ Update with None as ID
    def test_update_with_none_id(self):
        with self.assertRaises(ValueError):
            self.manager.update_sweet(None, name="Invalid")

    # ✅ Update with Empty String ID
    def test_update_with_empty_string_id(self):
        with self.assertRaises(ValueError):
            self.manager.update_sweet("", name="Invalid")

    # ✅ Update with Whitespace ID
    def test_update_with_whitespace_id(self):
        with self.assertRaises(ValueError):
            self.manager.update_sweet("   ", name="Invalid")

    # ✅ Update with Empty Name
    def test_update_with_empty_name(self):
        with self.assertRaises(ValueError):
            self.manager.update_sweet(1, name="")

    # ✅ Update with Whitespace Category
    def test_update_with_spaces_only_category(self):
        with self.assertRaises(ValueError):
            self.manager.update_sweet(1, category="   ")

    # ✅ Update with Negative Price
    def test_update_with_negative_price(self):
        with self.assertRaises(ValueError):
            self.manager.update_sweet(1, price=-10)

    # ✅ Update with Negative Quantity
    def test_update_with_negative_quantity(self):
        with self.assertRaises(ValueError):
            self.manager.update_sweet(1, quantity=-5)

    # ✅ Update with Zero Quantity
    def test_update_with_zero_quantity(self):
        with self.assertRaises(ValueError):
            self.manager.update_sweet(1, quantity=0)

    # ✅ No Update Parameters Provided
    def test_update_with_no_fields(self):
        with self.assertRaises(ValueError):
            self.manager.update_sweet(1)

if __name__ == "__main__":
    unittest.main()
