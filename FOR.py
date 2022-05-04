data = ['Error:File cannot be open',
        'Error:No free space on disk',
        'Error:File missing',
        'Warning:Internet connection lost',
        'Error:Access denied']
for blabla in data:
    print(blabla.upper())

for momo in data:
    elements = momo.split(":")
    print(elements[0].upper())
    print(elements[1])

for toto in data:
    elements = toto.split(":")
    if elements[0] == "Error":
        print(elements[0].upper())
    else:
        print(elements[1])