import math


def area(r):
    ''' Принимает число r (int) - радиус круга, и возвращает его площадь'''
    if r <= 0:
        raise ValueError("The radius of the circle must be a positive number")
    return math.pi * r * r


def perimeter(r):
    ''' Принимает число r (int) - радиус круга, и возвращает длину окружности'''
    if r <= 0:
        raise ValueError("The radius of the circle must be a positive number")
    return 2 * math.pi * r
