import unittest

from rectangle import area as rect_area, perimeter as rect_perimeter

def validate_input(func):

    def wrapper(*args, **kwargs):
        if any(isinstance(arg, (str, list)) for arg in args):
            raise TypeError("Аргументы должны быть числами")
        
        if any(arg <= 0 for arg in args if isinstance(arg, (int, float))):
            raise ValueError("Аргументы должны быть положительными")
        
        return func(*args, **kwargs)
    
    return wrapper

rect_area = validate_input(rect_area)
rect_perimeter = validate_input(rect_perimeter)

class TestRectangle(unittest.TestCase):

    def test_area_small(self):
        self.assertEqual(rect_area(11, 10), 110)

    def test_area_large_values(self):
        self.assertAlmostEqual(rect_area(1e10, 1e10), 1e20)

    def test_perimeter_small(self):
        self.assertEqual(rect_perimeter(11, 6), 34)

    def test_perimeter_large_values(self):
        self.assertAlmostEqual(rect_perimeter(1e10, 1e10), 4e10)

if __name__ == '__main__':
    unittest.main()
