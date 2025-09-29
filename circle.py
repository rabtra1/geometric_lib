import math


def area(radius:float) -> float:
    '''
    Принимает радиус круга, возвращает его площадь
    
    Имеет следующие параметры:
        -> radius:float - Радиус круга

    Возвращаемое значение:
        -> area:float - Площадь данного круга
    '''
    return math.pi * radius * radius


def perimeter(radius:float) -> float:
    '''
    Принимает радиус круга, возвращает его периметр
    
    Имеет следующие параметры:
        -> radius:float - Радиус круга

    Возвращаемое значение:
        -> perimeter:float - Периметр круга
    '''
    return 2 * math.pi * radius