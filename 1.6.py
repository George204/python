while True:
    a = int(input("a:"))
    b = int(input("b:"))
    c = int(input("c:"))
    pole = 2*(a*b+b*c+c*a)
    obj = a*b*c
    kraw = 4*(a+b+c)
    print(f"Pole={round(pole,2)}\nObjętość={round(obj,2)}\nKrawędzie={round(kraw,2)}\n")