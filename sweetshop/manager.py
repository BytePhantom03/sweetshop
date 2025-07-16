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


