import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

you = int(input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.'))

computer = random.randint(0, 2)

list = [rock, paper, scissors]

# if you enter any weird number.
if you > 2 or you < 0:
    print("You lost!! Coz you shouldn't have picked any number that is not 0, 1 and 2.")

# if you win
elif you - computer == -2 or you - computer == 1:
    print(f'You:\n{rock}\nComputer:\n{scissors}\nYou won!')

# if you draw
elif you == computer:
    print(f"You:\n{list[you]}\nComputer:\n{list[computer]}\nYou draw.")

# if you lose>> you - computer = -1 or 2
else:
    print(f'You:\n{list[you]}\nComputer:\n{list[computer]}\nYou lost!!')