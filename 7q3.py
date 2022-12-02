div = '융합예술대학'# 전역변수 선언
dept = '<미기재>'# 전역변수 선언
reg_no = 0

def reg_GM(name):
    dept = '게임개발학과'# 지역변수 선언
    global reg_no
    reg_no += 1
    print (reg_no, '.이름 :', name, ', 소속 :', div, dept)

def reg_MG(name):
    global reg_no
    reg_no += 1
    print (reg_no, '.이름 :', name, ', 소속 :', div, dept)

def reg_BT(name):
    dept = '뷰티디자인학과'# 지역변수 선언
    reg_no += 1
    print (reg_no, '.이름 :', name, ', 소속 :', div, dept)

reg_GM('name')
reg_MG('name')
reg_BT('name')