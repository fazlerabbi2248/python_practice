ip = input()
word=0
number =0

for i in ip:
    word = word+ i.isalpha()
    number = number +i.isdigit()

print(word,number)