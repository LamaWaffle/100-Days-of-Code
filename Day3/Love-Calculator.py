print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("Whats their name? \n")

both_names = name1 + name2  # Joins both names
result = both_names.lower()     # Converts to lowercase

t = both_names.count("t")   # counting the amount of times there are t's from the input.
r = both_names.count("r")
u = both_names.count("u")
e = both_names.count("e")

true = str(t + r + u + e)   # Counts each value from the letter and converts it into a string.

l = both_names.count("l")
o = both_names.count("o")
v = both_names.count("v")
e = both_names.count("e")

love = str(l + o + v + e)

score = int(true + love)

if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif 40 <= score <= 50:     # Learn what the fuck this is..
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")