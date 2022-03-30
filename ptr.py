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

def numcmp(s,t):
  s,t=float(s),float(t)
  if s>t:
    return 1
  elif s==t:
    return 0
  else:
    return -1

def fcmp(s,t):
  NUM, CHARCT=1,2
  cond=NUM

  for i in range(len(s)):
    c=s[i]
    if i==0 and c=='-':
      continue
    if c.isdigit() or c=='.':
      continue
    else:
      cond=CHARCT
      break
  
  if cond==NUM:
    for i in range(len(t)):
      c=t[i]
      if i==0 and c=='-':
        continue
      if c.isdigit() or c=='.':
        continue
      else:
        cond=CHARCT
        break
  
  if cond==NUM:
    return numcmp
  else:
    return strcmp

s,t=input('문자열 1 입력'),input('문자열 2 입력')
p=fcmp(s,t)
print(p(s,t))