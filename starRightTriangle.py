# Vikranth Pydeti                                 02-26-2025
#Lab 6 - This code give a right triangle using stars.

def starRightTriangle (num):
    for i in range (1, num + 1):
        for j in range (i):
            print ("*", end = "")
        print()

def main():
    num = int(input("Please enter an integer (depends on the number of lines your triangle must be): "))
    starRightTriangle(num)

if __name__ == "__main__":
    main()