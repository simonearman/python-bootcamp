print("Welcome to the tip calculator")
total_bill = float(input("What was the total bill? $"))
percentage = int(input("What percentage tip would you like to give? 10, 12, 15? "))
people = int(input("How many people to split the bill? "))
print(f"Each person should pay: ${round(total_bill*(1+percentage/100)/people, 2)}")
