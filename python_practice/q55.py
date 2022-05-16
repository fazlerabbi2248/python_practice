ip = input().split()
lst = []
for i in ip:
    if i.isdecimal():
        lst.append(i)
print(lst)
