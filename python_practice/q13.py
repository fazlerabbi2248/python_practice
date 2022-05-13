ip = input()

words=0
number=0
for i in ip:
    if ("a" <= i and i <= "z") or ("A" <= i and i <= "Z"):
        words += 1
    if "0" <= i and i <= "9":
        number += 1

print(words , ',' , number)