import random
#for i in range(10):
    #print(random.randint(1, 100))
number1 = random.randint(1,100)
print(number1)
counter = 1
number2 = random.randint(1,100)
while number1 != number2:
    counter +=1
    number2 = random.randint(1,100)
    print("number of count =", counter, ",",number2)
print("number 1 is", number1, " and the counter =",counter)

countries = [
    'Uruguay',
    'Russia',
    'Saudi Arabia',
    'Egypt',
    'Spain',
    'Portugal',
    'Iran',
    'Morocco',
    'France',
    'Denmark',
    'Peru',
    'Australia',
    'Croatia',
    'Argentina',
    'Nigeria',
    'Iceland',
    'Brazil',
    'Switzerland',
    'Serbia',
    'Costa Rica',
    'Sweden',
    'Mexico',
    'Korea Republic',
    'Germany',
    'Belgium',
    'England',
    'Tunisia',
    'Panama',
    'Colombia',
    'Japan',
    'Senegal',
    'Poland'
    ]

groupNumber = 0
random.shuffle(countries)

groupNumber = 0

for i in range(len(countries)):
    if i % 4 == 0:
        groupNumber += 1
        print("========== Group %d ==========" % (groupNumber))
    print(countries[i])