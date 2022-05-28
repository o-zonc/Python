num = []
for i in range(5):
    n = int(input("Enter a number: "))
    num.append(n)

up = sorted(num)
down = up[:]
down = sorted(down, reverse = True)

times = []
for j in range(5):
    t = up[j] * down[j]
    times.append(t)

print(times)