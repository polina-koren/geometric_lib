# About project
This project provides tools for calculating the area and perimeter of a circle, square and triangle. The user enters the name of the shape and function (area or perimeter) and sets the dimensions. After that, the program outputs the result of the calculations.

# How to use calculator:
1. Run `python calculate.py`
2. Enter the figure name. Available are Circle, Square.
3. Enter the function: Area or Perimeter.
4. Enter figure sizes. Radius for circle, one side for square.
5. Get the answer!

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

# Description of each function with call examples
## Calculate
- Function calc: 
1. Description:
    The function does not return a value, but displays a string indicating what was calculated for this shape (area or perimeter) and the result of the calculations itself.
2. Parameters:
    1. fig (str) - the name of the shap
    2. func (str) - the name of the function
    3. size (list) - the size
3. An example of a call:
    Calling the function `calc(circle, area, 5)`: area of circle is 78.53981633974483

## Circle
- Function area():
1. Desription and parameters:
    Takes the number r (int) - the radius of the circle, and returns its area.
2. An example of a call: `area(5)`
    When running this code, nothing will be displayed on the screen, since there are no commands for displaying the result.
    But it will return the value: 78,5398163

- Funcrion perimeter():
1. Desription and parameters:
    Takes the number r (int) - the radius of the circle, and returns the length of the circle.
2. An example of a call: `perimeter(5)`
    When running this code, nothing will be displayed on the screen, since there are no commands for displaying the result.
    But it will return the value: 31,4159265

## Square
- Function area():
1. Desription and parameters:
    Takes the number a (int) - the side of the square, and returns its area.
2. An example of a call: `area(6)`
    When running this code, nothing will be displayed on the screen, since there are no commands for displaying the result.
    But it will return the value: 36

- Funcrion perimeter():
1. Desription and parameters:
    Takes the number a (int) - the side of the square, and returns its perimeter.
2. An example of a call: `perimeter(6)`
    When running this code, nothing will be displayed on the screen, since there are no commands for displaying the result.
    But it will return the value: 24

## Triangle
- Function area():
1. Desription and parameters:
    Takes three numbers a, b, c (int) - the sides of a triangle, and returns its half-meter.
2. An example of a call: `area(4, 3, 2)`
    When running this code, nothing will be displayed on the screen, since there are no commands for displaying the result.
    But it will return the value: 4.5

- Funcrion perimeter():
1. Desription and parameters:
    Takes three numbers a, b, c (int) - the sides of a triangle, and returns its perimeter.
2. An example of a call: `perimeter(4, 3, 2)`
    When running this code, nothing will be displayed on the screen, since there are no commands for displaying the result.
    But it will return the value: 9

# 