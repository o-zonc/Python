import random
import time

def checkRank(ans, lotto):
    """
    1등의 숫자와 비교해 맞춘 숫자가 몇 개인지 확인합니다.
    """
    right_num = 0
    for i in range(len(ans)):
        right_num += (ans[i] == lotto[i])
    
    return right_num

def genNum():
    """
    로또의 6개 숫자를 생성합니다.
    """
    numbers = []
    while len(numbers) < 6:
        num = random.randint(1, 45)
        if num not in numbers:
            numbers.append(num)
    return sorted(numbers)

def genNumB():
    """
    로또의 1등 숫자 6개와 2등 보너스 숫자를 생성합니다.
    """
    numbers = []
    while len(numbers) < 7:
        num = random.randint(1, 45)
        if num not in numbers:
            numbers.append(num)
    return sorted(numbers)

# 위 2개의 함수를 이용해서
# 여러분의 코드를 작성해 주세요!

# 자동 생성된 로또 정답 번호와 
# 자동 생성된 5개의 숫자 조합으로 (한 개의 조합은 6개의 숫자)
# 꽝이 안 나올 때까지 돌리기!

flag = 1
st = 0
nd = 0
rd = 0
th = 0
fth = 0
prize = 0
iterable = int(input('몇 회 반복할까요? : '))
print(f'{iterable * 5000}원을 사용합니다.')
time.sleep(3)

while (flag <= iterable):
    rank1 = genNumB()
    prizefirst = rank1[0:5]
    bonus = rank1[6]
    print('1등 번호 :', prizefirst)
    res = []
    for i in range(5):
        res.append(genNum())
        print(res[i])
    
    print(f'{flag}회차 결과는?')

    for check in res:
        crtnum = checkRank(check, rank1)
        if crtnum == 6:
            print('1등!')
            prize += 1952160000
            time.sleep(1)
            st += 1
        elif crtnum == 5:
            if bonus in res:
                print('2등!')
                prize += 54226666
                time.sleep(1)
                nd += 1
            elif bonus not in res:
                print('3등!')
                prize += 1427017
                time.sleep(1)
                rd += 1
        elif crtnum == 4:
            print('4등!')
            prize += 50000
            th += 1
        elif crtnum == 3:
            print('5등!')
            prize += 5000
            fth += 1
        else:
            print('꽝..')
    
    flag += 1

print()
print(f'{flag - 1} 회 중 | 1등 {st} 회, 2등 {nd} 회, 3등 {rd} 회, 4등 {th} 회, 5등 {fth} 회 당첨!')
time.sleep(2)
print()
print(f'소비한 금액 : {iterable * 5000}원')
print(f'당첨된 금액 : {prize}')
if (prize - iterable * 5000) >= 0:
    rst = '수익'
else:
    rst = '손해'
print(f'로또의 결과 : {prize - iterable * 5000}원 {rst}')