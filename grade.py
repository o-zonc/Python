test_score = int(input('Enter your score > '))

if test_score >= 80:
    grade = 'A'
elif test_score >= 70:
    grade = 'B'
elif test_score >= 60:
    grade = 'C'
elif test_score >= 50:
    grade = 'D'
else:
    grade = 'F'

if test_score % 10 >= 5:
    sub = '+'
elif test_score % 10 >= 2:
    sub = '0'
else:
    sub = '-'

if grade == 'F':
    lettergrade = grade
else:
    lettergrade = grade + sub

if test_score == 100:
    print('score PS | grade %s'%(lettergrade))
else:
    print('score %02d | grade %s'%(test_score, lettergrade))