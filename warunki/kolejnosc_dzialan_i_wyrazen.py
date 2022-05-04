a=40
print((a*5+50)*20+1022-1996)

c = 11
print((c*2+10)/2-c)

print(2+2*2)
print(7+7/7+7*7-7)


obecnosc = 0.85
srednia = 3.5
praca_semestralna = False
zda = (obecnosc > 0.8 and srednia >= 3) or praca_semestralna == True
print(zda)

zda = (obecnosc > 0.8 and srednia >= 3) and praca_semestralna == True
print(zda)

obecnosc = 0.4
srednia = 2.5
praca_semestralna = True
zda = (obecnosc > 0.8 and srednia >= 3) or praca_semestralna == True
print(zda)
zda = (obecnosc > 0.8 and srednia >= 3) and praca_semestralna == True
print(zda)

