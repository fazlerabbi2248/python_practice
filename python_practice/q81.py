lst = [12, 24, 35, 70, 88, 120, 155]

newlst = list(filter(lambda n: n%7!=0 and n%5!=0,lst))
print(newlst)
