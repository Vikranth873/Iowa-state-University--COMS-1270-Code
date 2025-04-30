# Vikranth Pydeti                                 02-26-2025
#Lab 6 - This code give the multiplicatoin of all the numbers between two integers, taken from the user input.

def multiplicationTable (lowNum, highNum):
    for i in range (lowNum, highNum+1):
        for j in range (lowNum, highNum+1):
            print (i * j, end = "\t")
        print("")

def main():
    lowNum = int(input("Please enter the an integer (Must be lower than the next integer): "))
    highNum = int(input("Please enter an integer (Must be higher than the previous integer): "))
    multiplicationTable(lowNum, highNum)

if __name__ == "__main__":
    main()