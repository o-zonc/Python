import re

cor = re.compile('(\d{6}[ ,-]-?[1-4]\d{6})|(\d{6}[ ,-]?[1-4])')
male = re.compile('\d{6}[ ,-]-?[1]\d{6}|')

while True:
    num = input('주민등록번호를 ("-"포함, 공백없이) 입력하세요 : ')
    if num == "":
        print("*잘못된 입력입니다*")
    m = cor.match(num)
    if m:
        if 
    else:
        print("**주민등록번호를 확인해주세요**")