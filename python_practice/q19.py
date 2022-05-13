lst = []
while True:
    ip = input().split(",")
    if not ip[0]:
        break
    lst.append(tuple(ip))

lst.sort(
    key=lambda x: (x[0], x[1], x[2])
)
print(lst)