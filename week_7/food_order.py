def calculate_total(unit_price, quantity):
    if unit_price <= 0:
        return "invalid price"

    if quantity <= 0:
        return "invalid quantity"

    return unit_price * quantity