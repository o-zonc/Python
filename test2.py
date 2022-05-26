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

li = [3,4,2,5,2344,148980,-340,0.03]
z = ascOrder(li)
print(z)