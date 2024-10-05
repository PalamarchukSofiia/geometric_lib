# General description of the solution
The calculator calculates the area and perimeter of the shapes: square and circle. To perform this task, it connects functions from the corresponding files. To calculate, the user needs to enter the type of geometric shape, what he wants to calculate (area/perimeter) and the size of the shape.
# How to use calculator:
1. Run `python calculate.py`
2. Enter the figure name. Available are Circle, Square.
3. Enter the function: Area or Perimeter.
4. Enter figure sizes. Radius for circle, one side for square.
5. Get the answer!
# Circle function

`import math
def area(r):
    return math.pi * r * r
def perimeter(r):
    return 2 * math.pi * r`
    
## Description of the function operation
The circle function is used to calculate the area and perimeter of a circle. Calculations are performed using the formulas described below. To apply the number pi, the math module is connected.
## Example of a call
For a circle with a radius of 5, the function outputs the following values: 
area: 78.53981633974483 
perimeter: 31.41592653589793
# Square function

`def area(a):
    return a * a
def perimeter(a):
    return 4 * a`

## Description of the function operation
The square function is used to calculate the area and perimeter of a square. Calculations are performed using the formulas described below.
## Example of a call
For a square with side 4, the function outputs the following values: 
area: 16
perimeter: 16
# Math formulas
## Area
- Circle: `S = πR²`
- Rectangle: `S = ab`
- Square: `S = a²`
- Triangle: `S = sqrt(p * (p-a) * (p-b) * (p-c))` where p is semiperimeter

## Perimeter
- Circle: `P = 2πR`
- Rectangle: `P = 2a + 2b`
- Square: `P = 4a`
- Triangle: `P = a + b + c`

