import pytest
from calculate import calc
from math import pi

def test_calc_area_circle():
    fig = "circle"
    func = "area"
    size = [3]
    expected_result = f"Area of circle (π * 3^2) = {pi * 3**2:.2f}"
    result = calc(fig, func, size)
    assert result == expected_result, f"Expected '{expected_result}', got '{result}'"

def test_calc_perimeter_circle():
    fig = "circle"
    func = "perimeter"
    size = [3]
    expected_result = f"Perimeter of circle (3) = {2 * pi * 3:.2f}"
    result = calc(fig, func, size)
    assert result == expected_result, f"Expected '{expected_result}', got '{result}'"

def test_calc_area_square():
    fig = "square"
    func = "area"
    size = [4]
    expected_result = f"Area of square (4 * 4) = {4 * 4}"
    result = calc(fig, func, size)
    assert result == expected_result, f"Expected '{expected_result}', got '{result}'"

def test_calc_perimeter_square():
    fig = "square"
    func = "perimeter"
    size = [4]
    expected_result = f"Perimeter of square (4) = {4 * 4}"
    result = calc(fig, func, size)
    assert result == expected_result, f"Expected '{expected_result}', got '{result}'"

def test_calc_area_triangle():
    fig = "triangle"
    func = "area"
    size = [3, 4, 5]
    expected_result = f"Area of triangle (Heron's formula for sides 3, 4, 5) = 6.00"
    result = calc(fig, func, size)
    assert result == expected_result, f"Expected '{expected_result}', got '{result}'"

def test_calc_perimeter_triangle():
    fig = "triangle"
    func = "perimeter"
    size = [3, 4, 5]
    expected_result = f"Perimeter of triangle (3 + 4 + 5) = 12"
    result = calc(fig, func, size)
    assert result == expected_result, f"Expected '{expected_result}', got '{result}'"

def test_calc_invalid_figure():
    fig = "hexagon"
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
