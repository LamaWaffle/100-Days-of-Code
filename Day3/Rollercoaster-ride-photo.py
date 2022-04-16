# Same file as the original, but with an option for a photo.
# Code modified for this option, added bill variable.

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm?\n"))

bill = 0    # This is the starting / default variable for the bill.

if height >= 120:
    print(f"You are {height}cm, you can ride the rollercoaster :)")
    age = int(input("What is your age?\n"))

    if age <= 12:
        bill = 5    # Updates bill to $5
        print("Child tickets are $5.")

    elif age <= 18:
        bill = 7    # Updates bill to $7
        print("Youth tickets are $7.")

    elif age >= 45 and age <= 55:
        bill = 0    # Pension tickets are free
        print("Pension tickets are free.")

    else:
        bill = 12  # Updates bill to $12
        print("Adult tickets are $12.")

    photo = input("Do you want a photo taken? Y or N.\n")
    if photo == "y":
        bill += 3   # bill = bill + 3 < This is another way to write it, the longer way.

    print(f"Your final fill is ${bill}")    # Prints out the final bill.

else:
    print("Sorry, you have to grow taller, short-ass.")