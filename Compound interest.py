##Compound interest
def compound_interest(principle, rate, time):
    interest = principle * ((1 + rate / 100) ** time)
    return interest

principle = int(input("Money you borrowed: "))
interest_rate = float(input("Interest Rate: "))
time = float(input("Overall Duration: "))

total_due = compound_interest(principle, interest_rate, time)

print("Interest Amount is:", total_due)
