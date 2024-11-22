import pytest
import math
from circle import area, perimeter

def test_area_with_positive_integer():
  input_value = 7
  expected_result = math.pi * input_value**2
  result = area(input_value)
  assert math.isclose(result, expected_result, rel_tol=1e-9), f"Expected {expected_result}, got {result}"

def test_area_with_float():
  input_value = 3.14
  expected_result = math.pi * input_value**2
  result = area(input_value)
  assert math.isclose(result, expected_result, rel_tol=1e-9), f"Expected {expected_result}, got {result}"

def test_perimeter_with_positive_integer():
  input_value = 11
  expected_result = 2 * math.pi * input_value
  result = perimeter(input_value)
  assert math.isclose(result, expected_result, rel_tol=1e-9), f"Expected {expected_result}, got {result}"

def test_perimeter_with_float():
  input_value = 6.28
  expected_result = 2 * math.pi * input_value
  result = perimeter(input_value)
  assert math.isclose(result, expected_result, rel_tol=1e-9), f"Expected {expected_result}, got {result}"


def test_perimeter_with_invalid_string():
  input_value = "world"
  with pytest.raises(ValueError, match="Input must be a number"):
    perimeter(input_value)
