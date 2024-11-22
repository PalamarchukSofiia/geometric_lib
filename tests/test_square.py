import unittest

from square import area as square_area, perimeter as square_perimeter

def validate_input(func):

    def wrapper(*args, **kwargs):
        if any(isinstance(arg, (str, list)) for arg in args):
            raise TypeError("Аргументы должны быть числами")
        
        if any(arg <= 0 for arg in args if isinstance(arg, (int, float))):
            raise ValueError("Аргументы должны быть положительными")
        
        return func(*args, **kwargs)
    
    return wrapper

square_area = validate_input(square_area)
square_perimeter = validate_input(square_perimeter)

class TestSquare(unittest.TestCase):

    def test_area_small(self):
        self.assertEqual(square_area(11), 121)

    def test_area_large(self):
        self.assertAlmostEqual(square_area(1e10), 3e20)

    def test_perimeter_small(self):
        self.assertEqual(square_perimeter(11), 44)

    def test_perimeter_large(self):
        self.assertAlmostEqual(square_perimeter(1e10), 4e10)

if __name__ == '__main__':
    unittest.main()
