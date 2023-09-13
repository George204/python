import pygame as pg
import sys
import random as r
import time
import math as m
pg.init()

res = (1010,1010)
screen = pg.display.set_mode(res)
bariera = (1000,1000)
nkuli = 4
kule = []
mvx = 0.01
mvy = 0.01
FPS = 60
grav = 0.000981
def ktp(mytuple):
    x , y = mytuple
    ret = ((res[0]/2)+bariera[0]*x,(res[1]/2)+bariera[1]*y)
    return ret
def ktps(x):
    return ktp((x,0))[0]

class kula:
    def __init__(self, vx, vy , x, y, r, colour):
        self.vx = vx
        self.vy = vy
        self.x = x
        self.y = y
        self.r = r
        self.colour = colour

bx = (res[0]/3-bariera[0]/3)/res[0]
by = (res[1]/3-bariera[1]/3)/res[1]

for i in range(nkuli):
    k = kula(r.uniform(mvx*-1,mvx),r.uniform(mvy*-1,mvy),r.uniform(-bx,bx),r.uniform(-by,by),r.randint(10,50),(r.randint(0,255),r.randint(0,255),r.randint(0,255)))
    kule.append(k)
clock = pg.time.Clock()
czas = time.time()    
klatki = 0
# petla gry
while True:
    clock.tick(FPS)
    klatki += 1
    if time.time() - czas > 1:
        czas = time.time()  
        print(f"{klatki} fps")
        klatki = 0
        
    screen.fill(color="grey")
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit(0)
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                sys.exit(0) 
    pg.draw.rect(screen,color="blue", rect=((res[0]/2-bariera[0]/2,res[1]/2-bariera[1]/2),(bariera[0],bariera[1])))            
    for k in kule:
        k.x += k.vx
        k.y += k.vy
        # k.vy += grav
        if ktp((k.x,k.y))[0] + k.r > res[0]/2+bariera[0]/2:
            k.vx = -abs(k.vx)
        if ktp((k.x,k.y))[0]-k.r < res[0]/2-bariera[0]/2:
            k.vx = abs(k.vx)
        if ktp((k.x,k.y))[1]-k.r < res[1]/2-bariera[1]/2:
            k.vy = abs(k.vy)
        if ktp((k.x,k.y))[1] + k.r > res[1]/2+bariera[1]/2:
            k.vy = -abs(k.vy)
        pg.draw.circle(screen,color=k.colour,center=ktp((k.x,k.y)),radius=k.r)
        for i in kule:
            if i != k:
                if (ktp((k.x,0))[0]-ktp((i.x,0))[0])**2 + (ktp((0,k.y))[1]-ktp((0,i.y))[1])**2 < (k.r+i.r)**2:
                    k.vx, i.vx = i.vx, k.vx
                    k.vy, i.vy = i.vy, k.vy
                    
                    
                    print(k.x,i.x)
                    # print(ktps(k.x),ktps(i.x))
                    print(ktps(k.x)-ktps(i.x))
                    x = abs(k.x) - abs(i.x)
                    y = abs(k.y) - abs(i.y) 
                    print(k.r+i.r,m.sqrt((ktps(k.x)-ktps(i.x))**2+(ktps(k.y)-ktps(i.y))**2),m.sqrt(x**2+y**2))
                    print("\n")
                    
                    # print(kdkdxzxc12kdccck.x-i.x," ",k.y-i.y)
                    # print(a)
 
            
    pg.display.flip()
pg.quit()
