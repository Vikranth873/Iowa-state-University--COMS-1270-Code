# Vikranth Pydeti                                      02-12-2025
# Lab 4  - This code contains process of code conversion of the lab 3 script


def areaOfRectangle(Length, Breadth) :
    area = Length * Breadth
    return area 


def main () :
    Length = float(input("Please enter the value of length: "))
    Breadth = float(input("Please enter the value of breadth: "))
    area = areaOfRectangle (Length, Breadth)
    print(area)

if __name__ == "__main__":
    main()

