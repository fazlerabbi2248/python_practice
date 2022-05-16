def even(x):
    return x % 2 == 0


evenNumbers = filter(even, range(1, 21))
print(list(evenNumbers))