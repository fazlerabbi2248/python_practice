def check(x):
    if(x%5==0):
        return True
    return False

def binaryToDecimal(n):
    return int(n,2)

x = input().split(',')

list= []

for i in x:
    temp= (binaryToDecimal(i))
    print(temp)
    if(check(temp)==True):
        temp=str(temp)
        list.append(i)

print(','.join(list))
