import re

telnum = True
tel_exp = '0[1-8][0-9]?-[0-9]{3,4}-[0-9]{4}' # 전화번호의 정규 표현식

while telnum: # Telnum의 값이 True인 경우 반복 (Null 이면 종료)
    try:
        telnum = input('[전화번호] >> ')
        if not telnum:
            raise NullError
        result = re.match(tel_exp, telnum)
        print(result)
    except: # 입력 값 오류시 오류 메시지 출력
        print(' *입력오류* 프로그램 종료!')
    else:
        if result: # 정상 입력시 월-일 출력
            print(' **성공** 전화번호가 제대로 입력되었습니다!')
        else:# 번호 형식 오류시 오류 메시지 출력
            print(' *번호오류* 전화번호가 형식에 맞지 않습니다.')