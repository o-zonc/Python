answer_A = 'OXOXO'
answer_B = 'OOXXX'

answer = input('Answer: ')
answer = answer.upper()
count_alice = 0
count_bob = 0
for i in range(5):
  if answer[i] == answer_A[i]:
    count_alice += i
  if answer[i] == answer_B[i]:
    count_bob += i

if count_alice > count_bob:
  print('Alice')
elif count_alice < count_bob:
  print('bob')
else:
  print('same')