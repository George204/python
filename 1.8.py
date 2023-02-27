import os,msvcrt as m
imie = str(input("Jakie jest twoje imie\n"))
while True:
    os.system("cls")
    print("podaj swoje liczby")
    liczby = []
    liczby.append(int(input("a:")))
    liczby.append(int(input("b:")))
    liczby.append(int(input("c:")))
    print(f"{imie} średnia twoich liczb to {round(sum(liczby)/len(liczby),2)}\nndk\n")
    m.getch()    

