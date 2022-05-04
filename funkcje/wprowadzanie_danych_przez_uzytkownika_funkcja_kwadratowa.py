def check_int(s):
    if s[0] in ('-', '+'):
        return s[1:].isdigit()
    return s.isdigit()
a = input("Podaj współczynnik a: ")

b = input("Podaj współczynnik b: ")
c = input("Podaj współczynnik c: ")

if not( check_int(a) and check_int(b) and check_int(c) ):
    print("a, b i c muszą być liczbami całkowitymi!")
else:
    a = int(a)
    b = int(b)
    c = int(c)

    if a == 0:
        print('"a" nie może równać się 0!')
    else:
        delta = b ** 2 - 4 * a * c

        if delta < 0:
            print("nie ma rozwiązania")
        elif delta == 0:
            x1 = -b / (2 * a)
            print("Jest jedno rozwiązanie: %.2f" % (x1))
        else:
            x1 = (-b - delta ** 0.5) / (2 * a)
            x2 = (-b + delta ** 0.5) / (2 * a)
            print("Są dwa rozwiązania: %.2f i %.2f" % (x1, x2))