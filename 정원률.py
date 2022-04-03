def floinput(para):
  '''for문과 조합해서 실수를 여러 개 입력받을 수 있는 함수'''
  f = float(input('실수 {0} 입력: '.format(para)))
  return f

li = ['a','b','c','d','e'] # 실수 개수를 늘리거나 줄일 수 있음
F = []
for i in range(len(li)):
  z = floinput(li[i])
  F.append(z)
  
a = 0
for i in range(len(li)): # 모든 변량 더하기
  a = a + F[i]
m = a / len(li) # 평균 m 구하기

b = 0
for i in range(len(li)):
  c = F[i] - m
  b = b + (c**2)
v = b / len(li) # 분산 v 구하기

def min(list):
  '''리스트에서 가장 작은 값을 구하는 함수'''
  while len(list) != 1:
    les = []
    for i in range(1,len(list)):
      if list[i-1] < list[i]:
        les.append(list[i-1])
      else:
        les.append(list[i])
    list = les
  return list[0]

def max(list):
  '''리스트에서 가장 큰 값을 구하는 함수'''
  while len(list) != 1:
    les = []
    for i in range(1,len(list)):
      if list[i-1] < list[i]:
        les.append(list[i])
      else:
        les.append(list[i-1])
    list = les
  return list[0]

min, max = min(F), max(F)

def ascOrder(list):
  '''리스트를 오름차순으로 정리하는 함수'''
  for j in range(len(list)):
    k = len(list) - j
    for i in range(1,k):
      if list[i-1] >= list[i]:
        temp = list[i]
        list[i] = list[i-1]
        list[i-1] = temp
  return list

asc = ascOrder(F)

print('평균은 {0}, 분산은 {1}입니다.'.format(m,v))
print('최솟값은 {0}, 최댓값은 {1}입니다.'.format(min,max))
print('오름차순으로 정렬하면')
print(asc)
print('내림차순으로 정렬하면')

def desOrder(list):
  '''리스트를 내림차순으로 정리하는 함수'''
  for j in range(len(list)):
    k = len(list) - j
    for i in range(1,k):
      if list[i-1] < list[i]:
        temp = list[i]
        list[i] = list[i-1]
        list[i-1] = temp
  return list

des = desOrder(F)

print(des)
print('입니다.')