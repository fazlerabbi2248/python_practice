import random

resp = [i for i in range(10, 150, 5) if i%7==0]
print(random.choice(resp))