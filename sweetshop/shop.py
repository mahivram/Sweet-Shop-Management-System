from .models import Sweet
from .exceptions import SweetAlreadyExistsError, SweetNotFoundError, InsufficientStockError

class SweetShop:
    def __init__(self):
        self.sweets = {}

    def add_sweet(self, sweet: Sweet):
        if sweet.id in self.sweets:
            raise SweetAlreadyExistsError(f"Sweet with ID {sweet.id} already exists.")
        self.sweets[sweet.id] = sweet

    def delete_sweet(self, sweet_id: int):
        if sweet_id not in self.sweets:
            raise SweetNotFoundError(f"Sweet with ID {sweet_id} not found.")
        del self.sweets[sweet_id]

    def view_sweets(self):
        return [sweet.to_dict() for sweet in self.sweets.values()]

    def search_sweets(self, name=None, category=None, price_min=None, price_max=None):
        results = list(self.sweets.values())
        if name:
            results = [s for s in results if name.lower() in s.name.lower()]
        if category:
            results = [s for s in results if category.lower() == s.category.lower()]
        if price_min is not None:
            results = [s for s in results if s.price >= price_min]
        if price_max is not None:
            results = [s for s in results if s.price <= price_max]
        return [s.to_dict() for s in results]

    def sort_sweets(self, by="name", reverse=False):
        valid_fields = {"name", "category", "price", "quantity"}
        if by not in valid_fields:
            raise ValueError(f"Cannot sort by {by}. Valid fields: {valid_fields}")
        return [s.to_dict() for s in sorted(self.sweets.values(), key=lambda s: getattr(s, by), reverse=reverse)]

    def purchase_sweet(self, sweet_id: int, quantity: int):
        if sweet_id not in self.sweets:
            raise SweetNotFoundError(f"Sweet with ID {sweet_id} not found.")
        sweet = self.sweets[sweet_id]
        if sweet.quantity < quantity:
            raise InsufficientStockError(f"Not enough stock for sweet ID {sweet_id}.")
        sweet.quantity -= quantity

    def restock_sweet(self, sweet_id: int, quantity: int):
        if sweet_id not in self.sweets:
            raise SweetNotFoundError(f"Sweet with ID {sweet_id} not found.")
        self.sweets[sweet_id].quantity += quantity
