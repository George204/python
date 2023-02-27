import msvcrt as c,os 
print("cześć\nnaciśnij dowolny klawisz")
c.getch(),os.system("cls")
polep,obj = 5.875**2*6,5.875**3
print(f"pole pow.:{round(polep,2)}\nobjętość:{round(obj,2)}")