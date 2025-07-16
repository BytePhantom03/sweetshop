import unittest
from sweetshop_final.manager.sweet_manager import SweetManager

class TestDeleteSweet(unittest.TestCase):

    def setUp(self):
        self.manager = SweetManager()
        self.manager.add_sweet(1, "Ladoo", "Indian", 10, 5)
        self.manager.add_sweet(2, "Barfi", "Milk", 15, 10)

    # ✅ Delete Existing Sweet
    def test_delete_existing_sweet(self):
        result = self.manager.delete_sweet(1)
        self.assertTrue(result)
        self.assertNotIn(1, self.manager.sweets)

    # ✅ Delete Already Deleted Sweet
    def test_delete_sweet_twice(self):
        self.manager.delete_sweet(1)
        with self.assertRaises(ValueError):
            self.manager.delete_sweet(1)

    # ✅ Delete Non-Existent ID
    def test_delete_non_existent_sweet(self):
        with self.assertRaises(ValueError):
            self.manager.delete_sweet(999)

    # ✅ Delete with None ID
    def test_delete_with_none_id(self):
        with self.assertRaises(ValueError):
            self.manager.delete_sweet(None)

    # ✅ Delete with Empty String ID
    def test_delete_with_empty_string_id(self):
        with self.assertRaises(ValueError):
            self.manager.delete_sweet("")

    # ✅ Delete with Whitespace ID
    def test_delete_with_whitespace_id(self):
        with self.assertRaises(ValueError):
            self.manager.delete_sweet("   ")

    # ✅ Delete with Special Character ID (Valid Case)
    def test_delete_special_character_id(self):
        self.manager.add_sweet("S#1", "Halwa", "Special", 20, 10)
        self.assertTrue(self.manager.delete_sweet("S#1"))
        self.assertNotIn("S#1", self.manager.sweets)

if __name__ == "__main__":
    unittest.main()
