inputdata = [0,1,2,3,5,8,13,21,34,55,89]
factortable = [0,0.01,0.02, 0.03,0.05,0.08,0.13,0.21,0.34,0.55,0.89]
import math
c = len(inputdata)
y = len(factortable)
print(c)
print(y)
if c == y:
    for z in inputdata:
        
    print("ok")
elif c != y:
    print("inputdata and factortable need to have equal number of elements")