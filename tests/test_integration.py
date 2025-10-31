from app import add, multiply


def test_add_and_multiply():
    # simulate a real workflow using multiple functions
    result = multiply(add(2, 3), 4)  # (2 + 3) * 4 = 20
    assert result == 20
