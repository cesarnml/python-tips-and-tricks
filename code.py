# Chapter 2

shoes = {
    'name': 'Fancy Shoes',
    'price': 14900,
}

def apply_discount(product, discount):
    """Apply a discount to a product"""
    original_price = product['price']
    if discount:
        new_price = original_price * (1.0 - discount)
    else:
        new_price = original_price
    assert 0 <= new_price <= original_price
    return new_price

apply_discount(shoes, 2)