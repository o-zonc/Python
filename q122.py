# Ch11 p.400 rect03.py 참조
"""
#rect03.py : 사각형의 속성을 처리하는 Rect 클래스
속성 : count, rectid, width, height
메소드 : get_area(), get_peri()
"""
class Rect:
    count = 0 # 클래스 변수

    def __init__(self, height,width):
        self.width, self.height = width, height # 인스턴스 변수
        Rect.count += 1 # 클래스 변수 값 수정
        self.rectid = 'rectid_'+str(Rect.count) # 인스턴스 변수

    def get_area(self): # 사각형의 면적을 계산
        return (self.width * self.height)

    def get_peri(self): # 사각형의 둘레를 계산
        return 2 * (self.width + self.height)

if __name__ == '__main__':
    r1 = Rect(10,100)
    r2 = Rect(100,71000)
    print('r1.get_area(), r1_get_peri() = ', r1.get_area(), r1.get_peri())
    print('r2.get_area(), r2_get_peri() = ', r2.get_area(), r2.get_peri())