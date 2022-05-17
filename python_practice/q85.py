li = [12,24,35,70,88,120,155]

lst = []
l = len(li)
for i in range((l)):
    if(i!=0 and i !=4 and i!=5):
        lst.append(li[i])

print(lst)