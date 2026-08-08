from kiosk import CoffeKiosk
import pytest

@pytest.fixture
def stocked_kiosk():
    return CoffeKiosk(100, 50)

def test_reduce_ingredients(stocked_kiosk):
    stocked_kiosk.brew_expresso()
    assert stocked_kiosk.beans == 82
    assert stocked_kiosk.water == 20


@pytest.fixture
def stocked():
    return CoffeKiosk(10, 50)
def test_value_error_case(stocked):
    with pytest.raises(ValueError):
        stocked.brew_expresso()