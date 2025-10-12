def loan_payment(principal: float, annual_rate: float, years: int):
    r = annual_rate / 100 / 12
    n = years * 12
    if r == 0:
        payment = principal / n
    else:
        payment = principal * r * (1+r)**n / ((1+r)**n - 1)
    return {"monthly_payment": payment, "total_payment": payment * n}
