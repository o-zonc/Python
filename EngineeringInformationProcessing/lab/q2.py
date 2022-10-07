TARGET = 2000
money = 1000
year = 0
rate = 0.035

while money < TARGET:
    money = money + money * rate
    year = year + 1

print(year, '년 후', money, '만원이 될 거래요.')