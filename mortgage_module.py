class FixedMortgageCalculator():
    '''
    Fixed Mortgage Calculator - Calculates the monthly payments of a fixed term mortgage over given N-years at a given interest rate.

    Args:
        loan_amount (float): is used to specify the amount that a borrower receives as a loan
        yearly_interest_rate (decimal): is used to specify the yearly interest rate
        years (int): the number of years that the loan need to be paid off

    Attributes:
        loan_amount (float): is used to specify the amount that a borrower receives as a loan
        yearly_interest_rate (decimal): is used to specify the yearly interest rate
        years (int): the number of years that the loan need to be paid off
        monthly_interest_rate (decimal): yearly rate divided by number of months
        number_of_monthly_payments (int): Payments per year times number of years
        
    '''
    
    def __init__(self, loan_amount, yearly_interest_rate, years):
        
        self.loan_amount = loan_amount
        self.yearly_interest_rate = yearly_interest_rate
        self.years = years
        
        # derived
        self.monthly_interest_rate = yearly_interest_rate / 12
        self.number_of_monthly_payments = years * 12
        
    def monthly_payment(self):
        '''
        Returns:
            amount of monthly payments
        '''
        numerator =  self.loan_amount * self.monthly_interest_rate * (1 + self.monthly_interest_rate) ** self.number_of_monthly_payments
        denominator = (1 + self.monthly_interest_rate) ** self.number_of_monthly_payments - 1
        
        return numerator / denominator