q = "THE EYES"
print(q[0],q[1],q[2],q[5],q[3],q[7],q[4],q[6])
q = "a gentleman"
print(q[3]+q[6]+q[7]+q[2]+q[0]+q[4]+q[5]+q[1]+q[8:])
c = "THE MORSE CODE"
print(c[1:3]+c[6]+c[2], c[-4:-2]+c[4]+c[-1], c[-2]+c[-3]+c[0]+c[7])

line = 'Program "Kropka nad i" nadamy o: 22:00'
time = line[ line.find(':')+2:]
print(time)
tmp = line[line.find('"')+1:]
title = tmp[:tmp.find('"')]
print(title, time)

line = 'Program "Pytanie na śniadanie" nadamy o: 6:00'
time = line[line.find(':')+2:]
print(time)
tmp = line[line.find('"')+1:]
title = tmp[:tmp.find('"')]
print(title, time)