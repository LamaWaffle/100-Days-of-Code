import random
# numbers = random.randint(0, 100)
# random_float = random.random()

# Option 1
flip = random.randint(0, 1)
if flip == 0:
    print("Tails")
else:
    print("Heads")

# Option 2
flip = random.randint(0, 1) if flip == 1: print('Heads') else: print("Tails")

# Option 3
print("Heads" if random.randint(0, 1) == 0 else "Tails")