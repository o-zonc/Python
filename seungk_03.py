import random

while True:
    n = input('seed:')
    random.seed(n)
    count = 0
    dice = [0, 0, 0, 0, 0, 0]
    while count <= 100:
        die = random.randint(0,5)
        print(die)
        dice[die] += 1
        count += 1
    temp = dice
    temp.sort()
    common = max(temp)
    print(dice)
    for i in range(6):
        if common == dice[i]:
            print(i + 1)