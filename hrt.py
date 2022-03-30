class compare:
  def __init__(self,s,t):
    self.s=s
    self.t=t
  def cmp(self):
    pass
class strcmp(compare):
  def __init__(self, s, t):
    super().__init__(s, t)
  def cmp(self):
    for i in range(min(len(self,s),len(self,t))):
      if self.s[i]>self.t[i]:
        return 1
      elif self.s[i]==self.t[i]:
        return 0
      else:
        return -1
class numcmp(compare):
  def __init__(self, s, t):
    super().__init__(s, t)
  def cmp(self):
    if float(self.s)>float(self.t):
      return 1
    elif float(self.s)==float(self.t):
      return 0
    else:
      return -1
s=input('첫번째 문자열 입력')
t=input('두번째 문자열 입력')
num,charct=1,2
cond=num
for i in range(len(s)):
  c=s[i]
  if i==0 and c=='-':
    continue
  if c.isdigit() or c=='.':
    continue
  else:
    cond=charct
    break
if cond==num:
  for i in range(len(t)):
    c=t[i]
    if i==0 and c=='-':
      continue
    if c.isdigit() or c=='.':
      continue
    else:
      cond=charct
      break
if cond==num:
  p=numcmp(s,t)
else:
  p=strcmp(s,t)
print(p.cmp())