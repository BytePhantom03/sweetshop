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

    def test_add_duplicate_sweet_id(self):
        self.manager.add_sweet(1001, "Kaju Katli", "Nut-Based", 50, 20)
        with self.assertRaises(ValueError):
            self.manager.add_sweet(1001, "Another Sweet", "Candy", 25, 10)


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

    
    def test_search_sweets_by_name(self):
        self.manager.add_sweet(1001, "Kaju Katli", "Nut-Based", 50, 20)
        self.manager.add_sweet(1002, "Kaju Roll", "Nut-Based", 60, 10)
        results = self.manager.search_sweets(name="kaju")
        self.assertEqual(len(results), 2)

    def test_search_sweets_by_category(self):
        self.manager.add_sweet(1003, "Gulab Jamun", "Milk-Based", 10, 50)
        results = self.manager.search_sweets(category="Milk-Based")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]["name"], "Gulab Jamun")

    def test_search_sweets_by_price_range(self):
        self.manager.add_sweet(1004, "Ladoo", "General", 20, 40)
        self.manager.add_sweet(1005, "Rasgulla", "Milk-Based", 60, 15)
        results = self.manager.search_sweets(min_price=10, max_price=30)
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]["name"], "Ladoo")




if __name__ == "__main__":
    unittest.main()
