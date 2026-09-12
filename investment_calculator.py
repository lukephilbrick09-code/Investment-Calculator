InitialInvestment = float(input("What's your initial investment? "))
MonthlyContribution = float(input("How much are you contributing monthly? "))
ExpectAnnReturn = float(input("What's the expected annual return? x %"))
InvestmentPeriod = int(input("How many years would you like to invest? "))

MonthlyInterest = (ExpectAnnReturn / 100) /12

Balance = InitialInvestment
contribution = InitialInvestment

for i in range(InvestmentPeriod*12):
    contribution = contribution + MonthlyContribution

    Balance += MonthlyContribution
    Balance *= (1+MonthlyInterest)

print("You have contributed £ " + str(round(contribution,2)))


print("Your balance is now:  " + str(round(Balance,2)))

profit = Balance - contribution

print("Therefore, you have profited £ " + str(round(profit,2)))
