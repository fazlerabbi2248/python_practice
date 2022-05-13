ip = input()

lower =0
upper=0

for i in ip:
    if(i.islower()==True):
        lower=lower+1
    elif(i.isupper()==True):
        upper=upper+1

print('lower number=' ,lower,'upper number=',upper )