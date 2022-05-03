from audioop import mul


class plusnminus:
  def __init__(self, a, b):
    self.a = a
    self.b = b
    
  def add(self):
    return self.a + self.b

  def minus(self):
    return self.a - self.b

class mulndiv:
  def __init__(self, a, b):
    self.a = a
    self.b = b
  
  def multiple(self):
    return self.a * self.b
  
  def divide(self):
    return self.a / self.b

class fourcal(plusnminus, mulndiv):
  def __init__(self, a, b, c):
    super().__init__(a, b, c)

  def answer(self):
    return self.c

a = plusnminus(4, 2)
print(a.add())