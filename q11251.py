class Vect3:
    ndim = 3

    def __init__(self, x, y, z=0):
        self.x, self.y, self.z = x, y, z

    def __repr__(self):
        return 'Vector['+'%.2f'%self.x+', '+'%.2f'%self.y+', '+'%.2f'%self.z+']'
    
    def __add__(self, other):
        __new = Vect3(0,0)
        __new.x = self.x + other.x
        __new.y = self.y + other.y
        __new.z = self.z + other.z
        return __new

v1 = Vect3(4,5,6)
v2 = Vect3(7,8)
v3 = v1 + v2
print(v1, v2, v3)
print(v3.x, v3.y, v3.z)
print(v1.x, v1.y, v1.z)
print(v1.ndim)
print(v1.__new)