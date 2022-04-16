print('''
*******************************************************************************
   __,-----._                       ,-. 
     ,'   ,-.    \`---.          ,-----<._/ 
    (,.-. o:.`    )),"\\-._    ,'         `. 
   ('"-` .\       \`:_ )\  `-;'-._          \ 
  ,,-.    \` ;  :  \( `-'     ) -._     :   `: 
 (    \ `._\\ ` ;             ;    `    :    ) 
  \`.  `-.    __   ,         /  \        ;, ( 
   `.`-.___--'  `-          /    ;     | :   | 
     `-' `-.`--._          '           ;     | 
           (`--._`.                ;   /\    | 
            \     '                \  ,  )   : 
            |  `--::----            \'   ;  ;| 
            \    .__,-      (        )   :  :| 
             \    : `------; \      |    |   ; 
              \   :       / , )     |    |  ( 
     -hrr-     \   \      `-^-|     |   / , ,\ 
                )  )          | -^- ;   `-^-^' 
             _,' _ ;          |    | 
            / , , ,'         /---. : 
            `-^-^'          (  :  :,' 
                             `-^--' 

*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
direction = input("You\'re at a cross road. Where do you want to go? \nType \"left\" or \"right\". ").lower()
if direction == "left":
    question2 = input('You\'ve come to a lake. There is an island in the middle of the lake.\nType \"wait\" to wait for a boat. Type \"swim\" to swim across. ' ).lower()
    if question2 == "wait":
        door = input ( "You arrive at the island unharmed. There is a house with 3 doors.\nOne red, one yellow and one blue.\nWhich colour do you choose? ").lower()
        if door == "red":
            print("You\'re burned to dust by the ballfire! Game Over")
        elif door == "yellow":
            print("Congrats! You found the treasure in the ancient golden toilet bowl!")
        elif door == "blue":
            print("You accidentally step on a giant floof\'s tail.\nHe got so mad and devours you alive. You\'re dead!!\nGame Over!!")
        else:
            print("Haha loser! You died again!")
    else:
        print("Good choice! You\'re actually swimming in Megalodon\'s home sweet home.\nyou\'re his dinner!\nHaha yep Game Over!")
else:
    print("You got a golden ticket to endless hole and stuck there for eternity.\nSo you\'re dead. Game Over!")

