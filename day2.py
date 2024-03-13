# Tip Calculator

print("Welcome to the tip calculator :)")
total = float(input("What was the total bill?" ))
tip_amt = int(input("How much tip would you like to give? 10, 12 or 15? "))
ppl = int(input("How many people to split the bill? "))


tip = (total +(total * (tip_amt/100)))/ppl
print ("Each person should pay: £" + str(round(tip,2)))