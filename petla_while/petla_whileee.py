number = 1
previousNumber = 0
while number <= 50:
    print(number + previousNumber)
    previousNumber = number
    number += 1

import random
my_number = random.randint(0,20)
guess= -1
trials = 0
print("Guess my number!")
while guess != my_number:
    guess = int(input())
    trials += 1
    if guess == my_number:
        print("Bravo!")
        print(trials)
    elif guess > my_number:
        print("Sorry - my number is smaller than your guess, Try again!")
    else:
        print("Sorry - my number is greater than your guess, Try again!")