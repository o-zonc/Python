N = int(input('input N:'))
M = int(input('input M:'))

if N > M:
  i = N
else:
  i = M

while i !=1:
  if N % i == 0 and M % i == 0:
    break
  else:
    i = i-1

temp = []
for j in range(1,i+1):
  if i % j == 0:
    temp.append(j)

s = 0
for k in range(len(temp)):
  s = s + temp[k]

print(s)