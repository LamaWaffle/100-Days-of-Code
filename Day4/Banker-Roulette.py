import random
# 
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")    # List of names.
# 


number_of_names = len(names) -1   # Gives value of how many items from the list.

index_number = random.randint(0,number_of_names)

luckyone = names[index_number]

print(f"{luckyone} is going to buy the meal today!")

# Come back to this course, number 44 from 100 days of code.
