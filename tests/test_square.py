import pytest
from square import area, perimeter

def test_area_with_positive_integer():
  input_value = 7
  expected_result = 49
  result = area(input_value)
  assert result == expected_result, f"Expected {expected_result}, got {result}"

def test_area_with_float():
  input_value = 3.14
  expected_result = 3.14**2
  result = area(input_value)
  assert result == pytest.approx(expected_result), f"Expected {expected_result}, got {result}"

def test_perimeter_with_positive_integer():
  input_value = 11
  expected_result = 44
  result = perimeter(input_value)
  assert result == expected_result, f"Expected {expected_result}, got {result}"

def test_perimeter_with_float():
  input_value = 6.28
  expected_result = 4 * 6.28
  result = perimeter(input_value)
  assert result == pytest.approx(expected_result), f"Expected {expected_result}, got {result}"


def test_perimeter_with_invalid_string():
  input_value = "world"
  with pytest.raises(TypeError, match="Input must be a number"): # Исправлено на TypeError
    perimeter(input_value)
