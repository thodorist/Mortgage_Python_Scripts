from mortgage_module import FixedMortgageCalculator

my_mortgage = FixedMortgageCalculator(loan_amount = 100000, 
										yearly_interest_rate = 0.06, 
										years = 30)

print(my_mortgage.monthly_payment())