import pygame as pg
import sys
import random as r
import time
pg.init()

res = (1600,900)
bariera = (500,500)
screen = pg.display.set_mode(res)
FPS = 240
pam = []
clock = pg.time.Clock()
czas = time.time()    
klatki = 0
kule = []


def ktp(mytuple):
    x , y = mytuple
    ret = ((res[0]/2)+bariera[0]*x,(res[1]/2)+bariera[1]*y)
    return ret

class kula:
    def __init__(self, vx, vy , x, y, r, b, colour):
        self.vx = vx
        self.vy = vy
        self.x = x
        self.y = y
        self.r = r
        self.b = b
        self.colour = colour

k = kula(0,0,0,0,40,80,(150,150,150))
kule.append(k)
grav = 0.000981
    

while True:
    clock.tick(FPS)
    klatki += 1
    # if time.time() - czas > 1:
    #     czas = time.time()  
    #     print(f"{klatki} fps")
    #     klatki = 0
        
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
        k.vy += grav 
        if ktp((k.x,k.y))[0] + k.r > res[0]/2+bariera[0]/2:
            k.vx = -abs(k.vx)*k.b/100
        if ktp((k.x,k.y))[0]-k.r < res[0]/2-bariera[0]/2:
            k.vx = abs(k.vx)*k.b/100
        if ktp((k.x,k.y))[1]-k.r < res[1]/2-bariera[1]/2:
            k.vy = abs(k.vy)*k.b/100
        if ktp((k.x,k.y))[1] + k.r > res[1]/2+bariera[1]/2:
            k.vy = -abs(k.vy)*k.b/100
        if k.vy > 0.035:
            k.vy = 0.035
        
        
        pg.draw.circle(screen,color=k.colour,center=ktp((k.x,k.y)),radius=k.r)
        print(k.vy)

    pg.display.flip()
pg.quit()
