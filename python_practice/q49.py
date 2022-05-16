class Shape():
    def __init__(self):
        pass
    def Calarea(self):
        return 0

class Square(Shape):
    def __init__(self,length):
        Shape.__init__(self)
        self.length = length

    def Calarea(self):
        return self.length*self.length

sq = Square(4)
print(sq.Calarea())
