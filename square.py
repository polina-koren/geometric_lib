def area(a):
    ''' Принимает число a (int) - сторону квадрата, и возвращает его площадь'''
    if a <= 0:
        raise ValueError("The side of the square must be a positive number")
    return a * a


def perimeter(a):
    ''' Принимает число a (int) - сторону квадрата, и возвращает его периметр'''
    if a <= 0:
        raise ValueError("The side of the square must be a positive number")
    return 4 * a
