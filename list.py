s=list(input('문자열을 입력하세요:'))
a=int(input('시작할 지점을 선택하세요:'))
c=len(s)

if a>c:
  print('적절하지 않은 시작점입니다.')

b=int(input('시작점에서 몇 개의 문자를 선택할까요?:'))
t=a+b-1
if t>c:
  print('문자열이 부족합니다.')

result=s[a-1:t]
print('결과 문자열은 {0}입니다.'.format(result))