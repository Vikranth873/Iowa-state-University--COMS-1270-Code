# Vikranth Pydeti                                         02-12-2025
# Lab 4  - This code contains the conersion of the previous code.

def velocityAccelerationTime (Initial_velocity, Accelaration, Time) :
    Final_velocity = Initial_velocity + (Accelaration * Time)
    return Final_velocity 


def main () :
    Initial_velocity = float(input("Please enter the value of Initial Velocity in meters per seconds: "))
    Accelaration = float(input("Please enter the value of Accelaration in meter per second squared:"))
    Time = float (input("Please enter the value of Time in seconds: "))
    Final_velocity = velocityAccelerationTime (Initial_velocity, Accelaration, Time)
    print(Final_velocity)

if __name__ == "__main__":
    main()