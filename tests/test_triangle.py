import unittest

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

class TestTriangle(unittest.TestCase):

    def test_area_small(self):
        self.assertEqual(triangle_area(11, 10), 55)

    def test_area_large(self):
        self.assertAlmostEqual(triangle_area(1e10, 1e10), 2e10)

    def test_perimeter_small(self):
        self.assertEqual(triangle_perimeter(11, 10, 9), 30)

    def test_perimeter_large(self):
        self.assertAlmostEqual(triangle_perimeter(1e10, 1e10, 1e10), 4e10)

if __name__ == '__main__':
    unittest.main()
