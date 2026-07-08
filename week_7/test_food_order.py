from food_order import calculate_total

def test_order1():
    assert calculate_total(10, 2) == 20

def test_total_equal_30():
    assert calculate_total(10, 3) == 30

def test_invalid_price():
    assert calculate_total(0, 2) == "invalid price"

def test_invalid_quantity():
    assert calculate_total(10, 0) == "invalid quantity"
    