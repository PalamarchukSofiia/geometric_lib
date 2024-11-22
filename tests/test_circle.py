import unittest

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

class TestCircle(unittest.TestCase):

    def test_area_radius(self):
        self.assertAlmostEqual(circle_area(11), 380.13, places = 2)

    def test_area_large_radius(self):
        self.assertAlmostEqual(circle_area(1e10), 3.141592653589793e20, delta = 1e15)

    def test_perimeter_radius(self):
        self.assertEqual(circle_perimeter(11), 69.11503837897544)

    def test_perimeter_large_radius(self):
        self.assertAlmostEqual(circle_perimeter(1e10), 6.283185307179586e10)

if __name__ == '__main__':
    unittest.main()
