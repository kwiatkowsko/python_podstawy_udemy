import os
import time

dir = input("Podaj ścieżkę dostępu do katalogu: ")

if not os.path.isdir(dir):
    print("%s musi być katalogiem!" % dir)
else:
    file = input("Podaj nazwę pliku: ")

    path = os.path.join(dir,file)

    if not os.path.isfile(path):
        print("Plik nie istnieje!" % path)
    else:
        print('Wyświetlanie właściwości pliku %s' % path)

        print('Ostatnio modyfikowany: ', time.localtime(os.path.getmtime(path)))
        print('Rozmiar w bitach: ', os.path.getsize(path))

        print('Bieżący katalog: ', os.getcwd())
        print('Ścieżka względna do pliku: ', os.path.relpath(path))