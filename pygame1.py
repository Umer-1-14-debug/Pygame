import pygame
pygame.init()
screen=pygame.display.set_mode((400,300))
done=False
while not done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done=True
    pygame.draw.rect(screen,(00,100,100),pygame.rect(30,30,100,200))
    pygame.display.flip()