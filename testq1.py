fname = input('[내용 확인하고 싶은 파일 이름을 입력하세요] > ')

while fname:# fname이 제대로 입력되면 반복 (오류시 종료)
    myfile = open(fname,'r')
    print(myfile.read())
    fname = input('> \n[내용 확인하고 싶은 파일 이름을 입력하세요] > ')