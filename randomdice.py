import random
N = int(input('Seed: '))
random.seed(N)

def Dice():
    i = 0
    dice = {'1':0, '2':0, '3':0, '4':0, '5':0, '6':0}
    while i <= 100:
        die = random.randint(1,6)
        dice[f'{die}'] += 1
        i += 1
    dice = sorted(dice.items(), key=lambda x: x[1], reverse=True)
    return dice[0][0]
print(Dice())