a,b,c = 5,6,7
if a == 0:
    if b == c:
        print("równanie tozszamościowe")
    elif b != c:
        print("równanie sprzeczne")
else:
    print(f"x={(c-b)/a}")
