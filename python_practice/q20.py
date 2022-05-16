class calculator:
    def __init__(self,n):
        self.n = n
    def cal(self):
        for i in range(0,self.n):
            if(i%7==0):
                print(i)

input = int(input("Enter the number:"))
cal1 = calculator(input)
cal1.cal()