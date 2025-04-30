def annualPercentageRate(Interest_charges, Fees, Loan_amount, Days_in_term) :
    apr = (((Interest_charges + Fees) / Loan_amount) / Days_in_term) * 100
    return apr

def compoundAmount(Principal, Rate, Number_compounds, Time) :
   accured_amount = Principal * (1 + (Rate/100) / Number_compounds) ** (Number_compounds * Time)
   return accured_amount 