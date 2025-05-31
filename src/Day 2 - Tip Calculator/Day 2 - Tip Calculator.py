print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? $"))
tip = float(input("What percentage tip would you like to give? 10, 12, or 15? "))
numPeople = int(input("How many people to split the bill? "))

eachBill = round((bill + (bill*(tip/100))) / numPeople, 2)

print(f"\nEach person should pay: ${eachBill}")