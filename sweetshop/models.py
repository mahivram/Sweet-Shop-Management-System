# sweetshop/models.py

class Sweet:
    def __init__(self, sweet_id: int, name: str, category: str, price: float, quantity: int):
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
