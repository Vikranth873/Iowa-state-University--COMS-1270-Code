# Vikranth Pydeti                                         02-12-2025
# Lab 4  - This code contains the conversion of the previous code.

def rectanglePerimeter (Length, Breadth) :
    Perimeter = 2 * (Length + Breadth)
    return Perimeter 


def main () :
    Length = float(input("Please enter the value of length: "))
    Breadth = float(input("Please enter the value of breadth: "))
    Perimeter = rectanglePerimeter (Length, Breadth)
    print(Perimeter)

if __name__ == "__main__":
    main()