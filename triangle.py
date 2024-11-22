import math

def area(a, b, c):

  if not (a + b > c and a + c > b and b + c > a):
    raise ValueError("The provided sides do not form a valid triangle.")

  s = (a + b + c) / 2 # Полупериметр
  return math.sqrt(s * (s - a) * (s - b) * (s - c))


def perimeter(a, b, c):
  return a + b + c
