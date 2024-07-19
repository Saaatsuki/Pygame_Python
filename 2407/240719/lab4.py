import pygame 
import random

pygame.init()
screen = pygame.display.set_mode((800,600))

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
            pygame.draw.circle(screen,color,event.pos,30)
            pygame.display.flip()
pygame.quit()