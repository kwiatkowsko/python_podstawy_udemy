szerokosc = 50
wysokosc = 7

numbers = [1]
line = ''
for n in numbers:
    line+= "%3d " % (n)
print(line.center(szerokosc))

for i in range(wysokosc - 1):
    newNumbers = [1]

    position = 0
    while position < len(numbers) -1:
        newNumbers.append(numbers[position] + numbers[position+1])
        position+= 1
    newNumbers.append(1)

    numbers = newNumbers.copy()

    line = ''
    for n in numbers:
        line += "%3d " % (n)
    print(line.center(szerokosc))