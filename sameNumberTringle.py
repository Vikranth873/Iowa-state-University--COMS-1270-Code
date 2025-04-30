# Vikranth Pydeti                                 03-01-2025
#Lab 6 - This code give a right triangle using number where each line has a same number.

def sameNumberTriangle(num):
    for i in range (1, num + 1):
        for j in range (i):
            print (i, end = " ")
        print()

def main():
    num = int(input("Please enter an integer (depends on the height of your triangle): "))
    sameNumberTriangle(num)

if __name__ == "__main__":
    main()