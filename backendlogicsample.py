import pytest
from calculations import add
# assume there is a file called calculations that has an add function

def test_add():
    assert add(1, 2) == 3
    assert add(-1, 1) == 0
    assert add(-1, -1) == -2
