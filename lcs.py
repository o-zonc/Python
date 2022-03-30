num=int(input('변환할 숫자 입력:'))
n=int(input('옮길 자릿수 입력:'))
print(bin(num))
i=0
check=0x8000000000000000
while i<n:
  if (num&check)==0:
    num<<=1
  else:
    num<<=1
    num|=1
  i=i+1
print(bin(num))