import pygame
pygame.init()
win=pygame.display.set_mode(size=[600,600])
pygame.display.set_caption("my game")
x,y=60,60
width=40
height=80
run=True
while run:
    for event in  pygame.event.get():
        if event.type==pygame.QUIT:
            run =False
    pygame.draw.circle(win ,(255,10,90),(50,50),45)
    pygame.display.flip()
