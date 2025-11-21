import pytest
from armstrong import is_armstrong

def test_armstrong_valid_numbers():
    assert is_armstrong(153) is True
    assert is_armstrong(370) is True
    assert is_armstrong(371) is True
    assert is_armstrong(9474) is True

def test_armstrong_invalid_numbers():
    assert is_armstrong(10) is False
    assert is_armstrong(200) is False

def test_armstrong_edge_cases():
    with pytest.raises(TypeError):
        is_armstrong("153")

    with pytest.raises(ValueError):
        is_armstrong(-5)
