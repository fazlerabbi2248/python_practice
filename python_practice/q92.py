s = "H1e2l3l4o5w6o7r8l9d"
ns = ''
for i in range(len(s)):
    if (i % 2 == 0):
        ns = ns + str(s[i])
print(ns)