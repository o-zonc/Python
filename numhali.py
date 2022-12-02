# 학번: 2022189005
# 이름: 이경환
# 이메일: xerenes@yonsei.ac.kr
# 제출일: 2022-10-14
# 과제번호: 7주차 2번

import random

dummy = [1, 2, 3, 4]
dummy = dummy * 13
random.shuffle(dummy)

n = 1
end = int(input('종료할 차례: '))
p = [[0], [0]]

# p[0] for jane and p[1] for mike
p[0][0] = dummy.pop()
p[1][0] = dummy.pop()

while True:
    card = dummy.pop()
    turn = ['mike', 'jane']
    print(f'{n}번째 턴, {turn[n%2]}의 차례')
    # 카드를 한 장 뽑는다
    if n % 2 == 0:
        p[0].append(card)
    else:
        p[1].append(card)

    # 상태를 출력
    print('{'+f'{turn[0]}: {p[0]}, {turn[1]}: {p[1]}'+'}')

    # 누군가의 덱에 카드가 없으면
    if p[0] == [] or p[1] == []:
        print('덱에 카드가 없음')

    # 카드의 합이 5라면
    elif p[0][-1] + p[1][-1] == 5:
        hello = random.randint(0,1)
        if hello == 0:
            print('jane 종을 울림')
            for deck in p[0]:
                p[1].insert(0, deck)
                p[0] = []
        else:
            print('mike 종을 울림')
            for deck in p[1]:
                p[0].insert(0, deck)
                p[1] = []


    # n이 종료할 차례가 되면
    if n == end:
        print('게임 종료')
        break
    
    # 다음 턴으로
    n += 1

# 게임 종료 후 결과 출력
if len(p[0]) > len(p[1]):
    print(' 결과: mike의 승리')
elif len(p[0]) < len(p[1]):
    print(' 결과: jane의 승리')
else:
    print(' 결과: 비김')
