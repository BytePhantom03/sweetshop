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



    def test_view_sweets(self):
        # Add two sweets
        self.manager.add_sweet(1001, "Kaju Katli", "Nut-Based", 50, 20)
        self.manager.add_sweet(1002, "Gajar Halwa", "Vegetable-Based", 30, 15)

        sweets = self.manager.view_sweets()
        self.assertEqual(len(sweets), 2)
        self.assertEqual(sweets[0]["name"], "Kaju Katli")



if __name__ == "__main__":
    unittest.main()
