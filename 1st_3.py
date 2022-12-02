# 학번: 2022189005
# 이름: 이경환
# 이메일: xerenes@yonsei.ac.kr
# 제출일: 2022-09-13
# 과제번호: 2주차 3번

# 시간을 초 단위로 입력
seconds = input('Please enter the time in seconds ')
inseconds = int(seconds)

# 입력받은 시간을 시 분 초 스타일로 계산
hours = inseconds // 3600
remain1 = inseconds % 3600
minutes = remain1 // 60
remain2 = remain1 % 60

# 시 분 초 스타일로 표시
print("Hrs=", hours, "Mins=", minutes, "Secs=", remain2)