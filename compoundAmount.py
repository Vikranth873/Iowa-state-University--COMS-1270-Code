# Vikranth Pydeti                                         02-13-2025
# Lab 4  - This code contains the conversion of the previous code. 

def compoundAmount(Principal, Rate, Number_compounds, Time) :
   accured_amount = Principal * (1 + (Rate/100) / Number_compounds) ** (Number_compounds * Time)
   return accured_amount 


def main () :
   Principal = float(input("Please enter the value of your Principal amount: "))
   Rate = float(input("Please enter the value of iterest rate in the form percentage (WITHOUT % SYMBOL): "))
   Number_compounds = float(input("Please enter the value of number of times is the amount compounded per year: "))
   Time = float(input("Please enter the value of time in tearms of years: "))

   accured_amount = compoundAmount (Principal, Rate, Number_compounds, Time)
   print(accured_amount)

if __name__ == "__main__":
    main()