import random as r
import msvcrt as m
boki = (r.randrange(1,100)/10,r.randrange(1,100)/10,r.randrange(1,100)/10)
if max(boki)>(sum(boki)-max(boki)):
    print("trójkąt nie możliwy")
else:
    print(boki, "\x1b[20;0Htrójkąt możliwy")
m.getch()
