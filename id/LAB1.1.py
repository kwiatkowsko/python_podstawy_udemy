a = b = c = 10
print(a, b, c, id(a), id (b), id (c))
a = 20
print(a, b, c, id(a), id (b), id (c))
a = b = c = [1,2,3]

print(a, b, c, id(a), id(b), id(c))
a += [4]
print(a, b, c, id(a), id(b), id(c))