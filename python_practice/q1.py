for i in range(2000,3200):
    if(i%7==0 and i%5 !=0):
        print(i,end=',')

print(*(i for i in range(2000, 3201) if i % 7 == 0 and i % 5 != 0), sep=",")