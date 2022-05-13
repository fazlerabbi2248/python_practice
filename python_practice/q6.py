from math import sqrt

def cal(c,h,d):
    return sqrt((2 * c * d) / h)

d = input().split(',')
len = d.__len__()
c=50
h=30

for i in range(1,len+1):
    print(round(cal(c,h,int(d[i-1]))),end=',')

