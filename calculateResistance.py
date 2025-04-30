# Vikranth Pydeti                                         02-12-2025
# Lab 4 - This code contains the conversion of the previous code.

def calculateResistance(Voltage, Current) :
    Resistance = Voltage / Current
    return Resistance 


def main () :
   Voltage = float(input("Please enter the value of Voltage: "))
   Current = float(input("Please enter the value of Current: "))
   Resistance = calculateResistance (Voltage, Current)
   print(Resistance)

if __name__ == "__main__":
    main()