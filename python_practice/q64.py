ip = int(input())
even = []

for i in range(0,ip+1):
    if(i%5==0 and i%7==0):
        even.append(str(i))

print(','.join(even))