import pygame as pg
import sys,time
import random as r
import math as m

pg.init()

res = (1000,1000)
screen = pg.display.set_mode(res)


clock = pg.time.Clock()
czas = time.time()
time.sleep(0.1)   
FPS = 10
klatki = 0
coners = [(100,100),(100,200),(200,200),(200,100),(100,100)]
while True:
    ####framerate limit####
    clock.tick(FPS)
    screen.fill("grey")
    dt = time.time() - czas
    czas = time.time()
    ####exiting####
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit(0)
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                sys.exit(0) 
    ####framerate####
    if dt == 0:
        klatki = 1000
    else:
        klatki = 1/dt
    font = pg.font.Font('freesansbold.ttf', 24)  
    text = font.render('FPS: ' + str(round(klatki)), True, (0,255,0),)
    textRect = text.get_rect()
    screen.blit(text, textRect) 
    ####draw squer####
    for i in range(len(coners)-1):
        pg.draw.line(screen, "green", coners[i], coners[i+1], 2)
    for i in range(len(coners)):
        coners[i] = (coners[i][0]+dt*100,coners[i][1]+dt*100)
    pg.display.flip()
