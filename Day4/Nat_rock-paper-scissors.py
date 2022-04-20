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

computer= random.randint(0,2)

# if you draw
if you == computer:
  if you == 0:
    print(f"You:\n{rock}\nComputer:\n{rock}\nYou draw.")
  elif you == 1:
    print(f"You:\n{paper}\nComputer:\n{paper}\nYou draw.")
  else:
    print(f"You:\n{scissors}\nComputer:\n{scissors}\nYou draw.")
# if you win
elif you - computer == -2:
  print(f'You:\n{rock}\nComputer:\n{scissors}\nYou won!')
elif you - computer == 1:
  if you == 1:
    print(f'You:\n{paper}\nComputer:\n{rock}\nYou won!')
  if you == 2:
    print(f'You:\n{scissors}\nComputer:\n{paper}\nYou won!')

#if you enter any weird number.
elif you >2:
  print("You lost!! Coz you shouldn't have picked any number more than 2.")

# if you lose>> you - computer = -1 or 2
else:
  if you == 2:
    print(f'You:\n{scissors}\nComputer:\n{rock}\nYou lost!')
  elif you == 1:
    print(f'You:\n{paper}\nComputer:\n{scissors}\nYou lost!')
  else:
    print(f'You:\n{rock}\nComputer:\n{paper}\nYou lost!')