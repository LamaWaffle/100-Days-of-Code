print(""" _                                                           
| |                                                          
| |_ _ __ ___  __ _ ___ _   _ _ __ ___ _ __ ___   __ _ _ __  
| __| '__/ _ \/ _` / __| | | | '__/ _ \ '_ ` _ \ / _` | '_ \ 
| |_| | |  __/ (_| \__ \ |_| | | |  __/ | | | | | (_| | |_) |
 \__|_|  \___|\__,_|___/\__,_|_|  \___|_| |_| |_|\__,_| .__/ 
                                                      | |    
                                                      |_|
""")

print("""
Welcome to Treasure Island.
Your mission is to find the treasure and get out alive!
""")

choice1 = input("Which way do you turn, left or right?\n").lower()

if choice1 == "left":
    choice2 = input("You come across a river, do you wait or swim?\n").lower()
    if choice2 == "wait":
        choice3 = input("You see three doors, a blue door, a yellow door and a red door, which door do you go through?\n").lower()
        if choice3 == "yellow":
            print("YOU WIN!")
        elif choice3 == "red":
            print("You are burned by fire, game over.")
        elif choice3 == "blue":
            print("You are eaten by beasts, game over.")
        else:
            print("You choose a door that doesnt exist, you lose.")
    else:
        print("You get eaten by sharks")
else:
    print("You die, bad luck.")