def credit_Card_Bal(balance, annualInterestRate, monthlyPaymentRate):
    """
balance after one year if one only pays the minimum monthly payment
    :param balance: balance on the credit card
    :param annualInterestRate: annual interest rate as a decimal
    :param monthlyPaymentRate: minimum monthly payment rate as a decimal
    :return balance after one year
    """
    # monthlyInterestRate = annualInterestRate / 12.0
    # minimumMonthlyPayment = monthlyPaymentRate * balance
    # monthlyUnpaidBal = balance - minimumMonthlyPayment
    # prev_bal = monthlyUnpaidBal + monthlyInterestRate * monthlyUnpaidBal
    prev_bal = round((1 - monthlyPaymentRate) * balance * (1 + annualInterestRate / 12), 2)
    print(prev_bal)
    for month in range(1, 12):
        # minimumMonthlyPayment = monthlyPaymentRate * prev_bal
        # monthlyUnpaidBal = prev_bal - minimumMonthlyPayment
        # prev_bal = round((monthlyUnpaidBal + monthlyInterestRate * monthlyUnpaidBal), 2)
        prev_bal = round((1 - monthlyPaymentRate) * prev_bal * (1 + annualInterestRate / 12), 2)
        print(month, prev_bal)
    return prev_bal
