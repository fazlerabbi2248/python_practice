class Circle:
    def __init__(self,radious):
        self.radious = radious
    def calArea(self):
        return 3.14*self.radious*self.radious

c1 = Circle(3)
print(c1.calArea())
