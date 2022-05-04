x = 10
y = 10
print(id(x), id(y))
y += 1 - 1
print(id(x), id(y))
y += 1234567890 
y -= 1234567890
print(id(x), id(y))