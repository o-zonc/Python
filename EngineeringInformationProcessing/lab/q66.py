plus = lambda x, y: x+y
a = plus(3,5)
print('plus(3,5) =', a)

my_fn = lambda x, a = 2, b = 7: a*x+b
b = my_fn(4)
print('my_fn(4) =',b)

c = my_fn(4,5)
print('my_fn(4,5) =',c)

c = my_fn(4,b = 5)
print('my_fn(4,b = 5)',c)

c = my_fn(4,5,0)
print('my_fn(4,5,0)',c)
