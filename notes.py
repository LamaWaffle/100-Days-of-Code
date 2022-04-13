# Print - Prints a string into the console.
print("Hello There")

# input prompt for the user
input("What is your name? ")

# Variables give a name to a piece of data, like a box with a label. Notice a str needs "" and an int doesnt.
my_age = 12
my_name = "NatYolo"

# The += Operator - This is a convenient way of saying: take the previous value and add to it.
my_age = 12
my_age += 4
# my age is now 16.

# To add a paragraph break, a new paragraph put in \n
print("Hello World\nHello World")

#
# Data Types
#
# Strings - "Hey" or "123" with double quotes.
print("Hello")

# Integer - Whole numbers without decimal places.
print(123)
print(123 + 456)

# Float - Floating point number, decimal number.
print(3.14159)

# Boolean - Two values, either True or False.
True
False

# Subscript - pulling out a number from a string.
print("Hello"[0])

# Checking Data Types
age = 23
type(age) # This will print out the type of variable: <class 'int'>

#  Converting Data Types
float()
int()
str()


num_char = len(input("What is your name? \n"))
new_num_char = str(num_char)
print("Your name has " + new_num_char + " characters.")

a = 123
print(type(a))  # Prints and checks data type - which is an int.

a = str(123)  # Prints and converts data type to a str.
print(type(a))

a = float(123)  # Converts to a float.
print(type(a))

print(70 + float("100.5"))  # This will print int AND float.
print(str(70) + str(100))   # This will print the two strings together.


#
# Day 2, Exercise 1
#
## Cannot change the code below.
two_digit_number = input("Type a two digit number: ")
## Cannot change the code above.

# So find the data type, eg. string, interval, float.
(type(two_digit_number))

# Pull out the numbers with subscripting.
first_digit = two_digit_number[0]
second_digit = two_digit_number[1]

# Turn variables into int and + them together.
result = int(first_digit) + int(second_digit)

# Print the result.
print(result)


3 + 5
7 - 2
3 * 2
6 / 3  # When you device, you always end up with a float.
2 ** 2 # To the power of 2. Squared.
PEMDAS-LR # Remember PEMDASLR (Parentheses, Exponents, Multiply & Divide, Add & Subtract, Left to Right)
()
**
* /
+ -
print(3 * 3 + 3 / 3 - 3)  # This order matters. Use thonny to see the order.

#
# Day 2, Exercise 2 (BMI Calculator)
#
# Cannot change the code below
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# # Cannot change the code above
# print(type(height))
bmi = int(weight) / float(height) ** 2
bmi_as_int = int(bmi)

# Rounding numbers - 9 devided by 3, 2 decimals places
print(round(9 / 3, 2))
print(9 // 2) # Using // turns this float into an int.

result = 4 / 2 # 4 / 2 = 2, result is 2.
result /=2 # getting the result and device by 2.

# f-Strings, can insert different variable into strings.
score = 0  # string
height = 1.8  #  float
is_winning = True #  boolean
# Instead of putting + and converting them, just add and f-string.
print("Your score is " + str(score) + ", your height is " + str(height) + " and are you winning? " + str(is_winning))

# Just need to add an 'f' and variable inside {} 
print(f"Your score is {score}, your height is {height} and are you winning? {is_winning}")

#
# Day 2, Exercise 3 (Your life in weeks)
#
age = int(input("What is your current age? "))

years_remaining = 90 - age
days_remaining = years_remaining * 365
weeks_remaining = years_remaining * 52
months_remaining = years_remaining * 12

message = f"You have {days_remaining} days, {weeks_remaining} weeks, and {months_remaining} months left until you are 90 years old."

print(message)

#
# DAY 3
#

# Basic syntax to test if a condition is true. If so, the code with execute, if not it will be skipped.
# Anything that is indented will execute.

if conditon:
    do this
else:
    do this

# Example below

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm?\n"))

if height >= 120:
    print(f"You are {height}cm, you can ride the rollercoaster :)")
else:
    print("Sorry, you have to grow taller, short-ass.")

height = 160 #  = means assignment
height == 160 # == means check equality
height > 160  # greater than.
height >= 160 # greater than or equal to

# Modulo operator gives you the remainder result.
5 % 2
# result is 1.


# Cannot change the code below
number = int(input("Which number do you want to check? "))
# Cannot change the code above

if number % 2 == 0:
    print("This is an even number.")
else:
    print("This is an odd number.")

# Nested if / else
if condition:
    if another condition:
        do this
    else:
        do this
else:
    do this

# if / elif / else condition:
# with elif, once a condition is true, goes through the list, checking which is true.
if condtion1:
    do A
elif condition2:
    do B
elif condition3:
    do C
else:
    do this

print("Nat is pooping")
