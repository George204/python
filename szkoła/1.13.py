import msvcrt
def gi(z):
    try:
        x = int(input(f"{z}:"))
        return x
    except ValueError:
        print("ty głiupi ośle")
        msvcrt.getch()
        exit()
liczby = (gi("a"),gi("b"),gi("c"))
print("największa liczba:", max(liczby))
