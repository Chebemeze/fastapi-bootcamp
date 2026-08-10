from yield_cart import ShoppingCart
import pytest

@pytest.fixture
def cart():
    new_cart = ShoppingCart()
    print("Setting up cart")
    #using yield will return something (in this case new_cart) and go back to the code underneath the yield
    yield new_cart
    print("Tearing down cart")

def test_add_item(cart):
    cart.add_item(5)
    assert  cart.items == [5]

def test_cart_starts_empty(cart):
    assert cart.items == []
