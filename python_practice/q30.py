def printstr(s1,s2):
    len1 = len(s1)
    len2 = len(s2)
    if(len1>len2):
        print(s1)
    elif(len1<len2):
        print(s2)
    elif(len1==len2):
        print(s1,'\n')
        print(s2)

s1 = input()
s2= input()
printstr(s1,s2)