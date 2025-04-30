# Vikranth Pydeti                                         02-13-2025
# Lab 4  - This code contains the conersion of the previous code.


def annualPercentageRate(Interest_charges, Fees, Loan_amount, Days_in_term) :
    apr = (((Interest_charges + Fees) / Loan_amount) / Days_in_term) * 100
    return apr 


def main () :
   Interest_charges = float(input("Please enter the value of Interest rate: "))
   Fees = float(input("Please enter the value of Fees: "))
   Loan_amount = float(input("Please enter the value of Loan amount: "))
   Days_in_term = float(input("Please enter the Number of days in the loan term: "))
   apr = annualPercentageRate (Interest_charges, Fees, Loan_amount, Days_in_term)
   print(apr)

if __name__ == "__main__":
    main()