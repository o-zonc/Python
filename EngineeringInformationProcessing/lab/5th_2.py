# 학번: 2022189005
# 이름: 이경환
# 이메일: xerenes@yonsei.ac.kr
# 제출일: 2022-09-30
# 과제번호: 5주차 2번

email = input('이메일을 입력하세요 : ')

hostname_list = ['gmail.com','yonsei.ac.kr','naver.com']
spemail = email.split('@')

if '@' not in email :
    print('잘못된 이메일 형식입니다.')
elif spemail[1] == hostname_list[0]:
    print('Gmail 아이디:',spemail[0])
elif spemail[1] == hostname_list[1]:
    print('연세메일 아이디:',spemail[0])
elif spemail[1] == hostname_list[2]:
    print('네이버 아이디:',spemail[0])
else:
    s = spemail[1]
    print(f"['{s}'] 아이디:",spemail[0])
