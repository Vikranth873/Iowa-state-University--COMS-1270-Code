# Vikranth Pydeti                                 03-01-2025
#Lab 6 - This code creates a diamond using number, no.of lines depends on the user input.

def numberDiamond(num):
    for i in range (1, num + 1):
        print (" " * (num - i), end = "")
        for j in range (1, i + 1):
            print (j, end = " ")
        print()

    for i in range (num - 1, 0, -1):
        print (" " * (num - i), end = "")
        for j in range (1, i + 1):
            print (j, end = " ")
        print()


def main():
    num = int(input("Please enter an integer (depends on the size of the diamond [Size - No.Of lines you want the diamond to be?]): "))
    numberDiamond(num)

if __name__ == "__main__":
    main()