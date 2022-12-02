days = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
date = True

while date:
    try:
        date = input('날짜 <월 일>을 입력하세요')
        mm, dd = date.split()
        mm, dd = int(mm), int(dd)
        if mm < 1 or mm > 12:
            # raise ValueError('월은 1에서 12까지입니다.')
            print('월은 1에서 12까지입니다.')
        if dd < 1 or dd > days[mm-1]:
            #raise ValueError('일은 1에서 %d까지입니다.'%days[mm-1])
            print('일은 1에서 %d까지입니다.'%days[mm-1])
    except ValueError as e:
        print('[입력 오류]', e)
    except IndexError:
        print('12 이하로 입력')
    except:
        print('에러발생')
    else:
        print('%d월 %d일'%(mm, dd))