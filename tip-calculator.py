print("Welcome to the tip calculator.");
totalBill = input("What was the total bill? $");
tipPercentage = input("What percentage tip would you like to give? 10, 12, or 15? ");
numPeople = input("How many people to split the bill? ");
splitBill = ((totalBill * (tipPercentage/100.0)) + totalBill)/numPeople;
print("Each person should pay: $" + str(round(splitBill, 2)));