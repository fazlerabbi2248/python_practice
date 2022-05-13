line = input().split()


for i in line:
    if(line.count(i)>1):
        line.remove(i)

line.sort()
print(' '.join(line))