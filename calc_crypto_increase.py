# https://stackoverflow.com/questions/5997987/is-there-an-operator-to-calculate-percentage-in-python
print("Calculates increase/decrease of crypto from time of purchase.")
daCurrentVal = float(input("Enter the current crypto currency value for one coin: "))
daOrigVal = float(input("Enter the crypto currency value for one coin at the time you bought some: "))

daPercentof = daCurrentVal - daOrigVal
daRoundit01 = round(daPercentof, 2)
print("The difference between the original and current crypto coin value is:", daRoundit01)

daResult = (daPercentof / daOrigVal) * 100.0
daRoundit02 = round(daResult, 2)
print("percent of increase/decrease", daRoundit02)

print("Calculates the amount in cash that your crypto has increased/decreased by")
daPercentof = float(input("Enter the actual cash amount you spent on crypto at time of purchase: "))
daVar = (daResult * daPercentof) / 100
daAnswer = round(daVar, 2)
print("The value of your crypto has increased by:", daAnswer)
addem = (daAnswer + daPercentof)
daTotal = round(addem, 2)
print("The current value of your crypto is:", daTotal)
