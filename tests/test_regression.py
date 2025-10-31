import pytest
from app import divide


def test_divide_by_zero_regression():
    # ensures the old bug (crash on zero division) doesn't come back
    with pytest.raises(ValueError):
        divide(10, 0)
