class SweetValidator:
    @staticmethod
    def validate_id(sweet_id):
        if sweet_id is None or not str(sweet_id).strip():
            raise ValueError("Sweet ID must be a non-empty string or number.")
        if isinstance(sweet_id, int) and sweet_id < 0:
            raise ValueError("Sweet ID cannot be a negative number.")

    @staticmethod
    def validate_name(name):
        if not name or not str(name).strip():
            raise ValueError("Name must not be empty.")

    @staticmethod
    def validate_category(category):
        if not category or not str(category).strip():
            raise ValueError("Category must not be empty.")

    @staticmethod
    def validate_price(price):
        try:
            price = float(price)
            if price < 0:
                raise ValueError("Price cannot be negative.")
            return price
        except (TypeError, ValueError):
            raise ValueError("Invalid price.")

    @staticmethod
    def validate_quantity(quantity):
        try:
            quantity = int(quantity)
            if quantity <= 0:
                raise ValueError("Quantity must be more than 0.")
            return quantity
        except (TypeError, ValueError):
            raise ValueError("Invalid quantity.")