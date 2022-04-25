row1 = ["🟦"],["🟦"],["🟦"]
row2 = ["🟦"],["🟦"],["🟦"]
row3 = ["🟦"],["🟦"],["🟦"]
map = [row1, row2, row3]
print(F"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 'position' is a list
first_digit = int(position[0]) -1  #converts to int, picks out the item from the list.
second_digit = int(position[1]) -1






map [first_digit][second_digit] = "❌"   #Update map variable, with first a second digit.
print(F"{row1}\n{row2}\n{row3}")