n = int(input())
sum=0

for i in range(1,n+1):
    print(i)
    temp = i/(i+1)
    print(temp)
    sum=sum+temp
    print(sum)

print(sum)