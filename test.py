import pygame,sys,random,math
pygame.init()
screen=pygame.display.set_mode([640,640])
screen.fill([255,255,255])
for x in range(640):
    y=int(math.sin(x/640.0*4.0*math.pi)*200+240)
    pygame.draw.rect(screen,[255,0,0],[x,y,1,1],3)
pygame.display.flip()
while True:
    for event in pygame.event.get():
        if event.type==pygame.quit:
            sys.exit()