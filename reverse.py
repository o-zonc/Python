s=list(input('대상 문자열을 입력하세요: '))
t=list(input('삭제할 문자열을 입력하세요: '))
result=[]
for i in s:
  if i not in t:
    result.append(i)
result.reverse()
result=''.join(result)
print('결과 문자열은 {0}입니다.'.format(result))