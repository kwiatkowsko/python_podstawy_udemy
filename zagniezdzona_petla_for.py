i = 10
result = 1
for j in range(1,i+1):
    result *= j

print(i, result)

z = 10
for k in range(1, z+1):
    result = 1
    for c in range(1, k+1):
        result *= c
    print(k, result)

list_noun = ['dog', 'potato', 'meal', 'icecream', 'car']
list_adj = ['dirty', 'big', 'hot', 'colorful', 'fast']

for c in list_noun:
    for m in list_adj:
        print(c,m)