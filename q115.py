class Rect:
    count = 0

    def __init__(self, w, h):
        self.width, self. height = w, h
        Rect.count += 1
    
if __name__ == '__main__':
    r1 = Rect(3, 5)
    print('r1 (width, height, count) = ', r1.width, r1.height, r1.count)
    r2 = Rect(4, 7)
    print('r1 (width, height, count) = ', r1.width, r1.height, r1.count)
    print('r2 (width, height, count) = ', r2.width, r2.height, r2.count)
    r3 = Rect(5, 2)
    print('r1 (width, height, count) = ', r1.width, r1.height, r1.count)
    print('r2 (width, height, count) = ', r2.width, r2.height, r2.count)
    print('r3 (width, height, count) = ', r3.width, r3.height, r3.count)
    r4 = Rect(6, 3)
    print('r1 (width, height, count) = ', r1.width, r1.height, r1.count)
    print('r2 (width, height, count) = ', r2.width, r2.height, r2.count)
    print('r3 (width, height, count) = ', r3.width, r3.height, r3.count)
    print('r4 (width, height, count) = ', r4.width, r4.height, r4.count)