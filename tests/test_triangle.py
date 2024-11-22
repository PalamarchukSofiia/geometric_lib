import pytest
from triangle import area as triangle_area, perimeter as triangle_perimeter

def validate_input(func):
    def wrapper(*args, **kwargs):
        if any(isinstance(arg, (str, list)) for arg in args):
            raise TypeError("Аргументы должны быть числами")
        if any(arg <= 0 for arg in args if isinstance(arg, (int, float))):
            raise ValueError("Аргументы должны быть положительными")
        return func(*args, **kwargs)
    return wrapper

triangle_area = validate_input(triangle_area)
triangle_perimeter = validate_input(triangle_perimeter)


def test_area_small():
    assert triangle_area(11, 10) == 55

def test_area_large():
    assert triangle_area(1e10, 1e10) == 5e19

def test_perimeter_small():
    assert triangle_perimeter(11, 10, 9) == 30

def test_perimeter_large():
    assert triangle_perimeter(1e10, 1e10, 1e10) == 3e10


def test_area_invalid_input():
    with pytest.raises(TypeError):
        triangle_area("11", 10)

def test_area_negative_input():
    with pytest.raises(ValueError):
        triangle_area(-1, 10)

def test_perimeter_invalid_input():
    with pytest.raises(TypeError):
        triangle_perimeter("11", 10, 9)

def test_perimeter_negative_input():
    with pytest.raises(ValueError):
        triangle_perimeter(11, -10, 9)
