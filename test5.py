# 학번: 2022189005
# 이름: 이경환
# 이메일: xerenes@yonsei.ac.kr
# 제출일: 2022-10-21
# 과제번호: 중간고사 실습형 1

while True:
    test_score = int(input('Enter your score > '))

    if test_score >= 82:
        grade = 'A+'
        print(grade, end=' ')
    if test_score >= 80:
        grade = 'A0'
        print(grade, end=' ')    
    if test_score >= 72:
        grade = 'B+'
        print(grade, end=' ')
    if test_score >= 70:
        grade = 'B0'
        print(grade, end=' ')
    if test_score >= 62:
        grade = 'C0'
        print(grade, end=' ')
    if test_score >= 60:
        grade = 'C-'
        print(grade, end=' ')
    if test_score >= 52:
        grade = 'D0'
        print(grade, end=' ')
    if test_score >= 60:
        grade = 'D-'
        print(grade, end=' ')
    if test_score <= 55:
        grade = 'F'
        print(grade, end=' ')
    if test_score == 0:
        break
    print('')