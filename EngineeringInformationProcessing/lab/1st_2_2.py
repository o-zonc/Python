# 학번: 2022189005
# 이름: 이경환
# 이메일: xerenes@yonsei.ac.kr
# 제출일: 2022-09-13
# 과제번호: 2주차 2번

# 요일 별 학습시간
days = (3,3,3,3,3,3,3)

# 시간당 보상금
rate = 9160

# 학습비 계산
rewards = (days[0] + days[1] + days[2] + days[3] + days[4] + days[5] + days[6]) * rate

# 1주 보상금액
print(f"당신은 1주일 동안 {rewards}원을 보상 받을 수 있습니다.")

# 확인
print(f"당신은 정말 일요일에도 {days[6]} 시간이나 학습에 투자해요?")
hour = input("지난 일요일에는 몇 시간이나 학습했나요? ")

# 일요일 학습시간 변경
days[6] = int(hour)