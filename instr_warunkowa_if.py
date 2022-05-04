like = 500
share = 400

if like >= 500 and share >=100:
    print("Cena obniżona o 10%!!!")
else:
    print("Cena pozostaje bez zmian!")

isPizzaOrdered = False
isBigDrinkOrdered = True
isWeekend = False

if (isPizzaOrdered == True or isBigDrinkOrdered == True) and isWeekend != True:
    print("Otrzymujesz kupon na burgera!")
else:
    print("Rabat nie został naliczony.")

diskSize = 140
diskSizeUsed = 133
fileSize = 10
if diskSize - diskSizeUsed > fileSize:
    print("File can be downloaded.")
else:
    print("Not enough space to download.")