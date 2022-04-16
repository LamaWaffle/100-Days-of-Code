# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆
combined_name = name1 + name2

lowercase = combined_name.lower()

true = 0

true += lowercase.count("t")
true += lowercase.count("r")
true += lowercase.count("u")
true += lowercase.count("e")


love = 0

love += lowercase.count("l")
love += lowercase.count("o")
love += lowercase.count("v")
love += lowercase.count("e")


int_truelove = int( str(true) + str(love) )

#print the output and the love score.

if int_truelove<10 or int_truelove >90:
    print(f"Your score is {int_truelove}, you go together like coke and mentos.")

elif int_truelove>=40 and int_truelove<=50:
    print(f"Your score is {int_truelove}, you are alright together.")

else:
    print(f"Your score is {int_truelove}.")


