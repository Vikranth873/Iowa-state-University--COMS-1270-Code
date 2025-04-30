# Vikranth Pydeti                                         02-12-2025
# Lab 4 - This code contains the conversion of the previous code.

def calculateCurrent(Voltage, Resistance) :
    Current = Voltage / Resistance
    return Current 


def main () :
   Voltage = float(input("Please enter the value of Voltage: "))
   Resistance = float(input("Please enter the value of Resistance: "))
   Current = calculateCurrent (Voltage, Resistance)
   print(Current)

if __name__ == "__main__":
    main()