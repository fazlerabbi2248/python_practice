def printtuple():
    tup= ()
    for i in range(1,21):
        added_value = i*i
        added_value_tuple = (added_value,)
        tup = tup + added_value_tuple
    print(tup)


printtuple()