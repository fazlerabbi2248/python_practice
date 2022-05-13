def hasHigh(x):
    for i in x:
        if(i>='A' and i<='Z'):
            return True
    return False

def hasLower(x):
    for i in x:
        if(i>='a' and i<= 'z'):
            return True
    return False

def hassplChar(x):
    for i in x:
        if(i == "$" or i == "#" or i == "@"):
            return True
    return False

def hasNumber(x):
    for i in x:
        if(i>='0' and i<='9'):
            return True
    return False

def checklength(x):
    l = len(x)
    if(l>=6 and l<=12):
        return True
    return False

password = input().split(',')
aplist = []

for i in password:

    if(checklength(i) and hassplChar(i) and hasHigh(i) and hasLower(i) and hasNumber(i)):

        aplist.append(i)

print(','.join(aplist))
