x,y= map(int,input().split(','))
lst = []

for i in range(x):
    temp=[]
    for j in range(y):
        temp.append(i*j)
    lst.append(temp)

print(lst)