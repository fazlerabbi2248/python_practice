n = int(input())
sum=1
for i in range(1,n+1):
    sum=sum*i

print(sum,end=',')

fact=1
i=1
while(i<=n):
    fact=fact*i
    i=i+1
print(fact)