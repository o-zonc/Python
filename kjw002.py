import math

def calc_base_a_exponent_n(a,n):
  for i in range(n+1):
    x = math.pow(a,i)
    print(a,'^',i,'=',x)

a = int(input('a: '))
n = int(input('n: '))

calc_base_a_exponent_n(a,n)