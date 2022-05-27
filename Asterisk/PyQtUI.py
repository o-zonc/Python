import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
# 다익스트라 알고리즘이 구현된 모듈을 임포트합니다
# TODO

# 저장된 ui 파일을 불러옵니다
Welcomes = uic.loadUiType("Campuslife.ui")[0]
Everytime = uic.loadUiType("geteverytimeid.ui")[0]

# ui파일을 열 수 있도록 초기화 클래스를 지정합니다
class WelcomeWindow(QDialog, Welcomes):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

class geteverytimeidWindow(QDialog, Everytime):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

# main을 지정합니다
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = WelcomeWindow()
    myWindow.show()
    # 실행
    app.exec_()

# 다익스트라 알고리즘을 실행합니다
# TODO

# Everytime에서 로그인 할 아이디와 비밀번호를 받는 것에 대해 동의를 구하고, 계정 정지의 위험을 설명합니다
# TODO

# Everytime의 로그인 정보를 받아옵니다
# TODO

# 해당 로그인 정보로 시간표를 불러옵니다
# TODO

# 로그인이 실패한 경우 실패 사실을 알립니다
# TODO

# 다익스트라 알고리즘으로 넘기는 것은 알아서 실행바랍니다