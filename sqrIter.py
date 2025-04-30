# Vikranth Pydeti                                         02-14-2025
# Lab 4  - This code contains the random number that is created from the random function. 
#https://www.cuemath.com/algebra/square-root-of-2/

def sqrtIter(x, iterations):
    y = (x + 1) / 2

    for _ in range (iterations):
        y = (x / y + y) / 2
        return y
    
def main():
    x = int(input("Please enter the number for which the square root is to be found: "))
    iterations = int(input("Please enter the value of the number of iterations: "))

    answer = sqrtIter(x, iterations)
    print("The answer is :", answer)

if __name__ == "__main__":
    main()