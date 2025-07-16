from sweetshop.models import Sweet

class SweetManager:
    def __init__(self):
        self.sweets = {}

    def add_sweet(self, sweet_id, name, category, price, quantity):
        if sweet_id in self.sweets:
            raise ValueError(f"Sweet with ID {sweet_id} already exists.")
        sweet = Sweet(sweet_id, name, category, price, quantity)
        self.sweets[sweet_id] = sweet
        return sweet.to_dict()
    
    def delete_sweet(self, sweet_id):
        if sweet_id in self.sweets:
            del self.sweets[sweet_id]
            return True
        return False
    
    def view_sweets(self):
        return [s.to_dict() for s in self.sweets.values()]
    

    def search_sweets(self, name=None, category=None, min_price=None, max_price=None):
        results = []
        for sweet in self.sweets.values():
            if name and name.lower() not in sweet.name.lower():
                continue
            if category and sweet.category != category:
                continue
            if min_price is not None and sweet.price < min_price:
                continue
            if max_price is not None and sweet.price > max_price:
                continue
            results.append(sweet.to_dict())
        return results
    

    def purchase_sweet(self, sweet_id, quantity):
        if sweet_id not in self.sweets:
            raise ValueError("Sweet not found.")

        sweet = self.sweets[sweet_id]
        if sweet.quantity < quantity:
            raise ValueError("Not enough stock available.")

        sweet.quantity -= quantity
        return True




