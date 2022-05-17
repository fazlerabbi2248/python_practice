ip = int(input())
even = []

for i in range(0,ip+1):
    if(i%2==0):
        even.append(str(i))

print(','.join(even))