def list_max(mylist):# 목록 mylist에서 최대값을 찾아서 반환하는 함수
    max1 = 0
    for score in mylist:
        if score > max1:
            max1 = score
            return max1

def list_min(mylist):# 목록 mylist에서 최소값을 찾아서 반환하는 함수
    min1 = 999
    for score in mylist:
        if score < min1:
            min1 = score
            return min1

def list_sum(mylist):# 목록 mylist에서 값의 합계를 찾아서 반환하는 함수
    sum1 = 0
    for item in mylist:
        sum1 += item
        return sum1

def list_aver(mylist):# 목록 mylist에서 평균값을 찾아서 반환하는 함수
    aver1 = list_sum(mylist) / len(mylist)# 개수 구하기 내장 함수 사용
    return aver1

def report_score(mylist):
    aver2 = list_aver(mylist)
    max1 = list_max(mylist)
    min1 = list_min(mylist)

    print("성적 : ", mylist)
    print("평균 성적 : ", aver2)
    print("최고점수 : ", max1, ", 최하점수 : ", min1)

if __name__ == '__main__':
    mylist = [78, 56, 67, 95, 82]
    report_score(mylist)