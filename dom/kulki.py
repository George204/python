import pygame as pg
import sys
import random as r

pg.init()

res = (1600,900)
kord = (0.0,0.0)
vel = (r.randrange(-100,100,1)/200,r.randrange(-100,100,1)/200)
sred = 6
bariera = (300,500)
kula = {kord:kord,vel:vel}
screen = pg.display.set_mode(res)

def kord_to_pix(mytuple):
    x , y = mytuple
    r = ((res[0]/2)+bariera[0]*x,(res[1]/2)+bariera[1]*y)
    return r
    

# petla gry
while True:
    screen.fill(color="grey")
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit(0)
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                sys.exit(0)
    kula[kord] = kula[kord][0] + kula[vel][0]/1000,kula[kord][1] + kula[vel][1]/1000
    pg.draw.rect(screen,color="blue", rect=((res[0]/2-bariera[0]/2-sred,res[1]/2-bariera[1]/2-sred),(bariera[0]+sred*2,bariera[1]+sred*2)))
    pg.draw.circle(screen,color="red",radius=sred,center=kord_to_pix(kula[kord]))
    if kord_to_pix(kula[kord])[0] < res[0]/2-bariera[0]/2 or  kord_to_pix(kula[kord])[0] > res[0]/2+bariera[0]/2:
        kula[vel] = -kula[vel][0],kula[vel][1] 
    if kord_to_pix(kula[kord])[1] < res[1]/2-bariera[1]/2 or  kord_to_pix(kula[kord])[1] > res[1]/2+bariera[1]/2:
        kula[vel] = kula[vel][0],-kula[vel][1]  
    pg.display.flip()
pg.quit()
