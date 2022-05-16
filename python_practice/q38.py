tup = (1,2,3,4,5,6,7,8,9,10)
list1 ,list2 = [],[]
len =len(tup)
print(len)
for i in range(0,int(len/2)):
    list1.append(tup[i])

for i in range(int(tup.__len__()/2),tup.__len__()):
    list2.append(tup[i])

print(list1)
print(list2)
