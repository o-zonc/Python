player1 = 0
player2 = 0

while True:
  p1 = int(input('p1: '))
  if p1 == -1:
    break
  player1 += p1
  p2 = int(input('p2: '))
  if p2 == -1:
    break
  player2 += p2
  
if player1 > player2:
  print('player1')
elif player1 < player2:
  print('player2')
else:
  print('draw')