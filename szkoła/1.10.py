a = int(input("licznik:"))
b = int(input("mianownik:"))
if b == 0:
    print("nie można podzielić mianownik = 0")
elif a%b != 0:
    print("liczby nie podzielne")
else:
    print("liczby się dzielą")