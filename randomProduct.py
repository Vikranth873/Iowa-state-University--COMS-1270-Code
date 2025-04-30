# Vikranth Pydeti                                         02-13-2025
# Lab 4  - This code contains the random number that is created from the random function. 

import random

def randomProduct(a, b, c) :
    product = 1 
    for _ in range (a):
        random_number = random.randrange (b, c + 1)
        product *= random_number
    return product


def main () :
   a = int(input("Please enter the number of random numbers: "))
   b = int(input("Please enter the lowest number: "))
   c = int(input("Please enter the highest number: "))
   answer = randomProduct (a, b, c)
   print(answer)

if __name__ == "__main__":
    main()

