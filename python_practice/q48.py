class Rectangle:
    def __init__(self,length,width):
        self.length = length
        self.width = width

    def calArea(self):
        return self.length*self.width

r1 = Rectangle(2,3)
print(r1.calArea())