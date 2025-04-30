# Vikranth Pydeti                                         02-12-2025
# Lab 4  - This code contains the conversion of the previous code.

import math

def circleCircumference(Radius) :
    Circumference = 2 * math.pi * Radius
    return Circumference 


def main () :
    Radius = float(input("Please enter the value of radius: "))
    Circumference = circleCircumference (Radius)
    print(Circumference)

if __name__ == "__main__":
    main()