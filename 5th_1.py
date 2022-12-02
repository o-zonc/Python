# 학번: 2022189005
# 이름: 이경환
# 이메일: xerenes@yonsei.ac.kr
# 제출일: 2022-09-30
# 과제번호: 5주차 1번

li = []
while True:
    a = int(input('공학정보처리 점수를 입력하세요 : '))
    if a == 0:
        print('점수 리스트: ')
        print(li)
        avg = sum(li) / len(li)
        print('지금까지 평균 점수 =', avg)
        print('05주차 실습 과제 1번 끝')
        break
    li.append(a)
    print('점수 리스트:',li)
    print('평균 점수 =', sum(li) / len(li))