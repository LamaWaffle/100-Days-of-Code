import random

animals = input("List your favourite animals.\n")
list = animals.split(", ") # 0Chicken, 1Lamb, 2Goat, 3Horse

items_in_list = len(list) # how many animals did you list?

random_gen = random.randint(0, items_in_list -1)    #0 to number of animals

favourite_animal = list[random_gen]

print(F"Your favourite animal is {favourite_animal}")


"""
Since there are 4 items in the list, but there isnt an item at position 4, last item is at position 3.
list of items 4.
need to choose between 0 and 3 to actually choose an item. (picking 4 doenst do anything.)
"""

animals = ["Goat", "Banana", "Horse"]

for i in range (1):
    print(random.choice(animals))