import random as r
import msvcrt as m
boki = (r.randrange(1,100)/10,r.randrange(1,100)/10,r.randrange(1,100)/10)
print(boki,"\x1b[10;0H")
if max(boki)>(sum(boki)-max(boki)):
    print("trójkąt nie możliwy")
else:
    print("trójkąt możliwy")
m.getch()