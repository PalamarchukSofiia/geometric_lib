import math

def area(a, b, c):
  """Вычисляет площадь треугольника по формуле Герона.

  Args:
    a: Длина стороны a.
    b: Длина стороны b.
    c: Длина стороны c.

  Returns:
    Площадь треугольника. Вызывает ValueError, если стороны некорректны.
  """
  if not all(isinstance(side, (int, float)) and side >= 0 for side in (a, b, c)):
    raise ValueError("Входные данные должны быть неотрицательными числами.")

  if not (a + b > c and a + c > b and b + c > a):
    raise ValueError("The provided sides do not form a valid triangle.")

  s = (a + b + c) / 2 # Полупериметр
  return math.sqrt(s * (s - a) * (s - b) * (s - c))


def perimeter(a, b, c):
  """Вычисляет периметр треугольника."""
  if not all(isinstance(side, (int, float)) and side >= 0 for side in (a, b, c)):
    raise ValueError("Входные данные должны быть неотрицательными числами.")
  return a + b + c
