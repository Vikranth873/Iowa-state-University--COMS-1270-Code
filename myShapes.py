import math

def areaOfRectangle(Length, Breadth) :
    area = Length * Breadth
    return area

def rectanglePerimeter (Length, Breadth) :
    Perimeter = 2 * (Length + Breadth)
    return Perimeter 

def areaOfCircle(Radius) :
    area = math.pi * (Radius ** 2)
    return area 

def circleCircumference(Radius) :
    Circumference = 2 * math.pi * Radius
    return Circumference 