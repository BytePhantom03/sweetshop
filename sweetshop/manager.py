class SweetManager:
    def __init__(self):
        self.sweets = {}

    def add_sweet(self, sweet_id, name, category, price, quantity):
        sweet = {
            "id": sweet_id,
            "name": name,
            "category": category,
            "price": price,
            "quantity": quantity
        }
        self.sweets[sweet_id] = sweet
        return sweet
