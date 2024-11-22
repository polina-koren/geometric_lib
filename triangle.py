def area(a, b, c):
    ''' Принимает три числа a, b, c (int) - стороны треугольника, и возвращает его полупериметр'''
    if a <= 0 or b <= 0 or c <= 0:
        raise ValueError("The sides of the triangle must be positive numbers")
    if a + b <= c or a + c <= b or b + c <= a:
        raise ValueError("The sum of any two sides of the triangle must be greater than the third side")
    return (a + b + c) / 2


def perimeter(a, b, c):
    ''' Принимает три числа a, b, c (int) - стороны треугольника, и возвращает его периметр'''
    if a <= 0 or b <= 0 or c <= 0:
        raise ValueError("The sides of the triangle must be positive numbers")
    if a + b <= c or a + c <= b or b + c <= a:
        raise ValueError("The sum of any two sides of the triangle must be greater than the third side")
    return a + b + c
