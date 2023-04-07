def monthlyPayment(balance, annualInterestRate):
    """
use bisection search to get the lowest monthly payment
    :param balance: balance of the credit card
    :param annualInterestRate: annual interest rate as a decimal
    :return lowest monthly payment
    """
    monthly_interest_rate = annualInterestRate / 12
    lower_bound = round(balance / 12, 2)
    upper_bound = round((balance * pow((1 + monthly_interest_rate), 12) / 12.0), 2)

    def recur_find(lower, upper):
        prev_bal = balance
        payment = (lower + upper) / 2
        for month in range(12):
            prev_bal = round((prev_bal - payment) * (1 + annualInterestRate / 12), 2)
        if prev_bal == 0:
            return round(payment, 2)
        elif prev_bal > 0:
            return recur_find(payment, upper)
        else:
            return recur_find(lower, payment)

    return recur_find(lower_bound, upper_bound)


print(monthlyPayment(80000, 0.1825))
