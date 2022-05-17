li = [12,24,35,70,88,120,155]
lst = []
l = len(li)
for i in range((l)):
    if(i>4 or i<2):
        lst.append(li[i])

print(lst)
