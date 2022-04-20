import random
# 
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")    # List of names.
# 

number_of_names = len(names) -1   # Gives value of how many items from the list.
random_index = random.randint(0, number_of_names)

random_name = names[random_index]
print(f"{random_name} is going to buy the meal today!")


# OR a shorter way to do it is..
random_index = random.randint(0, len(names) - 1)

random_name = names[random_index]
print(f"{random_name} is going to buy the meal today!")