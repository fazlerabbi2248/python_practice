tup = (1,2,3,4,5,6,7,8,9,10)
newtup = ()
len =len(tup)
for i in tup:
    if(i%2==0):
        added_value = i 
        added_value_tuple = (added_value,)
        newtup = newtup+ added_value_tuple

print(newtup)
