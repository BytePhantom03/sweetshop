from sweetshop.models import Sweet

class SweetManager:
    def __init__(self):
        self.sweets = {}

    def add_sweet(self, sweet_id, name, category, price, quantity):
        try:
            price = float(price)
            quantity = int(quantity)
        except (TypeError, ValueError):
            raise ValueError("Price must be a number and quantity must be an integer.")
        
        if sweet_id in self.sweets:
            raise ValueError(f"Sweet with ID {sweet_id} already exists.")
        if sweet_id is None or not str(sweet_id).strip():
            raise ValueError("Sweet ID must be a non-empty string or number.")
        # Reject Nagative Sweet Id
        if isinstance(sweet_id, int) and sweet_id < 0:
            raise ValueError("Sweet ID cannot be a negative number.")
        if not name.strip() or not category.strip():
            raise ValueError("Name and category must not be empty.")
        if price < 0:
            raise ValueError("Price cannot be negative.")
        if quantity <= 0:
            raise ValueError("Quantity Must More Than 0.")
        sweet = Sweet(sweet_id, name, category, price, quantity)
        self.sweets[sweet_id] = sweet
        return sweet.to_dict()
    
    def delete_sweet(self, sweet_id):
        if sweet_id is None or not str(sweet_id).strip():
            raise ValueError("Sweet ID must be a non-empty string or number.")
        if sweet_id in self.sweets:
            del self.sweets[sweet_id]
            return True
        return False
    
    def view_sweets(self):
        return [s.to_dict() for s in self.sweets.values()]
    

    def search_sweets(self, name=None, category=None, min_price=None, max_price=None):
         # Normalize and strip inputs
        if isinstance(name, str):
            name = name.strip().lower()
        if isinstance(category, str):
            category = category.strip().lower()

        try:
            if min_price is not None: min_price = float(min_price)
            if max_price is not None: max_price = float(max_price)
        except ValueError:
            raise ValueError("Price filters must be numbers.")


        if min_price is not None and max_price is not None:
            if min_price > max_price:
                raise ValueError("Minimum price cannot be greater than maximum price.")
            
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
    

    def purchase_sweet(self, sweet_id, quantity):

        if not isinstance(quantity, int) or quantity <= 0:
            raise ValueError("Purchase quantity must be a positive integer.")

        if sweet_id not in self.sweets:
            raise ValueError("Sweet not found.")

        sweet = self.sweets[sweet_id]
        if sweet.quantity < quantity:
            raise ValueError("Not enough stock available.")

        sweet.quantity -= quantity
        return True
    

    def restock_sweet(self, sweet_id, quantity):
        if not isinstance(quantity, int) or quantity <= 0:
            raise ValueError("Restock quantity must be a positive integer.")
        if sweet_id not in self.sweets:
            raise ValueError("Sweet not found.")
        if quantity <= 0:
            raise ValueError("Restock quantity must be positive.")

        self.sweets[sweet_id].quantity += quantity
        return True
    

    def update_sweet(self, sweet_id, name=None, category=None, price=None, quantity=None):

        if sweet_id not in self.sweets:
            raise ValueError("Sweet not found.")

        sweet = self.sweets[sweet_id]
        if name is not None:
            if not str(name).strip():
                raise ValueError("Name must not be empty.")
            sweet.name = name

        if category is not None:
            if not str(category).strip():
                raise ValueError("Category must not be empty.")
            sweet.category = category

        if price is not None:
            try:
                price = float(price)
                if price < 0:
                    raise ValueError("Price cannot be negative.")
                sweet.price = price
            except ValueError:
                raise ValueError("Invalid price.")

        if quantity is not None:
            try:
                quantity = int(quantity)
                if quantity <= 0:
                    raise ValueError("Quantity must be positive.")
                sweet.quantity = quantity
            except ValueError:
                raise ValueError("Invalid quantity.")

        if sweet_id not in self.sweets:
            raise ValueError("Sweet not found.")

        if name: sweet.name = name
        if category: sweet.category = category
        if price is not None: sweet.price = price
        if quantity is not None: sweet.quantity = quantity

        return sweet.to_dict()






