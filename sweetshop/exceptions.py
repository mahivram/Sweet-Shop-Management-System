class SweetShopError(Exception):
    pass

class SweetAlreadyExistsError(SweetShopError):
    pass

class SweetNotFoundError(SweetShopError):
    pass

class InsufficientStockError(SweetShopError):
    pass
