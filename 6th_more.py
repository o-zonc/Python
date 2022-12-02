# 학번: 2022189005
# 이름: 이경환
# 이메일: xerenes@yonsei.ac.kr
# 제출일: 2022-10-07
# 과제번호: 6주차 2번

def check(num, ans):
    ball = 0
    strike = 0
    for i in range(3):
        if num[i] in ans:
            if num[i] != ans[i]:
                ball += 1
            else:
                strike += 1
    
    return (ball, strike)

answer = str(531)

for i in range(4):
    guess = input('정수를 입력하시오 : ')
    ded = check(guess, answer)
    print(f'{i + 1}회 결과 :', ded[0], 'ball', ded[1], 'strike')
    if i == 3 and ded[1] != 3:
        print(f'** {guess} : 4번 시도! 패배...')
    if ded[1] == 3:
        print(f'** {answer} : {i+1}번만에 승리하였습니다!')
        break
