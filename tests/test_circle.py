import pytest
import math
from circle import area as circle_area, perimeter as circle_perimeter

def validate_input(func):
    def wrapper(*args, **kwargs):
        if any(isinstance(arg, (str, list)) for arg in args):
            raise TypeError("Аргументы должны быть числами")
        if any(arg <= 0 for arg in args if isinstance(arg, (int, float))):
            raise ValueError("Аргументы должны быть положительными")
        return func(*args, **kwargs)
    return wrapper

circle_area = validate_input(circle_area)
circle_perimeter = validate_input(circle_perimeter)


def test_area_radius():
    assert math.isclose(circle_area(11), 380.13, abs_tol=0.01)

def test_area_large_radius():
    assert math.isclose(circle_area(1e10), 3.141592653589793e20, abs_tol=1e15)

def test_perimeter_radius():
    assert math.isclose(circle_perimeter(11), 69.11503837897544, abs_tol=0.01)

def test_perimeter_large_radius():
    assert math.isclose(circle_perimeter(1e10), 6.283185307179586e10, abs_tol=1e15)


def test_area_invalid_input():
    with pytest.raises(TypeError):
        circle_area("11")

def test_area_negative_input():
    with pytest.raises(ValueError):
        circle_area(-1)

def test_perimeter_invalid_input():
    with pytest.raises(TypeError):
        circle_perimeter("11")

def test_perimeter_negative_input():
    with pytest.raises(ValueError):
        circle_perimeter(-1)
