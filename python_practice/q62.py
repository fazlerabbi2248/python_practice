def fib(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fib(n-1)+fib(n-2)

ip = int(input())

lst = []

for i in range(0,ip+1):
    lst.append(fib(i))

print(lst)