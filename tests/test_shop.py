import pytest
from sweetshop.models import Sweet
from sweetshop.shop import SweetShop
from sweetshop.exceptions import SweetAlreadyExistsError, SweetNotFoundError, InsufficientStockError

@pytest.fixture
def shop():
    return SweetShop()

def test_add_sweet(shop):
    sweet = Sweet(1001, "Kaju Katli", "Nut-Based", 50, 20)
    shop.add_sweet(sweet)
    assert shop.sweets[1001].name == "Kaju Katli"

def test_add_duplicate_sweet(shop):
    sweet = Sweet(1001, "Kaju Katli", "Nut-Based", 50, 20)
    shop.add_sweet(sweet)
    with pytest.raises(SweetAlreadyExistsError):
        shop.add_sweet(sweet)

def test_delete_sweet(shop):
    sweet = Sweet(1001, "Kaju Katli", "Nut-Based", 50, 20)
    shop.add_sweet(sweet)
    shop.delete_sweet(1001)
    assert 1001 not in shop.sweets

def test_delete_nonexistent_sweet(shop):
    with pytest.raises(SweetNotFoundError):
        shop.delete_sweet(9999)

def test_view_sweets(shop):
    sweet1 = Sweet(1001, "Kaju Katli", "Nut-Based", 50, 20)
    sweet2 = Sweet(1002, "Gajar Halwa", "Vegetable-Based", 30, 15)
    shop.add_sweet(sweet1)
    shop.add_sweet(sweet2)
    sweets = shop.view_sweets()
    assert len(sweets) == 2

def test_search_by_name(shop):
    sweet = Sweet(1001, "Kaju Katli", "Nut-Based", 50, 20)
    shop.add_sweet(sweet)
    results = shop.search_sweets(name="kaju")
    assert len(results) == 1
    assert results[0]["name"] == "Kaju Katli"

def test_search_by_category(shop):
    sweet = Sweet(1001, "Kaju Katli", "Nut-Based", 50, 20)
    shop.add_sweet(sweet)
    results = shop.search_sweets(category="Nut-Based")
    assert len(results) == 1

def test_search_by_price_range(shop):
    sweet1 = Sweet(1001, "Kaju Katli", "Nut-Based", 50, 20)
    sweet2 = Sweet(1002, "Gajar Halwa", "Vegetable-Based", 30, 15)
    shop.add_sweet(sweet1)
    shop.add_sweet(sweet2)
    results = shop.search_sweets(price_min=40, price_max=60)
    assert len(results) == 1
    assert results[0]["name"] == "Kaju Katli"

def test_sort_sweets_by_name(shop):
    sweet1 = Sweet(1001, "Gulab Jamun", "Milk-Based", 10, 50)
    sweet2 = Sweet(1002, "Kaju Katli", "Nut-Based", 50, 20)
    shop.add_sweet(sweet1)
    shop.add_sweet(sweet2)
    sorted_sweets = shop.sort_sweets(by="name")
    assert sorted_sweets[0]["name"] == "Gulab Jamun"

def test_sort_sweets_by_price_desc(shop):
    sweet1 = Sweet(1001, "Gulab Jamun", "Milk-Based", 10, 50)
    sweet2 = Sweet(1002, "Kaju Katli", "Nut-Based", 50, 20)
    shop.add_sweet(sweet1)
    shop.add_sweet(sweet2)
    sorted_sweets = shop.sort_sweets(by="price", reverse=True)
    assert sorted_sweets[0]["price"] == 50

def test_purchase_sweet(shop):
    sweet = Sweet(1001, "Kaju Katli", "Nut-Based", 50, 20)
    shop.add_sweet(sweet)
    shop.purchase_sweet(1001, 5)
    assert shop.sweets[1001].quantity == 15

def test_purchase_sweet_insufficient_stock(shop):
    sweet = Sweet(1001, "Kaju Katli", "Nut-Based", 50, 2)
    shop.add_sweet(sweet)
    with pytest.raises(InsufficientStockError):
        shop.purchase_sweet(1001, 5)

def test_purchase_nonexistent_sweet(shop):
    with pytest.raises(SweetNotFoundError):
        shop.purchase_sweet(9999, 1)

def test_restock_sweet(shop):
    sweet = Sweet(1001, "Kaju Katli", "Nut-Based", 50, 2)
    shop.add_sweet(sweet)
    shop.restock_sweet(1001, 10)
    assert shop.sweets[1001].quantity == 12

def test_restock_nonexistent_sweet(shop):
    with pytest.raises(SweetNotFoundError):
        shop.restock_sweet(9999, 10)
