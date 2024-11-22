import pytest
from square import area as square_area, perimeter as square_perimeter

def validate_input(func):
    def wrapper(*args, **kwargs):
        if any(isinstance(arg, (str, list)) for arg in args):
            raise TypeError("Аргументы должны быть числами")
        if any(arg <= 0 for arg in args if isinstance(arg, (int, float))):
            raise ValueError("Аргументы должны быть положительными")
        return func(*args, **kwargs)
    return wrapper

square_area = validate_input(square_area)
square_perimeter = validate_input(square_perimeter)


def test_area_small():
    assert square_area(11) == 121

def test_area_large():
    assert square_area(1e10) == 1e20

def test_perimeter_small():
    assert square_perimeter(11) == 44

def test_perimeter_large():
    assert square_perimeter(1e10) == 4e10


def test_area_invalid_input():
    with pytest.raises(TypeError):
        square_area("11")

def test_area_negative_input():
    with pytest.raises(ValueError):
        square_area(-1)

def test_perimeter_invalid_input():
    with pytest.raises(TypeError):
        square_perimeter("11")

def test_perimeter_negative_input():
    with pytest.raises(ValueError):
        square_perimeter(-1)
