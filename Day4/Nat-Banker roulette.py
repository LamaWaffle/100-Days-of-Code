import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
population = (len(names) ) - 1
random_numb = random.randint(0,population)
luckyone = names[random_numb]
print (luckyone + " is going to buy the meal today!")

