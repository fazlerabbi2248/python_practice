import datetime

before = datetime.datetime.now()
print(before)
for i in range(1000):
    x=1+1

after = datetime.datetime.now()
print(after)
execution = after-before
print(execution.microseconds)