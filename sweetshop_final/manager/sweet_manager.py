from sweetshop_final.models.sweet import Sweet
from sweetshop_final.validators.sweet_validator import SweetValidator

class SweetManager:
    def __init__(self):
        self.sweets = {}

    def add_sweet(self, sweet_id, name, category, price, quantity):
        SweetValidator.validate_id(sweet_id)
        SweetValidator.validate_name(name)
        SweetValidator.validate_category(category)
        price = SweetValidator.validate_price(price)
        quantity = SweetValidator.validate_quantity(quantity)

        if sweet_id in self.sweets:
            raise ValueError(f"Sweet with ID {sweet_id} already exists.")

        sweet = Sweet(sweet_id, name.strip(), category.strip(), price, quantity)
        self.sweets[sweet_id] = sweet
        return sweet.to_dict()

    def delete_sweet(self, sweet_id):
        SweetValidator.validate_id(sweet_id)
        if sweet_id not in self.sweets:
            raise ValueError("Sweet not found.")
        del self.sweets[sweet_id]
        return True

    def view_sweets(self):
        return [s.to_dict() for s in self.sweets.values()]

    def search_sweets(self, name=None, category=None, min_price=None, max_price=None):
        # 🔒 Validate empty string / whitespace-only search
        if not any([name, category, min_price, max_price]):
            raise ValueError("At least one search filter must be provided.")

        # Normalize string filters
        if isinstance(name, str):
            name = name.strip().lower()
            if not name:
                raise ValueError("Search name cannot be empty.")
        if isinstance(category, str):
            category = category.strip().lower()
            if not category:
                raise ValueError("Category cannot be empty.")

        # Validate price filters
        try:
            if min_price is not None: min_price = float(min_price)
            if max_price is not None: max_price = float(max_price)
        except ValueError:
            raise ValueError("Price filters must be valid numbers.")

        if min_price is not None and max_price is not None and min_price > max_price:
            raise ValueError("Minimum price cannot be greater than maximum price.")

        # Perform filtering
        results = []
        for sweet in self.sweets.values():
            if name and name.lower() not in sweet.name.lower():
                continue
            if category and sweet.category.lower() != category:
                continue
            if min_price is not None and sweet.price < min_price:
                continue
            if max_price is not None and sweet.price > max_price:
                continue
            results.append(sweet.to_dict())

        return results


    def get_sweet_by_id(self, sweet_id):
        SweetValidator.validate_id(sweet_id)
        if sweet_id not in self.sweets:
            raise ValueError("Sweet not found.")
        return self.sweets[sweet_id]

    def purchase_sweet(self, sweet_id, quantity):
        quantity = SweetValidator.validate_quantity(quantity)
        sweet = self.get_sweet_by_id(sweet_id)
        if sweet.quantity < quantity:
            raise ValueError("Not enough stock available.")
        sweet.quantity -= quantity
        return sweet.to_dict()

    def restock_sweet(self, sweet_id, quantity):
        quantity = SweetValidator.validate_quantity(quantity)
        sweet = self.get_sweet_by_id(sweet_id)
        sweet.quantity += quantity
        return sweet.to_dict()

    def update_sweet(self, sweet_id, name=None, category=None, price=None, quantity=None):
         
        sweet = self.get_sweet_by_id(sweet_id)

        if sweet_id not in self.sweets:
            raise ValueError("Sweet not found.")
        if name is None and category is None and price is None and quantity is None:
            raise ValueError("No update fields provided.")

        if name is not None:
            SweetValidator.validate_name(name)
            sweet.name = name.strip()

        if category is not None:
            SweetValidator.validate_category(category)
            sweet.category = category.strip()

        if price is not None:
            sweet.price = SweetValidator.validate_price(price)

        if quantity is not None:
            sweet.quantity = SweetValidator.validate_quantity(quantity)

        return sweet.to_dict()
