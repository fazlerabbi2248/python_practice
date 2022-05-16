import  math


x=0
y=0
while True:
    move = input().split()
    if not move:
        break
    if(move[0]=='UP'):
        x=x+int(move[1])
    if(move[0]=='DOWN'):
        x=x-int(move[1])
    if(move[0]=='RIGHT'):
        y=y+int(move[1])
    if(move[0]=='LEFT'):
        y=y-int(move[1])

print(x,y)
print(round(math.sqrt(x*x+y*y)))