# Vikranth Pydeti                                                          02-21-2025
# Assignment 2 -  Lucky Calculator assignment        
# This code helps to peform basic math calculations with 7 different operatons and Generate a lucky number. 

import random 
print ("")
print ("Lucky Calculator ! ")
print("")
print ("Created by : Vikranth Pydeti ")
print ("[COM S 1270 1] ")
print ("")
choice = input("\n What would you like to do from the following options?\n [c]calculator, [l]lucky number, [q]quit: ")

if choice == "c":
    operator = input("Please choose a Calculation: [+], [-], [*], [/], [//], [%], [**] : ")
    if operator not in  ["+", "-", "*", "/", "//", "%", "**"]:
        print ('''ERROR: You must enter either "+", "-", "*", "/", "//", "%" or "**", Please restart and choose one of the above options.''')
        exit()

    num1 = int(input("Please enter the value of Integer : "))
    num2 = int(input("Please enter the value of Integer : "))

    if operator in ["/", "//", "%"] and num2 == 0:
        print ("Error!! This number can not be divided by 0, Please change the denomenator and make sure it is not 0.") 
        num2 = 1    

    if operator == "+" :
        result = num1 + num2 
    elif operator == "-" :
        result = num1 - num2 
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        result = num1 / num2
    elif operator == "//":
        result = num1 // num2
    elif operator == "%":
        result = num1 % num2
    elif operator == "**":
        result = num1 ** num2

    else: 
        print("Operator not avaiable! Please choose from the operators that are provided")
        exit()
            
    print(f"The result of the numbers calculated was: {result} !")

elif choice == "l":
    lower = int(input("Please enter an Integer (lower): "))
    upper = int(input("Please enter an Integer (upper): "))
    lucky_number = random.randint(lower, upper)

    print(f"Your Lucky Number is: {lucky_number}!  (Hope it is correct!)" )

elif choice == "q":
    print("We are lucky that you used the Lucky Calculator, Thankyou!, GoodBye!")
    exit()

else: 
    print("The choice is not available.. Please restart and choose from [c], [l], [q]. Thank you")

print("\n We are lucky that you used the Lucky Calculator, Thankyou!, GoodBye! ")