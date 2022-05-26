import sys
s=input('16진수를 입력하시오:')
value=0
for c in s:
  if (c>='0' and c<='9'):
    v=ord(c)-ord('0')
  elif (c>='A' and c<='F'):
    v=ord(c)-ord('A')+10
  else:
    print('16진수가 아닙니다.')
    sys.exit(0)
  value=value*16+v
print('16진수 {0}는 10진수 {1}입니다.'.format(s,value))