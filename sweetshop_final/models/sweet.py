class Sweet:
    def __init__(self, sweet_id, name, category, price, quantity):
        self.id = sweet_id
        self.name = name
        self.category = category
        self.price = price
        self.quantity = quantity

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "category": self.category,
            "price": self.price,
            "quantity": self.quantity
        }