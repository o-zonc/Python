scorelist = [10,56,67,95,82]
max1 = 100
min1 = 0

for score in scorelist:
    if score>max1:
        max1=score
    if score<min1:
        min1=score

print('HIscore:',max1,'LOscore:',min1)