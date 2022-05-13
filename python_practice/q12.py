lst = []

for i in range(1000,3000):
    if(i%2==0):
        i=str(i)
        lst.append(i)

print(','.join(lst))