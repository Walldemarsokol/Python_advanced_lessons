import random as rnd

START = -100
STOP = 1_000
STEP = 10
data = [2, 4, 6, 8, 42, 73]

print(f'{rnd.randint(START,STOP) = }')  # rnd.randint(START,STOP) = 528
print(f'{rnd.uniform(START,STOP) = }')  # rnd.uniform(START,STOP) = 632.0076634684854
print(f'{rnd.choice(data) = }')  # rnd.choice(data) = 4
print(f'{rnd.randrange(START,STOP,STEP) = }')  # rnd.randrange(START,STOP,STEP) = 300
