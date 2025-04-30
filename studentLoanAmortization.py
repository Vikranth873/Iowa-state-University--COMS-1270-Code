# Vikranth Pydeti                                          02-26-2025
#Lab 6 - This code takes up the role as the amortirization calculatorfor student loan.

def studentLoanAmortization(Principal, YearlyInterest, Time_year):
    monthly_Interest = (YearlyInterest/100 ) / 12
    time_months = Time_year * 12

    if monthly_Interest == 0:
        monthly_payment = Principal / time_months
    else: 
        monthly_payment = (Principal * monthly_Interest) / (1 - (1 + monthly_Interest) ** - time_months)

    print("\nPeriod     Total Payment Due     Compound Interest     Principal Due     Principal Balance")
    print("=" * 90)

    balance = Principal
    for period in range (1, time_months + 1):
        interest_due = balance * monthly_Interest 
        principal_due = monthly_payment - interest_due
        balance -= principal_due

        balance = max(balance, 0)

        print(f"{period:<10}{monthly_payment:>18.2f}{interest_due:>22.2f}{principal_due:>20.2f}{balance:>20.2f}")
        
def main():
    Principal = float(input("Please enter the amount you have taken as a loan:"))
    Interest = float(input("Please enter the Interest for the loan taken (in %): "))
    Time = int(input("Please enter the Number of years for the loan to be payed back by: "))
    
    studentLoanAmortization(Principal, Interest, Time)

if __name__ == "__main__":
    main()
             