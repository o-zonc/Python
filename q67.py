def plus(x, y):
    a = x+y
    return a

def my_fn(x, a = 2, b = 7):
    c = a * x + b
    return c

a = plus(3,5)
print('plus(3,5) =', a)

b = my_fn(4)
print('my_fn(4) =',b)

c = my_fn(4,5)
print('my_fn(4,5) =',c)

c = my_fn(4,b = 5)
print('my_fn(4,b = 5)',c)

c = my_fn(4,5,0)
print('my_fn(4,5,0)',c)