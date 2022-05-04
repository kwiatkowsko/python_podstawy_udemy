string_A = '+---+---+---+---+'
string_B = '|   |   |   |   |'

for i in range(10):
    print(string_A)

for i in range(4):
    print(string_A)
    print(string_B)

for z in range(10):
    print('x' * z)

for c in range(10):
    if c % 2 == 0:
        print("x" * c)
    else:
        print("o" * c)
