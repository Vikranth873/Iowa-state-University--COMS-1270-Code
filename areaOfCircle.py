# Vikranth Pydeti                                         02-12-2025
# Lab 4  - This code contains the conversion of the previous code.  

import math

def areaOfCircle(Radius) :
    area = math.pi * (Radius ** 2)
    return area 


def main () :
    Radius = float(input("Please enter the value of radius: "))
    area = areaOfCircle (Radius)
    print(area)

if __name__ == "__main__":
    main()