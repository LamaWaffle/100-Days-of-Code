# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆
combined_name = name1 + name2

lowercase = combined_name.lower()

count_t = lowercase.count("t")
count_r = lowercase.count("r")
count_u = lowercase.count("u")
count_e = lowercase.count("e")

true= count_t + count_r + count_u + count_e

count_l = lowercase.count("l")
count_o = lowercase.count("o")
count_v = lowercase.count("v")

love= count_l + count_o + count_v + count_e


int_truelove = int( str(true) + str(love) )

#print the output and the love score.

if int_truelove<10 or int_truelove >90:
    print(f"Your score is {int_truelove}, you go together like coke and mentos.")

elif int_truelove>=40 and int_truelove<=50:
    print(f"Your score is {int_truelove}, you are alright together.")

else:
    print(f"Your score is {int_truelove}.")


#Write your code below this line 👇