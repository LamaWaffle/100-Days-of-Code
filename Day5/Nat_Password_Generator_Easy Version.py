#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
# there are 52 letters, 10 numbers, 9 symbols
password=""  #set up empty string values and use loop to add letters, symbols, and numbers

for letter in range (1,nr_letters+1):#for loop with range to define how many time it will loop. the nr_ letters gotta + one otherwise the input number will be excluded from the loop.
  x = random.choice(letters) # pick up random letter from the list
  password = password + x

for symbol in range (1,nr_symbols+1):
  y = random.choice(symbols)
  password = password + y

for number in range (1, nr_numbers+1):
  z = random.choice(numbers)
  password = password +z

print(password)
