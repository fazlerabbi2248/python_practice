def even(x):
    return x % 2 == 0


def squer(x):
    return x * x


li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
li = map(
    squer, filter(even, li)
)  
print(list(li))