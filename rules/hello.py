y = 0
for x in range(1,21):
  for z in range(1,21):
    a = ((3*(x**3)) + ((z**3) - 1))**(1 / 2)
    y += a
print(y) #33374.78951642248