# Vikranth Pydeti                                                                          02-19-2025
# This code is the code converstion of the all the previpous codes combined to.

import myShapes
import myPhysics
import myOhmsLaw
import myFinances

def main():
    running = True
    while running:
        print("Please choose one of the follwoing calculations to perform:")
        print("1. Area of Rectangle")
        print("2. Perimeter of Rectangle")
        print("3. Area of Circle")
        print("4. Circle circumference")
        print("5. Distance through speed and time")
        print("6. Velocity through acceleration and time")
        print("7. Calculate voltage")
        print("8. Calculate Resistence")
        print("9. Calculate current")
        print("10. Annual Percentage Rate ")
        print("11. Compound Amount")
        print("12. Quit")
        
        choice = input("Please enter the number from 1 - 12 depending on the required calculation: ")
        
        if choice == "1":
            Length = float(input("Please enter the value of length: "))
            Breadth = float(input("Please enter the value of breadth: "))
            area = myShapes.areaOfRectangle(Length, Breadth)
            print(area)
            
        elif choice == "2":
            Length = float(input("Please enter the value of length: "))
            Breadth = float(input("Please enter the value of breadth: "))
            Perimeter = myShapes.rectanglePerimeter(Length, Breadth)
            print(Perimeter)
            
        elif choice == "3":
            Radius = float(input("Please enter the value of radius: "))
            area = myShapes.areaOfCircle (Radius)
            print(area)
        
        elif choice == "4":
            Radius = float(input("Please enter the value of radius: "))
            Circumference = myShapes.circleCircumference (Radius)
            print(Circumference)
            
        elif choice == "5":
            Speed = float(input("Please enter the value of Speed in meters per second: "))
            Time = float(input("Please enter the value of Time in seconds: "))
            Distance = myPhysics.distancespeedtime2 (Speed, Time)
            print(Distance)
            
        elif choice == "6":
            Initial_velocity = float(input("Please enter the value of Initial Velocity in meters per seconds: "))
            Accelaration = float(input("Please enter the value of Accelaration in meter per second squared:"))
            Time = float (input("Please enter the value of Time in seconds: "))
            Final_velocity = myPhysics.velocityAccelerationTime (Initial_velocity, Accelaration, Time)
            print(Final_velocity)
            
        elif choice == "7":
            Current = float(input("Please enter the value of Current: "))
            Resistance = float(input("Please enter the value of Resistance: "))
            Voltage = myOhmsLaw.calculateVoltage (Current, Resistance)
            print(Voltage)
            
        elif choice == "8":
            Voltage = float(input("Please enter the value of Voltage: "))
            Current = float(input("Please enter the value of Current: "))
            Resistance = myOhmsLaw.calculateResistance (Voltage, Current)
            print(Resistance)
            
        elif choice == "9":
            Voltage = float(input("Please enter the value of Voltage: "))
            Resistance = float(input("Please enter the value of Resistance: "))
            Current = myOhmsLaw.calculateCurrent (Voltage, Resistance)
            print(Current)
            
        elif choice == "10":
            Interest_charges = float(input("Please enter the value of Interest rate: "))
            Fees = float(input("Please enter the value of Fees: "))
            Loan_amount = float(input("Please enter the value of Loan amount: "))
            Days_in_term = float(input("Please enter the Number of days in the loan term: "))
            apr = myFinances.annualPercentageRate (Interest_charges, Fees, Loan_amount, Days_in_term)
            print(apr)
            
        elif choice == "11":
            Principal = float(input("Please enter the value of your Principal amount: "))
            Rate = float(input("Please enter the value of iterest rate in the form percentage (WITHOUT % SYMBOL): "))
            Number_compounds = float(input("Please enter the value of number of times is the amount compounded per year: "))
            Time = float(input("Please enter the value of time in tearms of years: "))
            
            accured_amount =myFinances.compoundAmount (Principal, Rate, Number_compounds, Time)
            print(accured_amount)
            
        elif choice == "12":
            print("Thank you for choosing this program. bye, bye!!")
            running = False
            
        else:
            print("Choice not available! Please try again and enter number 1 - 12.")

if __name__ == "__main__":
    main()