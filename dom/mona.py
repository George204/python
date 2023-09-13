import random as r
import pygame as pg
import time
import sys
res = pg.math.Vector2(1000,1000)
ires = pg.math.Vector2(1,1)
pg.init()
screen = pg.display.set_mode(res)
clock = pg.time.Clock()
FPS = 30

def loss():
    img = []
    for i in range(int(ires.x*ires.y)):
        img.append(pg.math.Vector3(r.randint(0,7),r.randint(0,7),r.randint(0,7)))
    return img


gole = loss()

czas = time.time()
klatki = 0

while True:
    # clock.tick(FPS)
    klatki += 1
    dt = time.time()- czas
    czas = time.time()
        
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit(0)
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                sys.exit(0) 
    img = loss()
    for i in range(len(img)):
        pg.draw.rect(screen,color=(img[i].x*36,img[i].y*36,img[i].z*36),rect=(i%ires.x*(res.x/ires.x),i//ires.x*(res.y/ires.y),res.x/ires.x,res.y/ires.y))
    if img == gole:
        print("found")
        time.sleep(10)                       
    ###FPS###
    # if dt == 0:
    #     klatki = 1000
    # else:
    #     klatki = 1/dt
    # font = pg.font.Font('freesansbold.ttf', 24)  
    # text = font.render('FPS: ' + str(round(klatki)), True, (0,255,0),(0,0,0))
    # textRect = text.get_rect()
    # screen.blit(text, textRect)     
            
    pg.display.flip()
pg.quit()