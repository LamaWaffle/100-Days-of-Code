#If the bill was $150.00, split between 5 people, with 12% tip.
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
#Write your code below this line 👇

# Round to two decimal places

# print(round(9 / 3, 2))
# print(9 // 2) # Using // turns this float into an int.


12 / 100
0.12
150 * 0.12
18.0
150 + 18
# OR
150 * 1.12

168 / 5
33.6


print("Welcome to the tip calculator!\n")
bill = (float(input("What was the total bill?\n$")))
# This bill is inputted at a string, so convert with float cause bill would be something like $100.23.
tip = int(input("How much tip would you like to give? 10, 12 or 15\n"))
# Similar to above, but just convert it to an integer.
people = int(input("How many people to split the bill?\n"))
bill_with_tip = tip / 100 * bill + bill
print(bill_with_tip)

NOT FINISHED
