ip = input().split()
ip.sort()
print(ip)
word = set(ip) #remove duplicate value 
word = sorted(
    word)

print(word)

for i in word:
    print(i,ip.count(i))






