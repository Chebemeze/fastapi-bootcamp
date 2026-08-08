import pytest
from calculator import add, divide

@pytest.mark.parametrize("a, b, result", [
    (4, 5, 9),
    (20, 39, 59),
    (0, 0, 0),
    (5, 6, 11),
])
def test_add(a,b, result):
    assert add(a, b) == result

@pytest.mark.parametrize("a, b, result", [
    (4, 2, 2),
    (20, 39, 20/39),
    (0, 10, 0),
    (5, 6, 5/6),
])
def test_divide_normal_cases(a, b, result):
    assert divide(a, b) == result

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(8, 0) 
