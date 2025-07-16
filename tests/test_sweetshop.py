import unittest
from sweetshop.manager import SweetManager

class TestSweetShop(unittest.TestCase):
    def setUp(self):
        self.manager = SweetManager()

    def test_add_sweet(self):
        sweet = self.manager.add_sweet(
            sweet_id=1001,
            name="Kaju Katli",
            category="Nut-Based",
            price=50,
            quantity=20
        )
        self.assertEqual(sweet["id"], 1001)
        self.assertEqual(sweet["name"], "Kaju Katli")
        self.assertEqual(len(self.manager.sweets), 1)

    def test_delete_sweet(self):
        # First, add a sweet
        self.manager.add_sweet(
            sweet_id=1002,
            name="Gajar Halwa",
            category="Vegetable-Based",
            price=30,
            quantity=15
        )

        # Now delete it
        result = self.manager.delete_sweet(1002)

        self.assertTrue(result)
        self.assertNotIn(1002, self.manager.sweets)


if __name__ == "__main__":
    unittest.main()
