import pytest
from calculate import calc
from math import pi

def test_calc_area_circle():
  fig = "circle"
  func = "area"
  size = [5]
  expected_result = f"Area of circle (π * 5^2) = {pi * 5**2:.2f}"
  result = calc(fig, func, size)
  assert result == expected_result, f"Expected '{expected_result}', got '{result}'"

def test_calc_perimeter_circle():
  fig = "circle"
  func = "perimeter"
  size = [7]
  expected_result = f"Perimeter of circle (7) = {2 * pi * 7:.2f}"
  result = calc(fig, func, size)
  assert result == expected_result, f"Expected '{expected_result}', got '{result}'"

def test_calc_area_square():
  fig = "square"
  func = "area"
  size = [6]
  expected_result = f"Area of square (6 * 6) = {6 * 6}"
  result = calc(fig, func, size)
  assert result == expected_result, f"Expected '{expected_result}', got '{result}'"

def test_calc_perimeter_square():
  fig = "square"
  func = "perimeter"
  size = [8]
  expected_result = f"Perimeter of square (8) = {4 * 8}"
  result = calc(fig, func, size)
  assert result == expected_result, f"Expected '{expected_result}', got '{result}'"

def test_calc_area_triangle():
  fig = "triangle"
  func = "area"
  size = [6, 8, 10] # Pythagorean triple for easier calculation
  s = (6 + 8 + 10) / 2 # Semi-perimeter
  area = math.sqrt(s * (s - 6) * (s - 8) * (s - 10))
  expected_result = f"Area of triangle (Heron's formula for sides 6, 8, 10) = {area:.2f}"
  result = calc(fig, func, size)
  assert result == expected_result, f"Expected '{expected_result}', got '{result}'"


def test_calc_perimeter_triangle():
  fig = "triangle"
  func = "perimeter"
  size = [12, 15, 9]
  expected_result = f"Perimeter of triangle (12 + 15 + 9) = {12 + 15 + 9}"
  result = calc(fig, func, size)
  assert result == expected_result, f"Expected '{expected_result}', got '{result}'"

def test_calc_invalid_figure():
  fig = "octagon"
  func = "area"
  size = [3]
  with pytest.raises(ValueError, match=f"Figure {fig} is not supported. Available figures: .*"):
    calc(fig, func, size)

def test_calc_invalid_function():
  fig = "circle"
  func = "volume"
  size = [3]
  with pytest.raises(ValueError, match=f"Function {func} is not supported. Available functions: .*"):
    calc(fig, func, size)

def test_calc_invalid_size():
  fig = "circle"
  func = "area"
  size = [3, 4]
  with pytest.raises(ValueError, match="Invalid number of sizes for circle area: expected 1, got 2"):
    calc(fig, func, size)

