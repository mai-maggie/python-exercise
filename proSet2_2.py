def miniMonRate(balance, annualInterestRate):
    """
find out the minimum fixed monthly payment
    :param balance: balance on the credit card
    :param annualInterestRate: annual interest rate as a decimal
    :return: the minimum monthly payment round up to ten places
    """
    ans = 10
    while ans > 0:
        print(ans)
        prev_bal = balance
        for month in range(12):
            # updated_bal=prev_bal so prev_bal=prev_bal
            prev_bal = (prev_bal - ans) * (1 + annualInterestRate / 12)
        if prev_bal <= 0:
            print(prev_bal)
            return ans
        else:
            ans += 10
