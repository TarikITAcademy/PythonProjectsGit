# Project 2 - Tip Calculator
print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? "))
people = int(input("How many people to split the bill? "))
bill_with_tip = tip / 100 * bill + bill
amount_per_person = bill_with_tip / people
total_amount = round(amount_per_person, 2)
print(f"Each person pays {total_amount}")
# End