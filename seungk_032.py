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

k = 1
a = 0
while k <= i:
  if i % k != 0:
    k = k + 1
  else:
    a = a + k
    k = k + 1
print(a)