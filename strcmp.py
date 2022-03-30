def deco(func):
  def dec(*args):
    lis=[]
    for i in range(len(args)):
      lis.append(args[i].replace(' ',''))
    return func(lis[0],lis[1])
  return dec

@deco
def strcmp(s,t):
  for i in range(min(len(s),len(t))):
    if s[i]<t[i]:
      return -1
    elif s[i]>t[i]:
      return 1
    else:
      i+1
  if len(s)<len(t):
    return -1
  elif len(s)>len(t):
    return 1
  else:
    return 0

s=input('첫번째 문자열 입력')
t=input('두번째 문자열 입력')
result=strcmp(s,t)
print(result)    