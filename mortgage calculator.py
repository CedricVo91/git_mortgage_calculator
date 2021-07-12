


print("Please enter your equity in CHF")
equity = int(input())
if equity < 100000:
    print("Sorry, your equity is too low to obtain a mortgage in Zurich")
else:
    if equity >= 100000:
        mortgage = equity/2
        print("The offered mortgage will be " + str(mortgage))
