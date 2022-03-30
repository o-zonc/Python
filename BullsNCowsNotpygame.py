import random
import time

class Invinput(Exception):
  def __init__(self,diff):
      super().__init__('{0}은 적절하지 않은 입력입니다.'.format(diff))

while True:
  try:
    diff=input('난이도를 설정하세요: [3]자리 수 / [4]자리 수 / [5]자리 수')
  except Invinput as err:
    print(err)
  else:
    diff=int(diff)
    break

for i in range(1,diff+1):
  BNClist=[]
  r=random.randint(0,9)
  BNClist.append(r)
