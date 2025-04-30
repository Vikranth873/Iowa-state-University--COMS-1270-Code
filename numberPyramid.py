# Vikranth Pydeti                                 03-01-2025
#Lab 6 - This code give a pyramid of numbers depending on the user input. 

def numberPyramid(num):
    for i in range (1, num + 1):
        print (" " * (num - i), end = "")
        for j in range (1, i + 1):
            print (j, end = " ")
        print()

def main():
    num = int(input("Please enter an integer (depends on the number of lines your pyramid must be): "))
    numberPyramid(num)

if __name__ == "__main__":
    main()