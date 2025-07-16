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

    def test_add_sweet_with_empty_id(self):
        with self.assertRaises(ValueError):
            self.manager.add_sweet("", "Ladoo", "Dry", 10, 5)

    def test_add_sweet_with_whitespace_id(self):
        with self.assertRaises(ValueError):
            self.manager.add_sweet("   ", "Ladoo", "Dry", 10, 5)

    def test_add_sweet_with_none_id(self):
        with self.assertRaises(ValueError):
            self.manager.add_sweet(None, "Ladoo", "Dry", 10, 5)

    def test_add_sweet_with_negative_price(self):
        with self.assertRaises(ValueError):
            self.manager.add_sweet("NEG1", "Ladoo", "Dry", -10, 5)

    def test_add_sweet_with_negative_quantity(self):
        with self.assertRaises(ValueError):
            self.manager.add_sweet("NEG2", "Ladoo", "Dry", 10, -5)

    def test_add_sweet_with_empty_name(self):
        with self.assertRaises(ValueError):
            self.manager.add_sweet("EMPTY_NAME", "", "Dry", 10, 5)

    def test_add_sweet_with_empty_category(self):
        with self.assertRaises(ValueError):
            self.manager.add_sweet("EMPTY_CAT", "Ladoo", "", 10, 5)
    
    def test_add_sweet_with_spaces_only_name(self):
        with self.assertRaises(ValueError):
            self.manager.add_sweet("S123", "   ", "Milk", 10, 5)

    def test_add_sweet_with_spaces_only_category(self):
        with self.assertRaises(ValueError):
            self.manager.add_sweet("S124", "Rasgulla", "   ", 10, 5)


    def test_add_sweet_with_special_characters_in_id(self):
        sweet = self.manager.add_sweet("S@#123", "Barfi", "Milk-Based", 30, 10)
        self.assertEqual(sweet["id"], "S@#123")
        self.assertIn("S@#123", self.manager.sweets)

    def test_add_sweet_with_numeric_string_id(self):
        sweet = self.manager.add_sweet("001", "Chocolate", "Candy", 5, 25)
        self.assertEqual(sweet["id"], "001")
        self.assertIn("001", self.manager.sweets)

    def test_add_sweet_with_integer_id_zero(self):
        sweet = self.manager.add_sweet(0, "ZeroSweet", "Special", 15, 5)
        self.assertEqual(sweet["id"], 0)
        self.assertIn(0, self.manager.sweets)

    def test_add_sweet_with_negative_integer_id(self):
        with self.assertRaises(ValueError):
            self.manager.add_sweet(-10, "InvalidID", "Error", 10, 5)



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
    
    def test_view_sweets_when_empty(self):
        sweets = self.manager.view_sweets()
        self.assertEqual(sweets, [])

    def test_view_sweets_with_many_items(self):
        for i in range(100):
            self.manager.add_sweet(f"S{i}", f"Sweet{i}", "Bulk", 10 + i, i+1)
        sweets = self.manager.view_sweets()
        self.assertEqual(len(sweets), 100)
        self.assertEqual(sweets[0]["name"], "Sweet0")
        self.assertEqual(sweets[-1]["name"], "Sweet99")



    
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

    def test_search_combined_filters(self):
        self.manager.add_sweet(1200, "Rasmalai", "Milk-Based", 50, 10)
        results = self.manager.search_sweets(name="ras", category="Milk-Based", min_price=40, max_price=60)
        self.assertEqual(len(results), 1)

    def test_search_no_results(self):
        self.manager.add_sweet(1201, "Sandesh", "Milk-Based", 50, 10)
        results = self.manager.search_sweets(name="xyz")
        self.assertEqual(results, [])

    def test_search_name_case_insensitive(self):
        self.manager.add_sweet(1300, "Chikki", "Crunchy", 25, 5)
        results = self.manager.search_sweets(name="CHIKKI")
        self.assertEqual(len(results), 1)

    def test_search_price_at_boundary(self):
        self.manager.add_sweet(1301, "Jalebi", "Sweet", 30, 5)
        results = self.manager.search_sweets(min_price=30, max_price=30)
        self.assertEqual(len(results), 1)

    def test_search_invalid_price_range(self):
        self.manager.add_sweet(1302, "Imarti", "Sweet", 45, 5)
        with self.assertRaises(ValueError):
            self.manager.search_sweets(min_price=60, max_price=30)


    def test_search_partial_match_fails_due_to_price(self):
        self.manager.add_sweet(1303, "Barfi", "Milk-Based", 90, 5)
        results = self.manager.search_sweets(name="bar", category="Milk-Based", min_price=10, max_price=50)
        self.assertEqual(results, []) 







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
