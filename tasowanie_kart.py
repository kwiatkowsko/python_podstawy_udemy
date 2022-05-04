colors = ['Hearts','Diamonds','Clubs','Spades']
figures = ['Ace','King','Queen','Jack','10','9']

allCards = []
for c in colors:
    for z in figures:
        allCards.append("%s - %s" % (c, z))

print(allCards)

import random

random.shuffle(allCards)
print(allCards)

player1 = []
player2 = []
max = len(allCards)
for i in range(max):
    if i % 2 == 1:
        player1.append(allCards[i])
    if i % 2 == 0:
        player2.append(allCards[i])
print(player1)
print(player2)

player1.append(allCards[0:12])
player2.append(allCards[12:24])
print(player1)
print(player2)
