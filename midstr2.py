def midstr(s,a,b):
  result=[]
  if a>len(s):
    raise Exception('{0}은 유효하지 않은 시작 지점입니다. 최대 시작 지점: {1}'.format(a,len(s)-1))
  elif b>(len(s)-a+1):
    raise Exception('{0}은 유효하지 않은 문자 수입니다. 선택 가능한 문자 수: {1}'.format(b,len(s)-a+1))
  else:
    result=result+s[a-1:a+b-1]
  return result

s=list(input('대상 문자열 입력'))
a=int(input('시작 지점 입력'))
b=int(input('취할 개수 입력'))

try:
  result=midstr(s,a,b)
except Exception as err:
  print('예외가 발생했습니다. {0}'.format(err))
else:
  result=''.join(result)
  print('결과는 {0}입니다.'.format(result))