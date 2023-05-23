a = float(input("a:"))
b = float(input("b:"))
if 0 >= a or 0 >= b:
    print("liczba podana w danych nie jest większa niż 0")
else:
    print(f"pole prostokąta:{a*b}")