import math

ip = input().split(',')

ls =[]
for i in ip:
    if(int(i)%2 !=0):
        ls.append(str(int(i)*int(i)))

print(','.join(ls))
