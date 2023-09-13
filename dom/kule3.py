import pygame as pg
import sys
import random as r
import time
import math as m


pg.init()

res = pg.math.Vector2(1010,1010)
screen = pg.display.set_mode(res)
bariera = pg.math.Vector2(500,500)
nkuli = 4
kule = []
mvx = 0.01
mvy = 0.01
FPS = 60
drawv = False
grav = 0.000981
def ktp(mytuple):
    x , y = mytuple
    ret = ((res.x/2)+bariera.x*x,(res.y/2)+bariera.y*y)
    return ret
def ktps(x):
    return ktp((x,0))[0]

class kula:
    def __init__(self, v, p, r, colour):
        self.v = v
        self.p = p
        self.r = r
        self.colour = colour

bx = (res.x/3-bariera.x/3)/res.x
by = (res.y/3-bariera.y/3)/res.y

for i in range(nkuli):
    k = kula(pg.math.Vector2(r.uniform(mvx*-1,mvx),r.uniform(mvy*-1,mvy)),pg.math.Vector2(r.uniform(-bx,bx),r.uniform(-by,by)),r.randint(10,50),(r.randint(0,255),r.randint(0,255),r.randint(0,255)))
    # k = kula(pg.math.Vector2(mvx,mvy).rotate(r.randint(0,360)),pg.math.Vector2(r.uniform(-bx,bx),r.uniform(-by,by)),r.randint(10,50),(r.randint(0,255),r.randint(0,255),r.randint(0,255)))
    kule.append(k)
clock = pg.time.Clock()
czas = time.time()    
klatki = 0
# petla gry
while True:
    clock.tick(FPS)
    klatki += 1
    dt = time.time()- czas
    czas = time.time()
        
    screen.fill(color="grey")
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit(0)
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                sys.exit(0) 
            if event.key == pg.K_SPACE:
                drawv = True       
        if event.type == pg.KEYUP:
            if event.key == pg.K_SPACE:
                drawv = False  
    pg.draw.rect(screen,color="blue", rect=((res.x/2-bariera.x/2,res.y/2-bariera.y/2),(bariera.x,bariera.y)))            
    
    for k in kule:
        ####bariera####
        if ktp(k.p)[0] + k.r > res.x/2+bariera.x/2:
            k.v.x = -abs(k.v.x)
        if ktp(k.p)[0]-k.r < res.x/2-bariera.x/2:
            k.v.x = abs(k.v.x)
        if ktp(k.p)[1]-k.r < res.y/2-bariera.y/2:
            k.v.y = abs(k.v.y)
        if ktp(k.p)[1] + k.r > res.y/2+bariera.y/2:
            k.v.y = -abs(k.v.y)
        ####kolisie####
        for i in kule:
            if k != i:    
                if (ktp((k.p.x,0))[0]-ktp((i.p.x,0))[0])**2 + (ktp((0,k.p.y))[1]-ktp((0,i.p.y))[1])**2 < (k.r+i.r)**2:
                    ang = k.v.angle_to(i.v)
                    posv = pg.math.Vector2(ktp(k.p)) - pg.math.Vector2(ktp(i.p))
                    if (ktp((k.p.x,0))[0]-ktp((i.p.x,0))[0])**2 + (ktp((0,k.p.y))[1]-ktp((0,i.p.y))[1])**2 > (ktp((k.p.x+k.v.x,0))[0]-ktp((i.p.x+i.v.x,0))[0])**2 + (ktp((0,k.p.y+k.v.y))[1]-ktp((0,i.p.y+i.v.y))[1])**2:    
                        k.v = k.v.reflect(posv)
                        i.v = i.v.reflect(posv)


        pg.draw.circle(screen,color=k.colour,center=ktp(k.p),radius=k.r)
    ###rysuj wektor###
        if drawv:
            pg.draw.line(screen,color="green",start_pos=ktp(k.p),end_pos=ktp(k.p+k.v*10),width=1)
            pg.draw.circle(screen,color="red",center=ktp(k.p+k.v*10),radius=3)
    ###PRZEMIESZCZENIE###
        k.p += k.v     
    ###FPS###
    if dt == 0:
        klatki = 1000
    else:
        klatki = 1/dt
    font = pg.font.Font('freesansbold.ttf', 24)  
    text = font.render('FPS: ' + str(round(klatki)), True, (0,255,0),(0,0,0))
    textRect = text.get_rect()
    screen.blit(text, textRect)     
            
    pg.display.flip()
pg.quit()
