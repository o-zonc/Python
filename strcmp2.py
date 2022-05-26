def strcmp(*s):
  for i in range(min(len(s[0]),len(s[1]))):
    if ord(s[0][i])>ord(s[1][i]):
      return 1
    elif ord(s[0][i])<ord(s[1][i]):
      return -1
  if len(s[0])==len(s[1]):
    return 0
  if len(s[0])<len(s[1]):
    return -1
  else:
    return 1
st1=input('문자열 1 입력')
st2=input('문자열 2 입력')
print(strcmp(st1,st2))