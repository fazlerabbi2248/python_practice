import zlib

l = zlib.compress(b'hello world!hello world!hello world!hello world!')
print(l)
print(zlib.decompress(l))