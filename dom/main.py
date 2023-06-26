import pygame as pg
import sys
import random

pg.init()

res = (1600, 900)
# res = (1280,720)
# res = (1920,1080)

ekr = (16, 9)
x = res[0]/ekr[0]
y = res[1]/ekr[1]
screen = pg.display.set_mode(res)
# logo i tytul okna
# logo = p.image.load("logo32x32.png")
# p.display.set_icon(logo)
# p.display.set_caption("Tysiąc")

bridge = [(6, 0), (7, 0), (8, 0), (9, 0), (6, 1), (7, 1), (8, 1), (9, 1), (6, 2), (7, 2), (8, 2), (9, 2), (6, 3), (7, 3), (8, 3), (9, 3), (6, 4), (7, 4),
          (8, 4), (9, 4), (6, 5), (7, 5), (8, 5), (9, 5), (6, 6), (7, 6), (8, 6), (9, 6), (6, 7), (7, 7), (8, 7), (9, 7), (6, 8), (7, 8), (8, 8), (9, 8),]
imgt = pg.image.load("t.png")
imgt = pg.transform.scale(imgt, (x, y))
triangle = [6, 8, imgt]


# petla gry
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit(0)
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                sys.exit(0)
            if event.key == pg.K_w and (triangle[0],triangle[1]-1) in bridge:
                triangle[1] -= 1
            if event.key == pg.K_s and (triangle[0],triangle[1]+1) in bridge:
                triangle[1] += 1
            if event.key == pg.K_a and (triangle[0]-1,triangle[1]) in bridge:
                triangle[0] -= 1
            if event.key == pg.K_d and (triangle[0]+1,triangle[1]) in bridge:
                triangle[0] += 1
    for i in range(16):
        for j in range(9):
            pg.draw.rect(screen, (0+i*16, 0+j*16, 0), (i*x, j*y, x, y),)
    for i in bridge:
        pg.draw.rect(screen, "grey", (i[0]*x, i[1]*y, x, y),)
    screen.blit(triangle[2], (triangle[0]*x, triangle[1]*y))
    pg.display.flip()
pg.quit()
