import textwrap

text = input()
w = int(input())

def twrap(text,w):
    stri = textwrap.wrap(text,w)
    stri ='\n'.join(stri)
    print(stri)

twrap(text,w)