import pytest
import math
from triangle import area, perimeter

def test_area_with_valid_triangle():
  a, b, c = 5, 12, 13 # Pythagorean triple
  expected_result = 30.0
  result = area(a, b, c)
  assert math.isclose(result, expected_result, rel_tol=1e-9), f"Expected {expected_result}, got {result}"

def test_area_with_float_triangle():
  a, b, c = 7.5, 9.5, 11.5
  p = (a + b + c) / 2
  expected_result = math.sqrt(p * (p - a) * (p - b) * (p - c))
  result = area(a, b, c)
  assert math.isclose(result, expected_result, rel_tol=1e-9), f"Expected {expected_result}, got {result}"

def test_area_with_invalid_triangle():
  a, b, c = 1, 2, 6 # Не может существовать треугольник с такими сторонами
  with pytest.raises(ValueError, match="The provided sides do not form a valid triangle."):
    area(a, b, c)

def test_perimeter_with_valid_triangle():
  a, b, c = 5, 12, 13 # Pythagorean triple
  expected_result = 30
  result = perimeter(a, b, c)
  assert result == expected_result, f"Expected {expected_result}, got {result}"

def test_perimeter_with_floats():
  a, b, c = 3.5, 6.5, 8.5
  expected_result = a + b + c
  result = perimeter(a, b, c)
  assert math.isclose(result, expected_result, rel_tol=1e-9), f"Expected {expected_result}, got {result}"

