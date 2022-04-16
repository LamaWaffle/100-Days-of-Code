print(""" _                                                           
88888b.  .d88b.  .d88b.  8888b. .d8888b 888  888.d8888b  
888 "88bd8P  Y8bd88P"88b    "88b88K     888  88888K      
888  88888888888888  888.d888888"Y8888b.888  888"Y8888b. 
888 d88PY8b.    Y88b 888888  888     X88Y88b 888     X88 
88888P"  "Y8888  "Y88888"Y888888 88888P' "Y88888 88888P' 
888                  888                                 
888             Y8b d88P                                 
888              "Y88P"  
""")

username = input("What is your name?\n")

print("Welcome, " + username )

print("You've been trapped in this simulation.. Your goal is to escape..Do you understand?\n")

intro = input("Y or N ?\n")
if intro.lower() == "y":
    print("\nYou are currently in a dark room, you feel confused.\nYou have no memory of how you got here..\n")
    light_switch = input("You can see a light in front of you, do you turn it on?\n")
    
    if light_switch == "y" and "yes" and "yeah":
        door = print("The lights suddenly turn on, the bliding bright light is just too much for your weak, small eyes.You squint, sneeze and fart, resulting in 20/20 vision..\nYou can see a red door at the end of the hallway, covered in smokey bbq sauce..\nDo you walk up to it..?\n")
        
        if door == "y":
            print("You skip and jump to the door, you are now a princess. Well Done, you've beaten the game!")
        else:
            print("You fart your brains out...\nGAME OVER!")

    else:
        print("You feel too weak to do anything, you try to gather the energy to get up, but you break a hip while doing so.. Resulting in your immidiate death..\nYou slowly fade away until the mice eat your skin.\n\nGAME OVER!")
        exit()
        #Import its own file. Add exit() program if NO.
else:
    intro.lower() == "n"
    exit()






# hungry = input("Are you hungry? True or false \n")

# if hungry.lower() == "true":
#     print("Feed me!")
# else:
#     print("I'm not hungry.")




# choice1 = input("Which way do you turn, left or right?\n").lower()

# if choice1 == "left":
#     choice2 = input("You come across a river, do you wait or swim?\n").lower()
#     if choice2 == "wait":
#         choice3 = input("You see three doors, a blue door, a yellow door and a red door, which door do you go through?\n").lower()
#         if choice3 == "yellow":
#             print("YOU WIN!")
#         elif choice3 == "red":
#             print("You are burned by fire, game over.")
#         elif choice3 == "blue":
#             print("You are eaten by beasts, game over.")
#         else:
#             print("You choose a door that doesnt exist, you lose.")
#     else:
#         print("You get eaten by sharks")
# else:
#     print("You die, bad luck.")