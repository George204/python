import msvcrt
from math import sqrt

a = int(input("a:"))
b = int(input("b:"))
c = int(input("c:"))
d = int(input("d:"))
print("\x1b[10;0H")
if a == 0:
    if b == 0:
        if c == d:
            print("równanie torzsamościowe")
        elif c != d:
            print("sprzeczne")
    else:
        print(f"x={(d-c)/b}")
else:
    c = c-d
    delta = b**2-4*a*c
    if delta == 0:
        x = (-b)/(2*a)
        print(f"x:{round(x,2)}")
    elif delta > 0:
        x1, x2 = (-b-sqrt(delta))/(2*a), (-b+sqrt(delta))/(2*a)
        print(f"x1:{round(x1,2)}\nx2:{round(x2,2)}")
    elif delta < 0:
        print("brak rozwiązań")
msvcrt.getch()
