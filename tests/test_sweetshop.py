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


    def test_purchase_sweet_success(self):
        self.manager.add_sweet(1006, "Barfi", "Milk-Based", 25, 10)
        result = self.manager.purchase_sweet(1006, 3)
        self.assertTrue(result)
        sweet = self.manager.sweets[1006]
        self.assertEqual(sweet.quantity, 7)

    def test_purchase_sweet_insufficient_stock(self):
        self.manager.add_sweet(1007, "Peda", "Milk-Based", 20, 2)
        with self.assertRaises(ValueError):
            self.manager.purchase_sweet(1007, 5)

    def test_restock_sweet(self):
        self.manager.add_sweet(1008, "Soan Papdi", "Flaky", 15, 5)
        result = self.manager.restock_sweet(1008, 10)
        self.assertTrue(result)
        sweet = self.manager.sweets[1008]
        self.assertEqual(sweet.quantity, 15)

    
    def test_update_sweet(self):
        self.manager.add_sweet(1009, "Jalebi", "Sugar-Based", 15, 30)

        updated = self.manager.update_sweet(
            sweet_id=1009,
            name="Jalebi Special",
            category="Festival",
            price=20,
            quantity=40
        )

        self.assertEqual(updated["name"], "Jalebi Special")
        self.assertEqual(updated["category"], "Festival")
        self.assertEqual(updated["price"], 20)
        self.assertEqual(updated["quantity"], 40)







if __name__ == "__main__":
    unittest.main()
