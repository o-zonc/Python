# 학번: 2022189005
# 이름: 이경환
# 이메일: xerenes@yonsei.ac.kr
# 제출일: 2022-11-11
# 과제번호: 11주차 1번

try:
    car_num = input()

    carClassTp = ('승용차', '승합차', '화물차', '특수차', '긴급자동차')
    usageTp = ('개인용', '사업용', '택배', '렌터카', '군용')

    HangulTp = ('가나다라마거너더러머버서어저고노도로모보소오조구누두루무부수우주', '바사아자', '배', '하허호', '육해공국합')

    temp = 5

    if (len(car_num) == 9):
        numFront = car_num[0:3]
        Hangul = car_num[3]
        numEnd = car_num[5:9]
    elif (len(car_num) == 8):
        numFront = car_num[0:2]
        Hangul = car_num[2]
        numEnd = car_num[4:8]
    else:
        raise Exception(ValueError)

    if (numEnd.count('0') >= 2):
        raise Exception(ValueError)
    
    if ('0' in numEnd[1:3]):
        raise Exception(ValueError)
    
    if ((len(numFront) == 3) and (numFront[0] == '0')):
        raise Exception(ValueError)

    numFront = int(numFront)
    numEnd = int(numEnd)
    
    if (numFront >= 1 and numFront <= 69) or (numFront >= 100 and numFront <= 699):
        carClass = '승용차'
    elif (numFront >= 70 and numFront <= 79) or (numFront >= 700 and numFront <= 799):
        carClass = '승합차'
    elif (numFront >= 80 and numFront <= 97) or (numFront >= 800 and numFront <= 979):
        carClass = '화물차'
    elif (numFront >= 98 and numFront <= 99) or (numFront >= 980 and numFront <= 997):
        carClass = '특수차'
    elif (numFront >= 998 and numFront <= 999):
        carClass = '긴급자동차'
    else:
        raise Exception(ValueError)

    for i in range(5):
        if (Hangul in HangulTp[i]):
            temp = i
        
    if temp == 0:
        usage = '개인용'
    elif temp == 1:
        usage = '사업용'
    elif temp == 2:
        usage = '택배'
    elif temp == 3:
        usage = '렌터카'
    elif temp == 4:
        usage = '군용'
    else:
        raise Exception(ValueError)

except:
    print('유효하지 않은 번호')
else:
    print(carClass+'/'+usage)