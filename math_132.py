inputdata = [0,1,2,3,5,8,13,21,34,55,89]
factortable = [0,0.01,0.02, 0.03,0.05,0.08,0.13,0.21,0.34,0.55,0.89]
import math
dlugosc1 = len(inputdata)
dlugosc2 = len(factortable)
print(dlugosc1, dlugosc2)

if dlugosc1 == dlugosc2:
    print("ok")
    i = 0
    while i < len(inputdata):
        minvalue=inputdata[i]-factortable[i]*inputdata[i]
        maxvalue=inputdata[i]+factortable[i]*inputdata[i]
        print('minvalue=',minvalue,'maxvalue=',maxvalue)

        mininteger = math.floor(minvalue)
        maxinteger = math.ceil(maxvalue)
        print(mininteger, "\t", inputdata[i], "\t", maxinteger)
        i += 1

elif dlugosc1 != dlugosc2:
    print("inputdata and factortable need to have equal number of elements")

import random

i = 0
while i < len(inputdata):
    minvalue = inputdata[i] - random.random() * inputdata[i]
    maxvalue = inputdata[i] + random.random() * inputdata[i]
    print('minvalue=', minvalue, 'maxvalue=', maxvalue)

    mininteger = math.floor(minvalue)
    maxinteger = math.ceil(maxvalue)
    print(mininteger, "\t", inputdata[i], "\t", maxinteger)
    i += 1

from datetime import datetime

print('results generated', datetime.today())
print('results generated:', datetime.today().strftime("%Y-%m-%d"))
