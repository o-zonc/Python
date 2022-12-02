class Rect:
    def __init__(self, width, height=-1):
        if height < 0: height = width
        self.width, self.height = width, height

    def __repr__(self):
        return 'Rect(w='+'%.2f'%self.width+', h='+'%.2f'%self.height+')'
    
    def get_area(self):
        return (self.width * self.height)
    
    def get_peri(self):
        return 2 * (self.width + self.height)
    
    def isSquare(self):
        return (self.width == self.height)
    
class Square(Rect):
    def __repr__(self):
        return 'Square(width='+'%.2f'%self.width+')'
    
    def isSquare(self):
        return True

r1 = Rect(3,5)
print(r1)
print(r1.get_area())
r2 = Square(7)
print(r2)
print(r2.get_area())
print(r1.isSquare())
print(r2.isSquare())