# Vikranth Pydeti                                         02-12-2025
# Lab 4  - This code contains the conersion of the previous code.

def calculateVoltage(Current, Resistance) :
    Voltage = Current * Resistance
    return Voltage 


def main () :
    Current = float(input("Please enter the value of Current: "))
    Resistance = float(input("Please enter the value of Resistance: "))
    Voltage = calculateVoltage (Current, Resistance)
    print(Voltage)

if __name__ == "__main__":
    main()