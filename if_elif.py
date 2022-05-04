likes = 1000
shares = 500
if likes < 500:
    print("za mało lajków :(")
elif shares < 100:
    print("za mało szeeerów :(")
else:
    print("ZNIŻKA 10%!!!")

isPizzaOrdered = False
isBigDrinkOrdered = False
isWeekend = False

if isWeekend == True:
    print("Zniżka do wykorzystania tylko w tygodniu!")
elif isPizzaOrdered == True or isBigDrinkOrdered == True:
    print("Rabat został naliczony!")
else:
    print("Rabat nie został naliczony. Proszę zamówić duży napój lub dużą pizzę.")