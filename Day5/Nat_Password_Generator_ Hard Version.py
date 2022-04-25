#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
password=""
all_lists = [letters, numbers, symbols] #list for randomising which type of character we will pick.

letters_quota = nr_letters  # I don't need to create extra variable but I would like to change the name of variable for my own understanding.
symbols_quota = nr_symbols
numbers_quota = nr_numbers


while numbers_quota != 0 or letters_quota != 0 or symbols_quota != 0: #as long as my expression is true, the statement below will keep looping.
  rand1 = random.choice(all_lists) #pick if it should be letter or number or symbol
#If the randomiser decides it will be letters, it will check the "if" condition below.

  if rand1 == letters and letters_quota != 0: #If it picks letters and letter quoter in our password is still available >> the statement below will be executed
    password += random.choice(letters)
    letters_quota = letters_quota - 1 #After one letter quota is used, this will updated the letter quota that we have already use 1 letter.

  elif rand1 == numbers and numbers_quota != 0:
    password += random.choice(numbers)
    numbers_quota = numbers_quota - 1

  elif rand1 == symbols and symbols_quota != 0:
    password += random.choice(symbols)
    symbols_quota = symbols_quota - 1

print(f"Your password will be \" {password} \".\nWarning: Please take note of this! It's irretrievable after this is reset.")
