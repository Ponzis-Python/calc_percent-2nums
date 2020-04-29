# https://stackoverflow.com/questions/5997987/is-there-an-operator-to-calculate-percentage-in-python
print("Calculates what percentage one number is of another.")
#print("Then it takes the result and and 

daPercentof = float(input("Enter the percentage number: "))
daNumba = float(input("Enter the main number: "))

daResult = (daPercentof / daNumba) * 100.0

print(daResult)
print("Calculates a percentage of a number using the previous result as the percent value")
daMainNumba = float(input("Enter the main number: "))
daVar = (daResult * daMainNumba) / 100
daAnswer = round(daVar, 4)
print(daAnswer)