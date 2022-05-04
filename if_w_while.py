numbers = [8, 18, 2, 4, 16, 5, 25, 4, 22, 3, 3, 5, 3, 9, 81, 11]
dlugosc = len(numbers) - 1
liczba = 0
while liczba < dlugosc:
    print(numbers[liczba], numbers[liczba+1])

    if numbers[liczba]*numbers[liczba] == numbers[liczba +1]:
        print("\tFOUND", numbers[liczba], numbers[liczba+1])
    liczba += 1
print("#######################")
numbers = [8, 18, 2, 4, 16, 5, 25, 4, 22, 3, 3, 5, 3, 9, 81, 11]
dlugosc = len(numbers) - 2
liczba = 0
while liczba < dlugosc:
    print(numbers[liczba], numbers[liczba+1], numbers[liczba+2])

    if numbers[liczba]*numbers[liczba] == numbers[liczba +1] and numbers[liczba+1]*numbers[liczba+1] == numbers[liczba +2]:
        print("\tFOUND", numbers[liczba], numbers[liczba+1], numbers[liczba+2])
    liczba += 1
print("#######################")
texts = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
dlugosc = len(numbers) - 1
liczba = 0
while liczba < dlugosc:
    print(texts[liczba], texts[liczba+1])

    if len(texts[liczba]) == len(texts[liczba + 1]):
        print("\tFOUND",texts[liczba], texts[liczba + 1])
    liczba += 1