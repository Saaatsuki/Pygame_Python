import pygame
import random

pygame.init()
screen = pygame.display.set_mode((800,600))

color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
x,y = (400,300)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                pygame.draw.line(screen,color,(x,y),(x,y - 10),5)
                y -= 10
            elif event.key == pygame.K_DOWN:
                pygame.draw.line(screen,color,(x,y),(x,y+10),5)
                y += 10
            elif event.key == pygame.K_LEFT:
                pygame.draw.line(screen,color,(x,y),(x-10,y),5)
                y -= 10
            elif event.key == pygame.K_RIGHT:
                pygame.draw.line(screen,color,(x,y),(x+10,y),5)
                y += 10
            pygame.display.flip()
pygame.quit()
                