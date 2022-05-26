from time import sleep
from cmath import sqrt

def lin(*s):
  a=float(s[0])
  b=float(s[1])
  if a==0 and b==0:
    return 'INDETERMINATE'
  elif a!=0:
    return a/b
  else:
    return 'INCONSISTENT'

def quar(*s):
  a=float(s[0])
  b=float(s[1])
  c=float(s[2])
  if a!=0:
    sqr=(b**2)-(4*a*c)
    x1=((-1*b)+sqrt(sqr))/(2*a)
    x2=x1+(b/a)
    return 