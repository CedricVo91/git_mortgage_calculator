


print("Please enter your equity in CHF")
equity = int(input())
if equity < 100000:
    print("Sorry, your equity is too low to obtain a mortgage in Zurich")
else:
    if equity >= 100000:
        mortgage = equity/2
        print("The offered mortgage will be " + str(mortgage))
print("Please enter your desired time period for downpayment first, followed by desired interest rate")
time = int(input())
rate = int(input())/100
monthlypayment = (rate*mortgage*(1+rate)**time)/((1+rate)**time-1)
print("your monthly payment will be: " + str(int(monthlypayment)))
print("done")